from versioning.VersionControlSystem import VersionControlSystem


class Github(VersionControlSystem):
    def __init__(self):
        username = ""
        url = ""
        token_path = ""
        super(Github, self).__init__(username, token_path, url)

    def get_projects(self):
        return []
    