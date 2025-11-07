import requests

def test_serve_about_page():
    base_url = "http://localhost:8000"
    endpoint = "/about/"
    url = base_url + endpoint
    headers = {
        "Accept": "text/html"
    }
    try:
        response = requests.get(url, headers=headers, timeout=30)
    except requests.RequestException as e:
        assert False, f"Request to {url} failed with exception: {e}"

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    response_text = response.text

    # Check for presence of owner information keywords, assuming it contains owner's name, skills or similar
    # These should be adjusted if the actual about page content is known
    expected_keywords = ["owner", "skills", "experience", "background"]
    found_keywords = [kw for kw in expected_keywords if kw.lower() in response_text.lower()]
    assert len(found_keywords) > 0, f"Response does not contain expected owner information keywords: {expected_keywords}"

test_serve_about_page()