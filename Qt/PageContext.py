from PySide2.QtWidgets import QMainWindow
from Account.AccountManager import AccountManager
from Qt.page.Login import LoginPage
from Qt.page.NewUserWelcome import NewUserWelcome
from Qt.page.MainPage import MainPage
from Qt.page.StorySelection import StorySelection
from Qt.page.PageStoryIntro import PageStoryIntro
from Qt.page.PageStoryOutcome import PageStoryOutcome
from Qt.page.PreIntroBrand import PreIntroBrand
from Qt.page.PageViewBrand import PageViewBrand
from Qt.page.Settings import PageSetting


class PageContext:
    AccountManager = None
    next_function = None

    def __init__(self, app: QMainWindow):
        self.app = app
        self.next_function = self.login

    def login(self):
        page = LoginPage(self.app, self.login_callback)
        page.load()

    def login_callback(self, username, language_selection):
        self.AccountManager = AccountManager(username)

        from Lang.Steam.LangString import LangString
        LangString(language_selection)

        if self.AccountManager.save.is_new_user:
            self.new_user_welcome()
        else:
            self.main_menu()

    def new_user_welcome(self):
        page = NewUserWelcome(self.app, self.new_user_welcome_callback)
        page.load()

    def new_user_welcome_callback(self):
        self.main_menu()

    def main_menu(self):
        page = MainPage(self.app, self.AccountManager, self.main_menu_callback)
        page.load()

    def main_menu_callback(self, value):
        mapping = {
            "StorySelection": self.story_selection,
            "ViewBrand": self.view_brand,
            "Setting": self.setting
        }
        mapping[value]()

    def story_selection(self):
        page = StorySelection(self.app, self.AccountManager, self.story_selection_callback)
        page.load()

    def story_selection_callback(self, *values):
        if values[0] == "Mainmenu":
            self.main_menu()
        elif values[0] == "Story":
            self.story_intro(values[1])

    def story_intro(self, genre: str):
        page = PageStoryIntro(self.app, self.AccountManager, genre, self.story_intro_callback)
        page.load()

    def story_intro_callback(self, *values):
        if values[0] == "StorySelection":
            self.story_selection()
        else:
            self.story_outcome(values[0], values[1])

    def story_outcome(self, genre: str, choice: int):
        self.AccountManager.answer.update_choice(genre, choice)
        page = PageStoryOutcome(self.app, genre, choice, self.story_outcome_callback)
        page.load()

    def story_outcome_callback(self, genre):
        self.story_intro(genre)

    def view_brand(self):
        if not self.AccountManager.save.brand_has_seen:
            self.pre_intro_brand()
        else:
            self.show_brand()

    def pre_intro_brand(self):
        page = PreIntroBrand(self.app, self.show_brand)
        page.load()

    def show_brand(self):
        self.AccountManager.save.change_brand_has_seen()
        page = PageViewBrand(self.app, self.AccountManager, self.main_menu)
        page.load()

    def setting(self):
        page = PageSetting(self.app, self.AccountManager, self.main_menu)
        page.load()
