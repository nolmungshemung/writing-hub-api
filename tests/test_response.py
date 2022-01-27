import json

def test_main_page(client):
    response = client.get("/")
    assert response.status_code == 200

'''def test_main_contents(client):
    response = client.get("/services/main_contents?keyword=test")
    assert response.status_code == 200
    assert json.loads(response.text)['msg'] == "응답 성공"'''