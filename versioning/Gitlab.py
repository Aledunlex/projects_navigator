from versioning.VersionControlSystem import VersionControlSystem


class Gitlab(VersionControlSystem):
    def __init__(self, username, private_key, url):
        super(Gitlab, self).__init__(username, private_key, url)

    def get_projects(self):
        return ["project1", "project2", "project3"]
