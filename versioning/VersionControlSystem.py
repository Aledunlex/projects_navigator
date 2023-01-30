from abc import ABC, abstractmethod


class VersionControlSystem(ABC):
    def __init__(self, username, private_key, url):
        self.username = username
        self.private_key = private_key
        self.url = url

    @abstractmethod
    def get_projects(self):
        pass


@staticmethod
def get_all_projects(version_control_systems):
    all_projects = []
    for vcs in version_control_systems:
        all_projects += vcs.get_projects()
    return all_projects
