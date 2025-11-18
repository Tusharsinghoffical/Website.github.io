import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://localhost:8000"
AUTH = HTTPBasicAuth("tusharsinghkumar2002", "Tushar@2002")
TIMEOUT = 30

def test_contact_form_submission_and_notification():
    contact_url = f"{BASE_URL}/contact/"
    headers = {"Content-Type": "application/json"}
    payload = {
        "name": "Test Visitor",
        "email": "testvisitor@example.com",
        "subject": "Test Inquiry",
        "message": "This is a test message for contact form submission."
    }

    try:
        response = requests.post(contact_url, json=payload, headers=headers, auth=AUTH, timeout=TIMEOUT)
        # Check that the form was submitted successfully
        assert response.status_code == 200 or response.status_code == 201, f"Unexpected status code: {response.status_code}"

        # Response is expected to confirm success and notify that email was sent
        json_response = response.json()
        # Validate essential keys and values in response
        assert isinstance(json_response, dict), "Response is not a JSON object"
        assert "success" in json_response, "'success' key missing in response"
        assert json_response["success"] is True, "Success flag not True"
        assert "message" in json_response, "'message' key missing in response"
        # Check the success message contains expected text
        assert "thank you" in json_response["message"].lower() or "success" in json_response["message"].lower(), \
            "Success message text not found"

    except requests.RequestException as e:
        assert False, f"Request failed: {e}"

test_contact_form_submission_and_notification()