from Blog import create_app


def test_config():
    assert not create_app().testing
    assert create_app({"TESTING":True}).testing


def test_hello():
    response = client.get("/hello")
    assert response.data == b"Hello world!"
