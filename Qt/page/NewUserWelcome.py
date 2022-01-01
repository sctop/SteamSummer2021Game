import PySide2.QtWidgets
from PySide2.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QMainWindow, QTextBrowser
from PySide2.QtCore import Qt
from Lang.Steam.LangString import LangString
from Qt.constants import FONTNAMES
from Qt.tool import QFont_recreate as QFont


class NewUserWelcome:
    def __init__(self, app: QMainWindow, continue_callback):
        self.app = app
        self.continue_callback = continue_callback

    def load(self):
        window = QWidget()

        layout = QGridLayout()
        layout.setSpacing(5)
        window.setLayout(layout)

        lang = LangString()
        font = FONTNAMES.get_font(lang.get_language_code())

        lb_its_time = QLabel(lang.get("Summer_21_Overview_Title_Prefix"))
        lb_its_time.setAlignment(Qt.AlignCenter)
        lb_its_time.setFont(QFont(font, 30))
        layout.addWidget(lb_its_time, 0, 0, 1, 10)

        lb_title = QLabel(lang.get("Summer_21_Overview_Title"))
        lb_title.setAlignment(Qt.AlignCenter)
        lb_title.setWordWrap(True)
        lb_title.setFont(QFont(font, 40))
        layout.addWidget(lb_title, 1, 0, 1, 10)

        browser_description = QTextBrowser()
        browser_description.setFont(QFont(font, 18))
        browser_description.insertHtml("<p>" + lang.mapping.story_overview("Description1") + "</p>\n" + \
                                       "<p>" + lang.mapping.story_overview("Description3") + "</p>\n" + \
                                       "<p>" + lang.mapping.story_overview("Description4") + "</p>\n<hr />\n" + \
                                       "<p><b>" + lang.get("Summer_21_Story_Decide_Notice") + "</b></p>")
        layout.addWidget(browser_description, 2, 0, 1, 10)

        line_description2 = QLineEdit(lang.mapping.story_overview("Description2"))
        line_description2.setFont(QFont(font, 18))
        line_description2.setAlignment(Qt.AlignCenter)
        line_description2.setReadOnly(True)
        layout.addWidget(line_description2, 3, 0, 1, 10)

        button_login = PySide2.QtWidgets.QPushButton(lang.get("SummerSale2021_CallToAction_NeedToSignIn"))
        button_login.setFont(QFont(font, 18))
        button_login.clicked.connect(lambda: self.continue_callback())
        layout.addWidget(button_login, 4, 3, 1, 4)

        self.app.setCentralWidget(window)
