import requests
from django.conf import settings

BASE_URL = "https://api.github.com"

def get_user_repos(username):
    url = f"{BASE_URL}/users/{username}/repos"

    headers = {
        "Authorization": f"Bearer {settings.GITHUB_TOKEN}"
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return {
                "error": response.json(),
                "status": response.status_code
                
            }
            

    except Exception as e:
        return {"error": str(e)}
    


def get_repo_issues(owner, repo):
    url = f"{BASE_URL}/repos/{owner}/{repo}/issues"

    headers = {
        "Authorization": f"Bearer {settings.GITHUB_TOKEN}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        issues = response.json()

        return [
            {
                "title": issue["title"],
                "state": issue["state"],
                "url": issue["html_url"]
            }
            for issue in issues
        ]

    return {"error": response.json()}


def create_issue(owner, repo, title, body=None):
    url = f"{BASE_URL}/repos/{owner}/{repo}/issues"

    headers = {
        "Authorization": f"Bearer {settings.GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    payload = {
        "title": title,
        "body": body
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 201:
        data = response.json()
        return {
            "message": "Issue created successfully",
            "issue_url": data["html_url"]
        }

    return {
        "error": response.json(),
        "status": response.status_code
    }