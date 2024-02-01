# GitHub API Test Automation

This repository contains a test automation script to interact with a GitHub repository via the REST API. The script covers various scenarios, such as retrieving issues, creating new issues, updating issues, and verifying the API responses.

## How to Execute the Automation Script

1. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

2. **Verify and Update the Authorization Token:**

   - Open `github_api_tests.py` and ensure the `token` variable contains a valid GitHub personal access token.
   - The token should have the necessary permissions to interact with the specified repository.

3. **Open `github_api_tests.py` and update the following global variables:**

    - `repo_owner`: GitHub repository owner.
    - `repo_name`: GitHub repository name.
    - `token`: Your GitHub personal access token.

4. **Execute the script using PyTest:**

    ```bash
    pytest github_api_tests.py
    ```

## Test Scenarios

### 1. `test_get_all_open_issues`

- Fetches a list of all open issues from the specified GitHub repository.
- Prints the number of returned issues.

### 2. `test_get_issues_with_label`

- Fetches a list of issues with the label "practice1"  or any other label of your choice from the specified GitHub repository.
- Prints the number of returned issues.

### 3. `test_create_new_issue`

- Creates a new issue with the following details:
  - Title: `<Your name>'s issue`
  - Body: `This issue was created via REST API from <Python/Java/C#> by <your name>`
  - Label: `practice1`
  - Assignee: `topq-practice`

### 4. `test_verify_new_issue_in_list`

- Verifies the response status code is 201 (created) after creating a new issue.
- Prints the new issue number contained in the response body.
- Gets a list of all issues and verifies:
  - Total number of returned issues equals the initial number of issues + 1.
  - The first issue listed in the response JSON is the newly created issue with the correct title.

### 6. `test_update_issue`

- Updates the state of the issue created in step 3 to "closed" with a state reason of "not_planned."
- Verifies the response status code is 200 (OK).

### 7. `test_verify_issue_not_in_list_after_closure`

- Gets a list of all issues and verifies the total number of issues is again equal to the initial number of issues.
- This is because the issue created in step 3 is now closed, and it shouldn't be in the returned list of issues.
