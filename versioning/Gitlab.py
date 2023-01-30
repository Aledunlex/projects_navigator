from pathlib import Path

import requests

from versioning.VersionControlSystem import VersionControlSystem


class Gitlab(VersionControlSystem):
    def __init__(self):
        username = "5041"
        url = "https://gitlab.univ-lille.fr/api/v4"
        GITLAB_PRIVATE_KEY_PATH = Path("C:/Tools/.lab_pers_tok")
        super(Gitlab, self).__init__(username, GITLAB_PRIVATE_KEY_PATH, url)

    def get_projects(self):
        GITLAB_API_URL = f"{self.url}/users/{self.username}/starred_projects"

        headers = {
            "accept": "application/json",
            "Private-Token": self.personal_token
        }

        response = requests.get(GITLAB_API_URL, headers=headers)
        projects = response.json()

        return projects
