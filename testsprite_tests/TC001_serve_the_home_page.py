import requests

def test_serve_home_page():
    base_url = "http://localhost:8000"
    url = f"{base_url}/"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }
    try:
        response = requests.get(url, headers=headers, timeout=30)
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
        content_type = response.headers.get('Content-Type', '')
        assert "text/html" in content_type, f"Expected 'text/html' in Content-Type but got {content_type}"
        assert len(response.text) > 0, "Home page content is empty"
    except requests.RequestException as e:
        assert False, f"Request to home page failed: {e}"

test_serve_home_page()