import pytest
from django.test import Client


@pytest.mark.django_db
def test_health_check():
    client = Client()
    response = client.get("/health/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Django Application"}


@pytest.mark.django_db
def test_invalid_route():
    client = Client()
    response = client.get("/invalid")
    assert response.status_code == 404
