import requests

BASE_URL = "http://localhost:8000"
CONTACT_ENDPOINT = "/contact/"
TIMEOUT = 30

def test_handle_contact_form_submission():
    url = BASE_URL + CONTACT_ENDPOINT
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    valid_payload = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "subject": "Inquiry about services",
        "message": "I would like to know more about your services."
    }

    # Test successful submission
    try:
        response = requests.post(url, json=valid_payload, headers=headers, timeout=TIMEOUT)
        assert response.status_code == 200 or response.status_code == 201, f"Expected 200 or 201, got {response.status_code}"
        response_data = response.json()
        # Basic check if response acknowledges the submission
        assert "success" in response_data or "message" in response_data, "Response missing success confirmation"
    except requests.RequestException as e:
        assert False, f"Request failed with exception: {e}"

    # Test submission with missing required fields to validate error handling
    invalid_payloads = [
        {},  # empty payload
        {"name": "", "email": "", "subject": "", "message": ""},  # all empty strings
        {"email": "invalid-email-format", "name": "John Doe", "subject": "Test", "message": "Hi"}, # invalid email
        {"name": "John Doe", "subject": "Test", "message": "Hi"}  # missing email
    ]
    for payload in invalid_payloads:
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=TIMEOUT)
            # Expecting client error status indicating validation failure
            assert response.status_code >= 400 and response.status_code < 500, (
                f"Expected 4xx status code for invalid payload {payload}, got {response.status_code}"
            )
            # Optionally check that the response contains validation error messages
            try:
                resp_json = response.json()
                assert "errors" in resp_json or "error" in resp_json or "message" in resp_json, "Expected validation error message in response"
            except ValueError:
                # Response is not json, skip detailed validation
                pass
        except requests.RequestException as e:
            assert False, f"Request for invalid payload failed with exception: {e}"

test_handle_contact_form_submission()