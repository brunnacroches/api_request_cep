from src.infra.requests.api_consumer import ApiConsumer

def test_get_ok_message():
    api_consumer = ApiConsumer()

    request_response = api_consumer.get_ok_message()

    assert request_response.request.method == 'GET'
    assert request_response.request.url == 'http://localhost:5007/'

    assert request_response.status_code == 200
    assert "message" in request_response.response["data"]