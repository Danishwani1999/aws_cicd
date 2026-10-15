
from app import app


def test_home_returns_200():
    resp = app.test_client().get("/")
    assert resp.status_code == 200


def test_health_reports_ok():
    resp = app.test_client().get("/health")
    assert resp.get_json()["status"] == "ok"
