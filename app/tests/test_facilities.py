def test_create_facility(client, test_db):
    # 관리자 로그인
    response = client.post(
        "/auth/",
        data={"username": "manager@example.com", "password": "managerpassword"}
    )
    assert response.status_code == 200
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 기존 놀이공원 조회
    response = client.get("/parks/", headers=headers)
    assert response.status_code == 200
    parks = response.json()
    assert len(parks) > 0
    park_id = parks[0]["id"]

    # 시설 생성
    response = client.post(
        "/facilities/",
        json={"name": "Roller Coaster", "description": "Exciting roller coaster", "capacity": 20, "park_id": park_id},
        headers=headers
    )
    assert response.status_code == 200
    facility = response.json()
    assert facility["name"] == "Roller Coaster"
    assert facility["description"] == "Exciting roller coaster"
    assert facility["capacity"] == 20
    assert facility["park_id"] == park_id

def test_create_facility_non_manager(client, test_db):
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
        "/facilities/",
        json={"name": "Water Slide", "description": "Fun water slide", "capacity": 15, "park_id": 1},
        headers=headers
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "권한이 부족합니다."