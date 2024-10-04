def test_create_user(client):
    response = client.post(
        "/users/",
        json={"email": "user@example.com", "password": "password123", "is_manager": False}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "user@example.com"
    assert "id" in data

def test_create_existing_user(client):
    # 이미 생성된 사용자를 다시 생성 시도
    response = client.post(
        "/users/",
        json={"email": "user@example.com", "password": "password123", "is_manager": False}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"

def test_login_user(client):
    response = client.post(
        "/auth/",
        data={"username": "user@example.com", "password": "password123"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_invalid_user(client):
    response = client.post(
        "/auth/",
        data={"username": "invalid@example.com", "password": "wrongpassword"}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "사용자 이름이나 비밀번호가 올바르지 않습니다."