import PySide2.QtWidgets
from PySide2.QtWidgets import QWidget, QGridLayout, QLabel, QMainWindow, QLineEdit, QTextBrowser
from PySide2.QtCore import Qt
from Lang.Steam.LangString import LangString
from Qt.constants import FONTNAMES
from Account.AccountManager import AccountManager
from Qt.tool import QFont_recreate as QFont, calc_font_size


class PageStoryIntro:
    def __init__(self, app_window: QMainWindow, acc: AccountManager, genre: str, callback):
        self.app_window = app_window
        self.acc = acc
        self.genre = genre
        self.callback = callback

    def load(self):
        window = QWidget()

        layout = QGridLayout()
        layout.setSpacing(5)
        window.setLayout(layout)

        lang = LangString().mapping
        font = FONTNAMES.get_font(lang.get_language_code())

        lb_title = QLabel(lang.get("Summer_21_Overview_Title"))
        lb_title.setAlignment(Qt.AlignCenter)
        lb_title.setFont(QFont(font, 30))
        layout.addWidget(lb_title, 0, 0, 1, 12)

        storyinfo = lang.get_storyinfo(self.genre)

        line_title = QLineEdit(storyinfo.Title)
        line_title.setAlignment(Qt.AlignCenter)
        line_title.setFont(QFont(font, 15))
        line_title.setReadOnly(True)
        layout.addWidget(line_title, 1, 0, 1, 12)

        story_content = storyinfo.Intro.Content
        story_content = story_content.split("\n")
        story_content = [i.strip() for i in story_content]
        story_content = "\n".join(story_content)
        browser_story = QTextBrowser()
        browser_story.setFont(QFont(font, 18))
        browser_story.setText(story_content)
        layout.addWidget(browser_story, 2, 0, 1, 12)

        def createQPushButtonWithWordWrap(text, fontsize=None):
            from Qt.page.tool import createQPushButtonWithWordWrap
            return createQPushButtonWithWordWrap(text, label_width=self.app_window.size().width() - 40,
                                                 fontsize=fontsize, fontname=font)

        btn_choice1 = createQPushButtonWithWordWrap(storyinfo.Choice1.Content, fontsize=17)
        btn_choice1.clicked.connect(lambda: self.goto_outcome(1))
        btn_choice1.setFixedHeight(calc_font_size(70) + 15)
        layout.addWidget(btn_choice1, 3, 0, 1, 12)

        btn_choice2 = createQPushButtonWithWordWrap(storyinfo.Choice2.Content, fontsize=17)
        btn_choice2.clicked.connect(lambda: self.goto_outcome(2))
        btn_choice2.setFixedHeight(calc_font_size(70) + 15)
        layout.addWidget(btn_choice2, 4, 0, 1, 12)

        choice = self.acc.answer.get_choice(self.genre)
        if choice == 1:
            btn_choice2.setDisabled(True)
        elif choice == 2:
            btn_choice1.setDisabled(True)

        btn_back = PySide2.QtWidgets.QPushButton("<")
        btn_back.setFont(QFont(font, 18))
        btn_back.clicked.connect(lambda: self.goto_back())
        layout.addWidget(btn_back, 5, 0, 1, 2)

        line_category = QLineEdit(storyinfo.Genre)
        line_category.setAlignment(Qt.AlignCenter)
        line_category.setFont(QFont(font, 14))
        line_category.setReadOnly(True)
        layout.addWidget(line_category, 5, 2, 1, 8)

        line_page_number = QLineEdit(storyinfo.Intro.Page)
        line_page_number.setFont(QFont(font, 18))
        line_page_number.setAlignment(Qt.AlignCenter)
        line_page_number.setFixedWidth(self.app_window.size().width() / 12 * 2)
        layout.addWidget(line_page_number, 5, 10, 1, 2)

        self.app_window.setCentralWidget(window)

    def goto_outcome(self, number: int):
        self.callback(self.genre, number)

    def goto_back(self):
        self.callback("StorySelection")
