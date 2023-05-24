from settings.app import app
from settings.config import APISettings, init_settings
from fastapi.testclient import TestClient

client = TestClient(app)

def init_new_settings():
    apisettings = APISettings(host="asdf", port="9098")
    return apisettings

app.dependency_overrides[init_settings] = init_new_settings

def test_hello():
    response = client.get("/hello")
    print(response.json())
    assert response.status_code == 200    