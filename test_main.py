from main import get_html_data


def test_get_html_data():
    data = get_html_data()
    assert "Hello, World!" in data
