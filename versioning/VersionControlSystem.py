from abc import ABC, abstractmethod


class VersionControlSystem(ABC):
    def __init__(self, username, token_path, url):
        self.username = username
        self.personal_token = self.read_token(token_path)
        self.url = url

    @abstractmethod
    def get_projects(self):
        pass

    @staticmethod
    def read_token(token_path):
        with open(token_path, "r") as file:
            private_token = file.read()
        return private_token.replace("\n", "")

    @staticmethod
    def merge_projects(version_control_systems):
        all_projects = []
        for vcs in version_control_systems:
            all_projects += vcs.get_projects()
        return all_projects
