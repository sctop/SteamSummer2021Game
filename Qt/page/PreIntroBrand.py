import PySide2.QtWidgets
from PySide2.QtWidgets import QWidget, QGridLayout, QLabel, QMainWindow, QLineEdit, QTextBrowser, QFileDialog
from PySide2.QtCore import Qt
from Lang.Steam.LangString import LangString
from Qt.constants import FONTNAMES
from Qt.tool import QFont_recreate as QFont


class PreIntroBrand:
    def __init__(self, window: QMainWindow, callback):
        self.app_window = window
        self.callback = callback

    def load(self):
        window = QWidget()

        layout = QGridLayout()
        layout.setSpacing(5)
        window.setLayout(layout)

        lang = LangString()
        font = FONTNAMES.get_font(lang.get_language_code())
        size_width, size_height = self.app_window.size().width(), self.app_window.size().height()

        lb_title = QLabel(lang.get("Summer21_Badge_Unlocked_Title"))
        lb_title.setAlignment(Qt.AlignCenter)
        lb_title.setFont(QFont(font, 30))
        lb_title.setWordWrap(True)
        layout.addWidget(lb_title, 0, 0, 1, 10)

        browser_description = QTextBrowser()
        browser_description.setFont(QFont(font, 15))
        browser_description.insertHtml("<center><h1>" + lang.get("Summer21_Badge_Congrats1") + \
                                       lang.get("Summer21_Badge_Unlocked_Title") + "</h1></center>" + \
                                       "<hr /><p>" + lang.get("Summer21_Badge_Unlocked_Description") + "</p>")
        layout.addWidget(browser_description, 2, 0, 1, 10)

        btn_continue = PySide2.QtWidgets.QPushButton()
        btn_continue.setFont(QFont(font, 20))
        btn_continue.setText(lang.get("Summer_21_Overview_Title"))
        btn_continue.clicked.connect(lambda: self.callback())
        layout.addWidget(btn_continue, 4, 2, 1, 6)

        self.app_window.setCentralWidget(window)
