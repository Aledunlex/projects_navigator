from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QDesktopWidget

from ui.BaseButton import BaseButton


class BaseWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.config = self.load_config()

        self.layout = QVBoxLayout()

        if self.parent:
            self.previous_button = BaseButton("Previous", "previousbutton")
        else:
            self.previous_button = BaseButton("Close", "previousbutton", "red")
        self.previous_button.clicked.connect(self.on_previous_clicked)
        self.layout.addWidget(self.previous_button)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    def load_config(self):
        return {
            "config_json": "../config.json",
            "font": "Arial",
            "font_size": 10
        }

    def on_previous_clicked(self):
        if self.parent:
            self.parent.show()
        self.close()
