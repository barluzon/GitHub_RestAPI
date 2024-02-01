import requests
import pytest

base_url = "https://api.github.com"
repo_owner = "topq-practice"
repo_name = "api-practice"
token = "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"
headers = {"Authorization": f"token {token}"}
initial_issue_count = 0


@pytest.fixture(scope="session", autouse=True)
def set_global_issue_count():
    global initial_issue_count
    initial_issue_count = len(get_all_open_issues())


# Test scenario 1
def test_get_all_open_issues():
    get_all_open_issues()


# Test scenario 2
def test_get_issues_with_label(label='practice1'):
    get_all_open_issues(label)


# Test scenarios 3 + 4
def test_create_new_issue():
    issue_data = {
        "title": "Bar's issue",
        "body": "This issue was created via REST API from Python by Bar",
        "labels": ["practice1"],
        "assignees": [repo_owner]
    }
    response = requests.post(f"{base_url}/repos/{repo_owner}/{repo_name}/issues", json=issue_data, headers=headers)
    assert response.status_code == 201
    new_issue_number = response.json()["number"]
    print(f"\nNew issue created with number: {new_issue_number}")


# Test scenario 5
def test_verify_new_issue_in_list():
    issues = get_all_open_issues()
    assert len(issues) == initial_issue_count + 1
    assert issues[0]["title"] == "Bar's issue"


# Test scenario 6
def test_update_issue():
    issue_number = get_issue_number_by_title("Bar's issue")
    update_data = {"state": "closed", "state_reason": "not_planned"}
    response = requests.patch(f"{base_url}/repos/{repo_owner}/{repo_name}/issues/{issue_number}", json=update_data,
                              headers=headers)
    assert response.status_code == 200
    print("\nIssue updated successfully")


# Test scenario 7
def test_verify_issue_not_in_list_after_closure():
    issues = get_all_open_issues()
    assert len(issues) == initial_issue_count


# Scenario 6 helper function to get the issue number by title
def get_issue_number_by_title(title):
    response = requests.get(f"{base_url}/repos/{repo_owner}/{repo_name}/issues", headers=headers)
    assert response.status_code == 200
    issues = response.json()
    for issue in issues:
        if issue["title"] == title:
            return issue["number"]


# Helper function
def get_all_open_issues(label=''):
    issues = []
    page = 1

    while True:
        if label == '':
            response = requests.get(f"{base_url}/repos/{repo_owner}/{repo_name}/issues", params={"page": page},
                                    headers=headers)
        else:
            response = requests.get(f"{base_url}/repos/{repo_owner}/{repo_name}/issues?labels={label}",
                                    params={"page": page},
                                    headers=headers)
        if response.status_code == 200:
            current_page_issues = response.json()
            if not current_page_issues:
                break  # No more issues, exit the loop
            issues.extend(current_page_issues)
            page += 1
        else:
            print(f"\nFailed to fetch issues. Status Code: {response.status_code}")
            break
    if label == '':
        print(f"\nNumber of open issues: {len(issues)}")
    else:
        print(f"\nNumber of open issues with label '{label}': {len(issues)}")
    return issues
