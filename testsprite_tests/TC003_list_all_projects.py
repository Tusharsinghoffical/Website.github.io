import requests

BASE_URL = "http://localhost:8000"

def test_list_all_projects():
    url = f"{BASE_URL}/projects/"
    headers = {
        'Accept': 'application/json',
    }
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
    except requests.RequestException as e:
        assert False, f"Request to list all projects failed: {e}"

    # Validate status code
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    try:
        projects = response.json()
    except ValueError:
        assert False, "Response is not valid JSON"

    # Validate that the response is a list (of projects)
    assert isinstance(projects, list), "Response JSON is not a list"

    if projects:
        project = projects[0]
        # Validate the project has keys typically expected
        for key in ('id', 'name', 'description', 'images'):
            assert key in project, f"Project item missing expected key: {key}"

        # Validate types of fields
        assert isinstance(project['id'], int) or isinstance(project['id'], str), "'id' should be int or str"
        assert isinstance(project['name'], str), "'name' should be str"
        assert isinstance(project['description'], str), "'description' should be str"
        # images might be a list or dict depending on implementation, so we check presence
        assert project['images'] is not None, "'images' should not be None"

test_list_all_projects()