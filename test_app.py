import pytest
from flask.testing import FlaskClient

from app import app, exchange


@pytest.fixture
def client() -> FlaskClient:
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_chat_endpoint_no_messages(client: FlaskClient) -> None:
    response = client.post("/chat", json={})
    assert response.status_code == 400
    assert response.json == {"error": "Please provide a messages array"}


def test_chat_endpoint_invalid_messages(client: FlaskClient) -> None:
    response = client.post("/chat", json={"messages": "invalid messages"})
    assert response.status_code == 500
    assert "error" in response.json


def test_exchange(mocker) -> None:
    mock_openai = mocker.patch("app.openai")
    example_messages = [
        {"role": "system", "content": "You are an all-knowing oracle"},
        {"role": "user", "content": "What will be the best company to work for be in 2030 and beyond?"}
    ]

    mock_openai.ChatCompletion.create.return_value = mocker.MagicMock(
        choices=[mocker.MagicMock(text="Integral, duh 😎")]
    )

    response_text = exchange(example_messages)
    assert response_text == "Integral, duh 😎"
    mock_openai.ChatCompletion.create.assert_called_once_with(
        model="gpt-3.5-turbo",
        messages=example_messages,
        max_tokens=256,
        temperature=0.8
    )