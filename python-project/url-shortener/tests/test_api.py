
import uuid

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import delete

from app.main import app
from app.database import SessionLocal
from app.models import URL


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def created_codes():
    codes = []

    yield codes

    # Remove test records after each test
    db = SessionLocal()

    try:
        if codes:
            db.execute(
                delete(URL).where(URL.code.in_(codes))
            )
            db.commit()
    finally:
        db.close()


def unique_alias():
    return f"test-{uuid.uuid4().hex[:10]}"


def test_health_check(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_create_short_url(client, created_codes):
    response = client.post(
        "/api/shorten",
        json={
            "original_url": "https://www.google.com"
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert len(data["code"]) == 7
    assert data["original_url"] == "https://www.google.com/"
    assert data["click_count"] == 0

    created_codes.append(data["code"])


def test_custom_alias(client, created_codes):
    alias = unique_alias()

    response = client.post(
        "/api/shorten",
        json={
            "original_url": "https://github.com",
            "custom_alias": alias,
        },
    )

    assert response.status_code == 201
    assert response.json()["code"] == alias

    created_codes.append(alias)


def test_duplicate_alias(client, created_codes):
    alias = unique_alias()

    first_response = client.post(
        "/api/shorten",
        json={
            "original_url": "https://github.com",
            "custom_alias": alias,
        },
    )

    assert first_response.status_code == 201
    created_codes.append(alias)

    second_response = client.post(
        "/api/shorten",
        json={
            "original_url": "https://www.google.com",
            "custom_alias": alias,
        },
    )

    assert second_response.status_code == 409


def test_reserved_alias(client):
    response = client.post(
        "/api/shorten",
        json={
            "original_url": "https://github.com",
            "custom_alias": "admin",
        },
    )

    assert response.status_code == 400


def test_url_expiry(client, created_codes):
    response = client.post(
        "/api/shorten",
        json={
            "original_url": "https://www.amazon.com",
            "expires_in_days": 1,
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["expires_at"] is not None

    created_codes.append(data["code"])


def test_invalid_url(client):
    response = client.post(
        "/api/shorten",
        json={
            "original_url": "javascript:alert(1)",
        },
    )

    assert response.status_code == 422


def test_redirect_and_click_count(client, created_codes):
    alias = unique_alias()

    create_response = client.post(
        "/api/shorten",
        json={
            "original_url": "https://github.com",
            "custom_alias": alias,
        },
    )

    assert create_response.status_code == 201
    created_codes.append(alias)

    # Check the initial click count
    stats_before = client.get(f"/api/stats/{alias}")

    assert stats_before.status_code == 200
    assert stats_before.json()["click_count"] == 0

    # Follow the redirect manually so the test client
    # does not navigate to the external website
    redirect_response = client.get(
        f"/{alias}",
        follow_redirects=False,
    )

    assert redirect_response.status_code == 302
    assert redirect_response.headers["location"] == "https://github.com/"

    # Verify that the click count increased
    stats_after = client.get(f"/api/stats/{alias}")

    assert stats_after.json()["click_count"] == 1
