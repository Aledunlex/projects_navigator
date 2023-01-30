from PyQt5.QtWidgets import QPushButton


class BaseButton(QPushButton):
    def __init__(self, text, name=None, color=None):
        super().__init__(text)
        if name:
            self.setObjectName(name)
        else:
            name = self.__str__()
            self.setObjectName(name)
        if color:
            self.setStyleSheet(
                f"""
                    #{name} {{
                    background-color: {color};
                    color: white;
                    padding: 15px 32px;
                    text-align: center;
                    display: inline-block;
                    font-size: 16px;
                    border-radius: 5px;
                    }}
                    #{name}:hover {{
                    background-color: #3e8e41;
                    }}
                """
            )
        else:
            self.setStyleSheet(
                f"""
                    #{name} {{
                        background-color: "grey";
                        color: white;
                        padding: 15px 32px;
                        text-align: center;
                        display: inline-block;
                        font-size: 16px;
                        border-radius: 5px;
                    }}
                    #{name}:hover {{
                        background-color: #3e8e41;
                    }}
                """
            )
