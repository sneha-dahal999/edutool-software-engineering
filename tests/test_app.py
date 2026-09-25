import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_tc01_login_page_loads(client):
    response = client.get("/login")
    assert response.status_code == 200
    assert b"Login" in response.data


def test_tc02_valid_login(client):
    response = client.post(
        "/login",
        data={"username": "sneha", "password": "password123"},
    )
    assert response.status_code == 302
    assert response.headers["Location"].endswith("/catalogue")


def test_tc03_invalid_login(client):
    response = client.post(
        "/login",
        data={"username": "sneha", "password": "wrong-password"},
    )
    assert response.status_code == 200
    assert b"Invalid username or password." in response.data


def test_tc04_catalogue_loads_after_login(client):
    client.post(
        "/login",
        data={"username": "sneha", "password": "password123"},
    )
    response = client.get("/catalogue")
    assert response.status_code == 200
    assert b"Edutool.com E-Book Catalogue" in response.data


def test_tc05_catalogue_search(client):
    client.post(
        "/login",
        data={"username": "sneha", "password": "password123"},
    )
    response = client.get("/catalogue?q=Python")
    assert response.status_code == 200
    assert b"Python Basics" in response.data
