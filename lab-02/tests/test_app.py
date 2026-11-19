import pytest

import app as app_module
from app import app


@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(app_module, "COUNTER_FILE", tmp_path / "visits.txt")
    monkeypatch.setattr(app_module, "DATABASE_URL", None)
    return app.test_client()


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_data(as_text=True) == "ok\n"


def test_ready(client):
    r = client.get("/ready")
    assert r.status_code == 200
    assert r.get_json()["ready"] is True
    assert r.get_json()["store"].startswith("file:")


def test_visits_starts_at_one(client):
    r = client.get("/visits")
    assert r.status_code == 200
    assert r.get_json() == {"visits": 1, "store": "file"}


def test_visits_counts_up(client):
    first = client.get("/visits").get_json()["visits"]
    second = client.get("/visits").get_json()["visits"]
    assert second == first + 1