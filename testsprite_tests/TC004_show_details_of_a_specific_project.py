import requests

BASE_URL = "http://localhost:8000"
TIMEOUT = 30


def test_show_details_of_specific_project():
    # First, list all projects to get a valid project ID
    try:
        list_resp = requests.get(f"{BASE_URL}/projects/", timeout=TIMEOUT)
        assert list_resp.status_code == 200, "Failed to get list of projects"
        projects = list_resp.json()
        assert isinstance(projects, list), "Projects response is not a list"
        assert len(projects) > 0, "No projects available to test"

        valid_id = None
        # Projects might be a list of dicts with 'id' and project details
        for project in projects:
            if "id" in project:
                valid_id = project["id"]
                break
        assert valid_id is not None, "No project with 'id' found in the projects list"

        # Test valid project ID
        detail_resp = requests.get(f"{BASE_URL}/projects/{valid_id}/", timeout=TIMEOUT)
        assert detail_resp.status_code == 200, f"Expected 200 for valid project ID {valid_id}, got {detail_resp.status_code}"
        project_detail = detail_resp.json()
        assert isinstance(project_detail, dict), "Project detail response is not a dictionary"
        assert project_detail.get("id") == valid_id, "Returned project ID does not match requested ID"

        # Test invalid project ID (assuming ID -1 does not exist)
        invalid_id = -1
        invalid_resp = requests.get(f"{BASE_URL}/projects/{invalid_id}/", timeout=TIMEOUT)
        # Expecting 404 Not Found or similar status code for invalid ID
        assert invalid_resp.status_code in {400, 404}, f"Expected error status for invalid project ID, got {invalid_resp.status_code}"

    except requests.RequestException as e:
        assert False, f"Request failed: {e}"


test_show_details_of_specific_project()
