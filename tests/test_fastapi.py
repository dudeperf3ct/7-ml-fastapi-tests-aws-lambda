from http import HTTPStatus

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK


def test_healthcheck_endpoint():
    response = client.get("/healthcheck")
    assert response.status_code == HTTPStatus.OK


# # TODO: not working as expected
# def test_classify_endpoint():
#     response = client.post("/classify/", json={"input_text": "\'"})
#     assert response.status_code == 422 # Unprocessable Entity
#     response = client.post("/classify/", json={"input_text": "this is positive sentence"})
#     assert response.status_code == HTTPStatus.OK
