def test_create_park(client, test_db):
    # 관리자 사용자 생성
    response = client.post(
        "/users/",
        json={"email": "manager@example.com", "password": "managerpassword", "is_manager": True}
    )
    assert response.status_code == 200
    manager = response.json()

    # 관리자 로그인
    response = client.post(
        "/auth/",
        data={"username": "manager@example.com", "password": "managerpassword"}
    )
    assert response.status_code == 200
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 놀이공원 생성
    response = client.post(
        "/parks/",
        json={"name": "Fun Park", "description": "A fun amusement park", "location": "Seoul"},
        headers=headers
    )
    assert response.status_code == 200
    park = response.json()
    assert park["name"] == "Fun Park"
    assert park["description"] == "A fun amusement park"
    assert park["location"] == "Seoul"
    assert park["manager_id"] == manager["id"]

def test_create_park_unauthorized(client):
    # 일반 사용자 로그인
    response = client.post(
        "/auth/",
        data={"username": "user@example.com", "password": "password123"}
    )
    assert response.status_code == 200
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 놀이공원 생성 시도 (관리자 권한 필요)
    response = client.post(
        "/parks/",
        json={"name": "Unauthorized Park", "description": "Should fail", "location": "Busan"},
        headers=headers
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "권한이 부족합니다."