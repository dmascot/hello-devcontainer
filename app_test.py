import app


def test_sayMyName():
    assert app.sayMyName() == "Hello there"


def test_main():
    with app.simple_app.test_client() as test_client:
        response = test_client.get("/")
        assert response.status_code == 200
        assert b"Hello there" in response.data


def test_db_connection():
    assert app.db_connection()
