from versioning.VersionControlSystem import VersionControlSystem


class GitlabEtu(VersionControlSystem):
    def __init__(self):
        username = ""
        url = ""
        token_path = ""
        super(GitlabEtu, self).__init__(username, token_path, url)

    def get_projects(self):
        return []
