import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QPushButton

from connection.VpnAuth import connect_vpn
from ui.BaseButton import BaseButton
from ui.BaseWindow import BaseWindow
from ui.ProjectWindow import ProjectWindow
from versioning.Github import Github
from versioning.Gitlab import Gitlab
from versioning.GitlabEtu import GitlabEtu
from versioning.VersionControlSystem import VersionControlSystem


class MainWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        # self.check_vpn_enabled()
        self.current_window = None
        self.project_buttons = None
        self.__init_ui()

    def __init_ui(self):
        self.setWindowTitle("Git Project Interface")

        projects = self.get_all_projects()

        self.project_buttons = []
        for project in projects:
            button = BaseButton(project["name"], f"{project['name']}_button", "#4CAF50")
            project = project['name']
            button.clicked.connect(lambda checked, p=project: self.open_project_window(p))
            self.layout.addWidget(button)

        self.showMaximized()

    @pyqtSlot()
    def open_project_window(self, project):
        print(f"Opening {project} window")
        self.current_window = ProjectWindow(project, self)
        self.hide()

    @staticmethod
    def check_vpn_enabled():
        # connect_vpn() todo: fix it
        pass

    @staticmethod
    def get_all_projects():
        gitlab = Gitlab()
        # gitlab_etu = GitlabEtu()
        # github = Github()
        return VersionControlSystem.merge_projects([gitlab])  # , gitlab_etu, github])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
