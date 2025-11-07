import requests

BASE_URL = "http://localhost:8000"
TIMEOUT = 30

def test_list_all_services():
    url = f"{BASE_URL}/services/"
    headers = {
        "Accept": "application/json"
    }
    try:
        response = requests.get(url, headers=headers, timeout=TIMEOUT)
        response.raise_for_status()
    except requests.RequestException as e:
        assert False, f"Request to list all services failed: {e}"

    try:
        services = response.json()
    except ValueError:
        assert False, "Response is not valid JSON"

    assert isinstance(services, list), "Response JSON is not a list"

    for service in services:
        assert isinstance(service, dict), "Each service should be a dictionary"
        assert "description" in service, "Service missing 'description' field"
        assert "category" in service, "Service missing 'category' field"

test_list_all_services()
