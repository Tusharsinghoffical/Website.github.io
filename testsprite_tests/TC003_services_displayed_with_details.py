import requests

BASE_URL = "http://localhost:8000"
TIMEOUT = 30

def test_services_displayed_with_details():
    url = f"{BASE_URL}/services"
    try:
        response = requests.get(url, timeout=TIMEOUT)
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        data = response.json()
        assert isinstance(data, list), f"Expected response to be a list, got {type(data)}"
        assert len(data) > 0, "Expected at least one service in the response"

        for service in data:
            assert isinstance(service, dict), "Each service should be a dictionary"
            assert "name" in service, "Service missing 'name' field"
            assert isinstance(service["name"], str) and service["name"].strip() != "", "Service 'name' should be a non-empty string"
            assert "description" in service, "Service missing 'description' field"
            assert isinstance(service["description"], str) and service["description"].strip() != "", "Service 'description' should be a non-empty string"
            assert "icon" in service, "Service missing 'icon' field"
            assert isinstance(service["icon"], str) and service["icon"].strip() != "", "Service 'icon' should be a non-empty string"
    except requests.exceptions.RequestException as e:
        assert False, f"Request failed: {e}"


test_services_displayed_with_details()