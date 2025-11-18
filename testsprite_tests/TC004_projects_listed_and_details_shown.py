import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://localhost:8000"
USERNAME = "tusharsinghkumar2002"
PASSWORD = "Tushar@2002"
TIMEOUT = 30

def test_projects_listed_and_details_shown():
    auth = HTTPBasicAuth(USERNAME, PASSWORD)
    headers = {'Accept': 'application/json'}
    # Step 1: Get the list of projects
    try:
        resp_list = requests.get(f"{BASE_URL}/projects", auth=auth, headers=headers, timeout=TIMEOUT)
        assert resp_list.status_code == 200, f"Expected 200, got {resp_list.status_code}"
        content_type = resp_list.headers.get('Content-Type', '')
        assert 'application/json' in content_type, f"Expected JSON response, got {content_type}"
        projects = resp_list.json()
        assert isinstance(projects, list), "Projects list response is not a list"
        assert len(projects) > 0, "Projects list is empty"
        
        # Pick the first project for details
        first_project = projects[0]
        assert 'id' in first_project, "Project does not have 'id'"
        project_id = first_project['id']

        # Step 2: Get project details
        resp_detail = requests.get(f"{BASE_URL}/projects/{project_id}", auth=auth, headers=headers, timeout=TIMEOUT)
        assert resp_detail.status_code == 200, f"Expected 200 on project detail, got {resp_detail.status_code}"
        content_type_detail = resp_detail.headers.get('Content-Type', '')
        assert 'application/json' in content_type_detail, f"Expected JSON response, got {content_type_detail}"
        project_detail = resp_detail.json()
        # Validate that the detail matches the listed project id
        assert project_detail.get('id') == project_id, "Project detail id does not match listed project id"
        # Validate some expected fields presence
        assert 'project_name' in project_detail, "Project detail missing 'project_name'"
        assert 'project_description' in project_detail, "Project detail missing 'project_description'"

    except (requests.RequestException, AssertionError) as e:
        raise AssertionError(f"Test failed: {str(e)}")

test_projects_listed_and_details_shown()