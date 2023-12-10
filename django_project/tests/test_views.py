import pytest

def test_that_home_redirects(client):
    response = client.get("/")
    assert response.status_code == 302