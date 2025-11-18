import requests
from requests.auth import HTTPBasicAuth

def test_homepage_loads_successfully():
    base_url = "http://localhost:8000/"
    auth = HTTPBasicAuth("tusharsinghkumar2002", "Tushar@2002")
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }
    try:
        response = requests.get(base_url, auth=auth, headers=headers, timeout=30)
        response.raise_for_status()
        content = response.text.lower()
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
        # Check presence of some expected keywords in the homepage that indicate introduction to freelancer
        assert "freelancer" in content or "portfolio" in content or "welcome" in content, \
            "Homepage introduction content not found"
    except requests.exceptions.RequestException as e:
        assert False, f"HTTP request failed: {e}"

test_homepage_loads_successfully()