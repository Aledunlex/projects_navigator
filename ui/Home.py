import sys
from pathlib import Path

import requests
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

from connection.VpnAuth import connect_vpn
from ui.BaseWindow import BaseWindow
from ui.ProjectWindow import ProjectWindow


class MainWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        # self.check_vpn_enabled()
        self.current_window = None
        self.project_buttons = None
        self.__init_ui()

    def __init_ui(self):
        self.setWindowTitle("Git Project Interface")

        projects = self.get_projects_from_gitlab()

        self.project_buttons = []
        for project in projects:
            button = QPushButton(project["name"])
            project = project['name']
            button.clicked.connect(lambda checked, p=project: self.open_project_window(p))
            self.project_buttons.append(button)

        for button in self.project_buttons:
            self.layout.addWidget(button)

        self.show()

    @pyqtSlot()
    def open_project_window(self, project):
        print(f"Opening {project} window")
        self.current_window = ProjectWindow(project, self)
        self.close()

    def check_vpn_enabled(self):
        # connect_vpn() todo: fix it
        pass

    def get_projects_from_gitlab(self):
        GITLAB_API_URL = "https://gitlab.univ-lille.fr/api/v4/users/5041/starred_projects"
        GITLAB_PRIVATE_KEY_PATH = Path("C:/Tools/.lab_pers_tok")

        with open(GITLAB_PRIVATE_KEY_PATH, "r") as file:
            private_token = file.read()

        private_token = private_token.replace("\n", "")
        headers = {
            "accept": "application/json",
            "Private-Token": private_token
        }

        response = requests.get(GITLAB_API_URL, headers=headers)
        projects = response.json()

        return projects


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
