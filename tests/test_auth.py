def test_main_page(client):
    response = client.get("/")
    assert response.status_code == 200