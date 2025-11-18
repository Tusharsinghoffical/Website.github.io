import requests
from requests.auth import HTTPBasicAuth

def test_about_section_information_display():
    base_url = "http://localhost:8000"
    endpoint = "/about"
    url = base_url + endpoint
    auth = HTTPBasicAuth("tusharsinghkumar2002", "Tushar@2002")
    headers = {
        "Accept": "application/json"
    }
    try:
        response = requests.get(url, auth=auth, headers=headers, timeout=30)
        response.raise_for_status()
    except requests.RequestException as e:
        assert False, f"Request to about page failed: {e}"

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    try:
        data = response.json()
    except ValueError:
        assert False, "Response is not valid JSON"

    # Validate that key information exists about freelancer: skills and experience
    # Since no exact schema, we expect keys 'skills' and 'experience' in json response
    assert "skills" in data, "'skills' key not found in about page response"
    assert isinstance(data["skills"], list), "'skills' should be a list"
    assert len(data["skills"]) > 0, "'skills' list should not be empty"

    assert "experience" in data, "'experience' key not found in about page response"
    # experience can be string or list, allow both but not empty
    exp = data["experience"]
    assert (isinstance(exp, str) and exp.strip() != "") or (isinstance(exp, list) and len(exp) > 0), \
        "'experience' should be a non-empty string or non-empty list"

test_about_section_information_display()