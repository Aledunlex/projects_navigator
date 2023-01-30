from versioning.Gitlab import Gitlab


class GitlabEtu(Gitlab):
    def __init__(self, username, private_key, url):
        super(GitlabEtu, self).__init__(username, private_key, url)

    def get_projects(self):
        # Implement logic to retrieve projects from GitlabEtu
        return ["project4", "project5", "project6"]