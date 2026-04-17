import pytest
from YouGileApi import YouGileApi


@pytest.fixture(scope="session")
def api():
    return YouGileApi()


@pytest.fixture(scope="session")
def token(api):
    key = api.get_token()
    yield key


@pytest.fixture
def created_project(api, token):
    response = api.create_project(token, "Project_for_test")
    assert response.status_code in (200, 201)

    project_id = response.json()["id"]
    yield project_id

    api.delete_project(token, project_id)


def test_create_project_positive(api, token):
    response = api.create_project(token, "NewProject_test_01")
    assert response.status_code in (200, 201)

    data = response.json()
    assert "id" in data
    assert data["id"]


def test_get_project_positive(api, token, created_project):
    response = api.get_project(token, created_project)
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == created_project


def test_update_project_positive(api, token, created_project):
    response = api.update_project(token, created_project, title="Project_updated")
    assert response.status_code in (200, 201)

    data = response.json()
    assert data["id"] == created_project


def test_get_project_negative(api, token):
    response = api.get_project(token, "invalid-id")
    assert response.status_code >= 400


def test_create_project_negative(api, token):
    response = api.create_project(token, "")
    assert response.status_code >= 400


def test_update_project_negative(api, token):
    response = api.update_project(token, "invalid-id", title="Updated")
    assert response.status_code >= 400
