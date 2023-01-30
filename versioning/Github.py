from versioning.VersionControlSystem import VersionControlSystem


class Github(VersionControlSystem):
    def __init__(self, username, private_key, url):
        super(Github, self).__init__(username, private_key, url)

    def get_projects(self):
        # Implement logic to retrieve projects from Github
        return ["project7", "project8", "project9"]
    