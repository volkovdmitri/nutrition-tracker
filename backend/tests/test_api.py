from fastapi.testclient import TestClient

from app.application import create_app

app = create_app()
client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
