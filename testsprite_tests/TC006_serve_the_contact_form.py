import requests

def test_serve_contact_form():
    base_url = "http://localhost:8000"
    url = f"{base_url}/contact/"
    headers = {
        "Accept": "text/html",
    }
    try:
        response = requests.get(url, headers=headers, timeout=30)
    except requests.RequestException as e:
        assert False, f"Request to {url} failed: {e}"

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    content_type = response.headers.get("Content-Type", "")
    assert "text/html" in content_type, f"Expected 'text/html' in Content-Type header, got '{content_type}'"
    # Check for presence of form in content to verify contact form is served
    assert "<form" in response.text and "contact" in response.text.lower(), "Contact form HTML not found in response content"

test_serve_contact_form()