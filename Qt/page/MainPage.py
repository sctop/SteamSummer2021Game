import PySide2.QtWidgets
import sys
import webbrowser
from PySide2.QtWidgets import QWidget, QGridLayout, QLabel, QMainWindow, QDialog, QTextBrowser
from PySide2.QtCore import Qt
from Lang.Steam.LangString import LangString
from Qt.constants import FONTNAMES
from Account.AccountManager import AccountManager
from Lang.Interface.InterfaceLangString import InterfaceLangString
from Qt.tool import QFont_recreate as QFont, calc_font_size
from Lang.Interface.constants import *


class MainPage:
    def __init__(self, window: QMainWindow, acc: AccountManager, callback):
        self.app_window = window
        self.acc = acc
        self.callback = callback

    def load(self):
        window = QWidget()

        layout = QGridLayout()
        layout.setSpacing(5)
        window.setLayout(layout)

        lang = LangString()
        interface_lang = InterfaceLangString()
        font = FONTNAMES.get_font(lang.get_language_code())
        print(font)

        lb_title = QLabel()
        lb_title.setText(lang.get("Summer_21_Overview_Title"))
        lb_title.setFont(QFont(font, 30))
        lb_title.setAlignment(Qt.AlignCenter)
        layout.addWidget(lb_title, 0, 0, 1, 10)

        lb_login_as = QLabel(interface_lang.get("Text_LoginAs").format(username=self.acc.username))
        lb_login_as.setAlignment(Qt.AlignCenter)
        lb_login_as.setFont(QFont(font, 15))
        layout.addWidget(lb_login_as, 1, 0, 1, 10)

        lb_temp = QLabel("<hr />")
        lb_temp.setFixedHeight(calc_font_size(10))
        layout.addWidget(lb_temp, 2, 0, 1, 10)

        lb_whats_next = QLabel(lang.get("Summer_21_Story_Next"))
        lb_whats_next.setAlignment(Qt.AlignLeft)
        lb_whats_next.setFont(QFont(font, 25))
        layout.addWidget(lb_whats_next, 3, 0, 1, 10)

        btn_continue_story = PySide2.QtWidgets.QPushButton()
        btn_continue_story.setFont(QFont(font, 18))
        btn_continue_story.setText("📖 " + lang.get("SummerSale2021_CallToAction_SecondLine"))
        btn_continue_story.clicked.connect(lambda: self.goto_story_selection())
        layout.addWidget(btn_continue_story, 4, 0, 1, 10)

        btn_view_brand = PySide2.QtWidgets.QPushButton()
        btn_view_brand.setFont(QFont(font, 18))
        btn_view_brand.setText("🏅 " + lang.get("Summer21_Badge_Unlocked_Title"))
        btn_view_brand.clicked.connect(lambda: self.goto_view_brand())
        layout.addWidget(btn_view_brand, 5, 0, 1, 10)
        if not self.acc.answer.is_finished: btn_view_brand.setDisabled(True)

        btn_setting = PySide2.QtWidgets.QPushButton()
        btn_setting.setFont(QFont(font, 18))
        btn_setting.setText("⚙️ " + interface_lang.get("Settings"))
        btn_setting.clicked.connect(lambda: self.goto_setting())
        layout.addWidget(btn_setting, 6, 0, 1, 10)

        btn_wallpaper = PySide2.QtWidgets.QPushButton()
        btn_wallpaper.setFont(QFont(font, 18))
        btn_wallpaper.setText("🎨 " + interface_lang.get("DownloadWallpaper"))
        btn_wallpaper.clicked.connect(lambda: self.goto_wallpaper())
        layout.addWidget(btn_wallpaper, 7, 0, 1, 10)

        lb_temp = QLabel("\n" * 500)
        layout.addWidget(lb_temp, 8, 0, 1, 10)

        btn_about = PySide2.QtWidgets.QPushButton()
        btn_about.setFont(QFont(font, 18))
        btn_about.setText("🛈 " + interface_lang.get("About"))
        btn_about.clicked.connect(lambda: self.goto_about())
        layout.addWidget(btn_about, 9, 0, 1, 7)

        btn_quit = PySide2.QtWidgets.QPushButton()
        btn_quit.setFont(QFont(font, 18))
        btn_quit.setText(interface_lang.get("Quit"))
        btn_quit.clicked.connect(lambda: sys.exit())
        layout.addWidget(btn_quit, 9, 7, 1, 3)

        self.app_window.setCentralWidget(window)

    def goto_story_selection(self): self.callback("StorySelection")

    def goto_view_brand(self): self.callback("ViewBrand")

    def goto_setting(self): self.callback("Setting")

    def goto_wallpaper(self):
        lang = LangString()
        interface_lang = InterfaceLangString()
        font = FONTNAMES.get_font(lang.get_language_code())

        window = QWidget()
        layout = QGridLayout()
        layout.setSpacing(5)
        window.setLayout(layout)

        dialog = QDialog()
        dialog.setWindowTitle(interface_lang.get("DownloadWallpaper"))
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.setFixedWidth(calc_font_size(900))
        dialog.setFixedHeight(calc_font_size(300))

        dialog.setLayout(layout)

        lb_description = QLabel(interface_lang.get("DownloadWallpaper_Description"))
        lb_description.setFont(QFont(font, 15))
        lb_description.setAlignment(Qt.AlignLeft)
        lb_description.setWordWrap(True)
        layout.addWidget(lb_description, 0, 0, 1, 10)

        btn_lanzou = PySide2.QtWidgets.QPushButton()
        btn_lanzou.setFont(QFont(font, 15))
        btn_lanzou.setText(interface_lang.get("DownloadWallpaper_Lanzoui"))
        btn_lanzou.clicked.connect(lambda: webbrowser.open(WALLPAPER_DOWNLOAD_CN))
        layout.addWidget(btn_lanzou, 1, 0, 1, 10)

        btn_mega = PySide2.QtWidgets.QPushButton()
        btn_mega.setFont(QFont(font, 15))
        btn_mega.setText(interface_lang.get("DownloadWallpaper_Mega"))
        btn_mega.clicked.connect(lambda: webbrowser.open(WALLPAPER_DOWNLOAD_MEGA))
        layout.addWidget(btn_mega, 2, 0, 1, 10)

        btn_goo = PySide2.QtWidgets.QPushButton()
        btn_goo.setFont(QFont(font, 15))
        btn_goo.setText(interface_lang.get("DownloadWallpaper_Google"))
        btn_goo.clicked.connect(lambda: webbrowser.open(WALLPAPER_DOWNLOAD_GOOGLE))
        layout.addWidget(btn_goo, 3, 0, 1, 10)

        dialog.exec_()

    def goto_about(self):
        lang = LangString()
        interface_lang = InterfaceLangString()
        font = FONTNAMES.get_font(lang.get_language_code())

        window = QWidget()
        layout = QGridLayout()
        layout.setSpacing(5)
        window.setLayout(layout)

        dialog = QDialog()
        dialog.setWindowTitle(interface_lang.get("About"))
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.setFixedWidth(calc_font_size(900))
        dialog.setFixedHeight(calc_font_size(300))

        dialog.setLayout(layout)

        browser_description = QTextBrowser()
        with open("data/page/css/all_font.css", mode="r", encoding="UTF-8") as file: css_all_font = file.read()
        with open("data/page/css/set_p_firacode.css", mode="r", encoding="UTF-8") as file: css_set_p = file.read()
        with open("data/page/about.html", mode="r", encoding="UTF-8") as file: html_content = file.read()
        html_content = html_content.format(fontsize_22=int(calc_font_size(22)), fontsize_18=int(calc_font_size(18)),
                                           all_font=css_all_font, p_set_font=css_set_p)
        browser_description.setHtml(html_content)
        layout.addWidget(browser_description, 0, 0, 1, 1)

        dialog.exec_()
