def test_create_ticket(client, test_db):
    # 관리자 로그인
    response = client.post(
        "/auth/",
        data={"username": "manager@example.com", "password": "managerpassword"}
    )
    assert response.status_code == 200
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 놀이공원 조회
    response = client.get("/parks/", headers=headers)
    assert response.status_code == 200
    parks = response.json()
    assert len(parks) > 0
    park_id = parks[0]["id"]

    # 티켓 생성
    response = client.post(
        f"/tickets/{park_id}/",
        json={"title": "General Admission", "description": "Access to all rides", "price": 50.0},
        headers=headers
    )
    assert response.status_code == 200
    ticket = response.json()
    assert ticket["title"] == "General Admission"
    assert ticket["description"] == "Access to all rides"
    assert ticket["price"] == 50.0
    assert ticket["park_id"] == park_id

def test_create_purchase(client, test_db):
    # 일반 사용자 로그인
    response = client.post(
        "/auth/",
        data={"username": "user@example.com", "password": "password123"}
    )
    assert response.status_code == 200
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 티켓 조회
    response = client.get("/tickets/1/", headers=headers)
    assert response.status_code == 200
    tickets = response.json()
    assert len(tickets) > 0
    ticket_id = tickets[0]["id"]

    # 구매 생성
    response = client.post(
        "/purchases/",
        json={"ticket_id": ticket_id, "quantity": 2},
        headers=headers
    )
    assert response.status_code == 200
    purchase = response.json()
    assert purchase["ticket_id"] == ticket_id
    assert purchase["quantity"] == 2
    assert purchase["qr_code"] is not None