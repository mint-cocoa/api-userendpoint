# tests/test_purchases.py
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, get_db
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 테스트용 데이터베이스 설정
@pytest.fixture(scope="module")
def test_db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

# 의존성 재정의
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_purchase():
    # 사용자 생성
    response = client.post(
        "/users/",
        json={"email": "test@example.com", "password": "testpassword", "is_manager": False}
    )
    assert response.status_code == 200
    user = response.json()
    assert user["email"] == "test@example.com"

    # 로그인하여 토큰 획득
    response = client.post(
        "/auth/token",
        data={"username": "test@example.com", "password": "testpassword"}
    )
    assert response.status_code == 200
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 티켓 생성 (관리자 권한 필요)
    # 관리자 계정 생성
    response = client.post(
        "/users/",
        json={"email": "manager@example.com", "password": "managerpassword", "is_manager": True}
    )
    assert response.status_code == 200

    # 관리자 로그인
    response = client.post(
        "/auth/token",
        data={"username": "manager@example.com", "password": "managerpassword"}
    )
    assert response.status_code == 200
    manager_token = response.json()["access_token"]
    manager_headers = {"Authorization": f"Bearer {manager_token}"}

    # 파크 생성
    response = client.post(
        "/parks/",
        json={"name": "Test Park", "description": "A test park", "location": "Test Location"},
        headers=manager_headers
    )
    assert response.status_code == 200
    park = response.json()

    # 티켓 생성
    response = client.post(
        f"/tickets/{park['id']}/",
        json={"title": "Test Ticket", "description": "A test ticket", "price": 10.0},
        headers=manager_headers
    )
    assert response.status_code == 200
    ticket = response.json()

    # 구매 생성
    response = client.post(
        "/purchases/",
        json={"ticket_id": ticket['id'], "quantity": 2},
        headers=headers
    )
    assert response.status_code == 200
    purchase = response.json()
    assert purchase["ticket_id"] == ticket['id']
    assert purchase["quantity"] == 2
    assert purchase["qr_code"] is not None