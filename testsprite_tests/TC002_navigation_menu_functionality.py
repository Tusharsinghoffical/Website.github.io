import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://localhost:8000"
AUTH = HTTPBasicAuth("tusharsinghkumar2002", "Tushar@2002")
TIMEOUT = 30

def test_navigation_menu_functionality():
    try:
        # Step 1: Load homepage
        homepage_resp = requests.get(f"{BASE_URL}/", auth=AUTH, timeout=TIMEOUT)
        assert homepage_resp.status_code == 200, f"Expected 200 OK but got {homepage_resp.status_code}"

        content = homepage_resp.text
        content_lower = content.lower()

        # Step 2: Check navigation menu visibility by looking for expected navigation elements or id/class
        nav_indicators = [
            'nav',               # generic nav tag
            'navigation',        # class or id
            'menu',              # common menu keyword
            'href="#services"',  # link to services section
            'href="#projects"',  # link to projects section
            'href="#about"',     # link to about section
            'href="#contact"'    # link to contact section
        ]

        nav_found = any(indicator in content_lower for indicator in nav_indicators)
        assert nav_found, "Navigation menu not found or not visible on the homepage."

        # Step 3: Test navigation to different portfolio sections by requesting them if separate URLs or anchors
        # Since this is a single page usually, check that anchors exist in the homepage content:
        sections = ["services", "projects", "about", "contact"]
        for section in sections:
            anchor = f'href="#'+section+'"'
            anchor_lower = anchor.lower()
            assert anchor_lower in content_lower, f"Navigation link to section '{section}' not found."

        # Optionally test that section content also exists in homepage
        # For example, presence of section headers or IDs
        section_id_tags = [f'id="{sec}"' for sec in sections]
        for tag in section_id_tags:
            assert tag.lower() in content_lower, f"Section with {tag} not found in homepage content."

    except requests.RequestException as e:
        raise AssertionError(f"HTTP request failed: {e}")

test_navigation_menu_functionality()
