import json
import os
import subprocess
import sys

from PyQt5.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QFileDialog, QApplication

from ui.BaseWindow import BaseWindow


class ProjectWindow(BaseWindow):
    def __init__(self, project, parent=None):
        super().__init__(parent)
        self.project = project
        self.directory = self.load_directory()
        self.__init_ui()

    def __init_ui(self):
        self.setWindowTitle(f"Project: {self.project}")

        if self.directory:
            directory_label = QLabel(f"Directory: {self.directory}")
            directory_button = QPushButton("Open directory")
            directory_button.clicked.connect(self.open_directory)
        else:
            directory_label = QLabel("Directory: Not set")
            directory_button = QPushButton("Set directory")
            directory_button.clicked.connect(self.set_directory)

        self.layout.addWidget(directory_label)
        self.layout.addWidget(directory_button)

        self.show()

    def set_directory(self):
        self.directory = QFileDialog.getExistingDirectory(self, "Set directory")
        if self.directory:
            project_to_direct = {self.project: self.directory}
            self.save_directory()
        else:
            raise NotADirectoryError

    def save_directory(self):
        project_to_direct = {self.project: self.directory}
        with open(self.config["config_json"], 'w') as file:
            json.dump(project_to_direct, file, indent=2)

    def load_directory(self):
        try:
            with open(self.config["config_json"], 'r') as file:
                return json.load(file).get(self.project)
        except FileNotFoundError:
            return None
        except KeyError:
            return None

    def open_directory(self):
        FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
        path = os.path.normpath(self.directory)
        if os.path.isdir(path):
            subprocess.run([FILEBROWSER_PATH, path])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = ProjectWindow('un projet')
    sys.exit(app.exec_())
