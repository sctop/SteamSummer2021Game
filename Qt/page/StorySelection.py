import PySide2.QtWidgets
from PySide2.QtWidgets import QWidget, QGridLayout, QLabel, QMainWindow, QLineEdit
from PySide2.QtCore import Qt
from Lang.Steam.LangString import LangString
from Qt.constants import FONTNAMES
from Account.AccountManager import AccountManager
from Qt.tool import QFont_recreate as QFont, calc_font_size


class StorySelection:
    def __init__(self, window: QMainWindow, acc: AccountManager, callback):
        self.app_window = window
        self.acc = acc
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
        layout.addWidget(lb_title, 0, 0, 1, 10)

        temp = QLabel("<hr />")
        temp.setFixedHeight(10)
        layout.addWidget(temp, 1, 0, 1, 10)

        lb_continue_story = QLabel(lang.get("SummerSale2021_CallToAction_SecondLine"))
        lb_continue_story.setAlignment(Qt.AlignLeft)
        lb_continue_story.setFont(QFont(font, 20))
        layout.addWidget(lb_continue_story, 2, 0, 1, 10)

        size_width = self.app_window.size().width()
        """
        all_genres = list(sorted(ALL_GENRES, key=str.lower))

        counter_ = 0
        for i in all_genres:
            storyinfo = lang.ALL_STORIES[i]
            genre, name = storyinfo.Genre, storyinfo.Title
            button = createQPushButtonWithWordWrap(f'{genre}')
            button.setFont(QFont(font, 20))
            button.genre = deepcopy(i)
            button.clicked.connect(lambda: self.enter_story(deepcopy(i)))
            button.setText(button.genre)
            button.setFixedSize(size_width / 2, calc_font_size(90))
            if counter_ % 2 == 1:
                layout.addWidget(button, counter_ // 2 + 3, 5, 1, 5)
            else:
                layout.addWidget(button, counter_ // 2 + 3, 0, 1, 5)
            del storyinfo, genre, name, button

            counter_ += 1
        """

        def createQPushButtonWithWordWrap(text, fontsize=None):
            from Qt.page.tool import createQPushButtonWithWordWrap
            return createQPushButtonWithWordWrap(text, fontsize=fontsize, fontname=font)

        btn_story_action = createQPushButtonWithWordWrap(lang.ALL_STORIES['Action'].Genre, fontsize=20)
        btn_story_action.clicked.connect(lambda: self.enter_story('Action'))
        btn_story_action.setFixedSize(size_width / 2, calc_font_size(90))
        layout.addWidget(btn_story_action, 3, 0, 1, 5)

        btn_story_adventure = createQPushButtonWithWordWrap(lang.ALL_STORIES['Adventure'].Genre, fontsize=20)
        btn_story_adventure.clicked.connect(lambda: self.enter_story('Adventure'))
        btn_story_adventure.setFixedSize(size_width / 2, calc_font_size(90))
        layout.addWidget(btn_story_adventure, 3, 5, 1, 5)

        btn_story_anime = createQPushButtonWithWordWrap(lang.ALL_STORIES['Anime'].Genre, fontsize=20)
        btn_story_anime.clicked.connect(lambda: self.enter_story('Anime'))
        btn_story_anime.setFixedSize(size_width / 2, calc_font_size(90))
        layout.addWidget(btn_story_anime, 4, 0, 1, 5)

        btn_story_horror = createQPushButtonWithWordWrap(lang.ALL_STORIES['Horror'].Genre, fontsize=20)
        btn_story_horror.clicked.connect(lambda: self.enter_story('Horror'))
        btn_story_horror.setFixedSize(size_width / 2, calc_font_size(90))
        layout.addWidget(btn_story_horror, 4, 5, 1, 5)

        btn_story_mystery = createQPushButtonWithWordWrap(lang.ALL_STORIES['Mystery'].Genre, fontsize=20)
        btn_story_mystery.clicked.connect(lambda: self.enter_story('Mystery'))
        btn_story_mystery.setFixedSize(size_width / 2, calc_font_size(90))
        layout.addWidget(btn_story_mystery, 5, 0, 1, 5)

        btn_story_open = createQPushButtonWithWordWrap(lang.ALL_STORIES['Open'].Genre, fontsize=20)
        btn_story_open.clicked.connect(lambda: self.enter_story('Open'))
        btn_story_open.setFixedSize(size_width / 2, calc_font_size(90))
        layout.addWidget(btn_story_open, 5, 5, 1, 5)

        btn_story_roguelike = createQPushButtonWithWordWrap(lang.ALL_STORIES['Roguelike'].Genre, fontsize=20)
        btn_story_roguelike.clicked.connect(lambda: self.enter_story('Roguelike'))
        btn_story_roguelike.setFixedSize(size_width / 2, calc_font_size(90))
        layout.addWidget(btn_story_roguelike, 6, 0, 1, 5)

        btn_story_rpg = createQPushButtonWithWordWrap(lang.ALL_STORIES['RPG'].Genre, fontsize=20)
        btn_story_rpg.clicked.connect(lambda: self.enter_story('RPG'))
        btn_story_rpg.setFixedSize(size_width / 2, calc_font_size(90))
        layout.addWidget(btn_story_rpg, 6, 5, 1, 5)

        btn_story_scifi = createQPushButtonWithWordWrap(lang.ALL_STORIES['SciFi'].Genre, fontsize=20)
        btn_story_scifi.clicked.connect(lambda: self.enter_story('SciFi'))
        btn_story_scifi.setFixedSize(size_width / 2, calc_font_size(90))
        layout.addWidget(btn_story_scifi, 7, 0, 1, 5)

        btn_story_sim = createQPushButtonWithWordWrap(lang.ALL_STORIES['Sim'].Genre, fontsize=20)
        btn_story_sim.clicked.connect(lambda: self.enter_story('Sim'))
        btn_story_sim.setFixedSize(size_width / 2, calc_font_size(90))
        layout.addWidget(btn_story_sim, 7, 5, 1, 5)

        btn_story_space = createQPushButtonWithWordWrap(lang.ALL_STORIES['Space'].Genre, fontsize=20)
        btn_story_space.clicked.connect(lambda: self.enter_story('Space'))
        btn_story_space.setFixedSize(size_width / 2, calc_font_size(90))
        layout.addWidget(btn_story_space, 8, 0, 1, 5)

        btn_story_sports = createQPushButtonWithWordWrap(lang.ALL_STORIES['Sports'].Genre, fontsize=20)
        btn_story_sports.clicked.connect(lambda: self.enter_story('Sports'))
        btn_story_sports.setFixedSize(size_width / 2, calc_font_size(90))
        layout.addWidget(btn_story_sports, 8, 5, 1, 5)

        btn_story_strategy = createQPushButtonWithWordWrap(lang.ALL_STORIES['Strategy'].Genre, fontsize=20)
        btn_story_strategy.clicked.connect(lambda: self.enter_story('Strategy'))
        btn_story_strategy.setFixedSize(size_width / 2, calc_font_size(90))
        layout.addWidget(btn_story_strategy, 9, 0, 1, 5)

        btn_story_survival = createQPushButtonWithWordWrap(lang.ALL_STORIES['Survival'].Genre, fontsize=20)
        btn_story_survival.clicked.connect(lambda: self.enter_story('Survival'))
        btn_story_survival.setFixedSize(size_width / 2, calc_font_size(90))
        layout.addWidget(btn_story_survival, 9, 5, 1, 5)

        layout.addWidget(QLabel("\n" * 50), 10, 0, 1, 10)

        btn_back = PySide2.QtWidgets.QPushButton("<")
        btn_back.setFont(QFont(font, 14))
        btn_back.clicked.connect(lambda: self.goto_mainmenu())
        layout.addWidget(btn_back, 11, 0, 1, 2)

        if self.acc.answer.is_finished:
            line_finished = QLineEdit(lang.get("Summer21_Badge_Unlocked_Title"))
            line_finished.setReadOnly(True)
            line_finished.setAlignment(Qt.AlignCenter)
            line_finished.setFont(QFont(font, 14))
            layout.addWidget(line_finished, 11, 2, 1, 8)

        self.app_window.setCentralWidget(window)

    def enter_story(self, genre: str):
        self.callback("Story", genre)

    def goto_mainmenu(self): self.callback("Mainmenu")
