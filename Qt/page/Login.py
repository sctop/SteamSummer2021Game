import PySide2.QtWidgets
from PySide2.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QMainWindow, QComboBox
from PySide2.QtCore import Qt
from Lang.Interface.constants import TEXT_INIT_LANGUAGE, TEXT_INIT_USERNAME, TEXT_INIT_CONTINUE
from Lang.Steam.constants import LANGPACK_NAME
from Qt.tool import QFont_recreate as QFont


class LoginPage:
    def __init__(self, app: QMainWindow, continue_callback):
        self.app = app
        self.continue_callback = continue_callback

    def load(self):
        window = QWidget()
        size_width, size_height = self.app.size().width(), self.app.size().height()

        layout = QGridLayout()
        layout.setSpacing(5)
        window.setLayout(layout)

        temp_top_label = QLabel("\n" * 500)
        temp_top_label.setFixedSize(100, size_height / 9)
        layout.addWidget(temp_top_label, 0, 0, 1, 10)

        lb_name = QLabel(TEXT_INIT_USERNAME)
        lb_name.setFixedSize(size_width, size_height / 9)
        lb_name.setAlignment(Qt.AlignCenter)
        lb_name.setFont(QFont("Noto Sans", 30))
        layout.addWidget(lb_name, 1, 0, 1, 10)

        self.line_name = QLineEdit()
        self.line_name.setAlignment(Qt.AlignCenter)
        self.line_name.setFont(QFont("Noto Sans", 20))
        self.line_name.setPlaceholderText("Enter your name")
        self.line_name.setMaxLength(14)
        layout.addWidget(self.line_name, 2, 2, 1, 6)

        temp_middle_label = QLabel("\n" * 5)
        temp_middle_label.setFixedSize(size_width, size_height / 9 / 2)
        layout.addWidget(temp_middle_label, 3, 0, 1, 10)

        lb_language = QLabel(TEXT_INIT_LANGUAGE)
        lb_language.setAlignment(Qt.AlignCenter)
        lb_language.setFont(QFont("Noto Sans", 30))
        layout.addWidget(lb_language, 4, 0, 1, 10)

        self.combo_language = QComboBox()
        temp_all_language = sorted(LANGPACK_NAME.keys(), key=str.lower)
        self.combo_language.addItems(temp_all_language)
        from Account.SettingManager import SettingManager
        if SettingManager().defaultLanguage == "":
            self.combo_language.setCurrentText("English")
        elif SettingManager().defaultLanguage in LANGPACK_NAME.keys():
            self.combo_language.setCurrentText(SettingManager().defaultLanguage)
        else:
            self.combo_language.setCurrentText("English")
        self.combo_language.setFixedSize(size_width / 10 * 6, size_height / 9 / 2)
        self.combo_language.setFont(QFont("Noto Sans", 20))
        layout.addWidget(self.combo_language, 5, 2, 1, 6)

        temp_mid2_label = QLabel("\n" * 10)
        temp_mid2_label.setFixedSize(size_width, size_height / 9 * 2.5)
        layout.addWidget(temp_mid2_label, 6, 0, 1, 10)

        self.button_continue = PySide2.QtWidgets.QPushButton(TEXT_INIT_CONTINUE)
        self.button_continue.setFont(QFont("Noto Sans", 20))
        self.button_continue.clicked.connect(lambda: self.continue_check())
        layout.addWidget(self.button_continue, 7, 2, 1, 6)

        temp_bottom_label = QLabel("\n" * 50)
        temp_bottom_label.setFixedSize(size_width, size_height / 9)
        layout.addWidget(temp_bottom_label, 8, 0, 1, 10)

        self.app.setCentralWidget(window)

    def continue_check(self):
        if len(self.line_name.text()) >= 3:
            self.continue_callback(self.line_name.text(), self.combo_language.currentText())
