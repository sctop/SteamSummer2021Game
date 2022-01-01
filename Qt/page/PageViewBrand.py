import datetime
import PySide2.QtWidgets
from dateutil import tz
from PySide2.QtWidgets import QWidget, QGridLayout, QLabel, QMainWindow, QLineEdit, QTextBrowser, QDialog
from PySide2.QtCore import Qt
from Lang.Steam.LangString import LangString
from Qt.constants import FONTNAMES
from Lang.Interface.InterfaceLangString import InterfaceLangString
from Account.AccountManager import AccountManager
from Qt.ImageHandler import ImageHandler
from Qt.tool import QFont_recreate as QFont, calc_font_size


class PageViewBrand:
    def __init__(self, app_window: QMainWindow, acc: AccountManager, callback):
        self.app_window = app_window
        self.acc = acc
        self.callback = callback

    def load(self):
        window = QWidget()

        layout = QGridLayout()
        layout.setSpacing(5)
        window.setLayout(layout)

        lang = LangString().mapping
        interface_lang = InterfaceLangString()
        font = FONTNAMES.get_font(lang.get_language_code())

        lb_title = QLabel(lang.get("Summer21_Badge_Unlocked_Title"))
        lb_title.setAlignment(Qt.AlignCenter)
        lb_title.setFont(QFont(font, 30))
        layout.addWidget(lb_title, 0, 0, 1, 10)

        brand_info = lang.get_brandinfo(int(self.acc.save.brand))
        brand_image = ImageHandler.get_brand_filepath(self.acc.save.brand)

        browser_show = QTextBrowser()
        # 加载字体
        browser_show.setHtml('<html><head><link rel="stylesheet" href="data/page/css/all_font.css">' +
                             "<style>p {font-family: \"" + font + "\";}</style></head>" +
                             f'<body><p style="font-size: {int(calc_font_size(30))}px;">' +
                             lang.get("Summer21_Badge_Prelude") + "</p>" +
                             f'<center><img src={brand_image}><p style="font-size: {int(calc_font_size(48))}px;">' +
                             brand_info.Title + "</p></center><hr />" +
                             f'<p style="font-size: {int(calc_font_size(24))}px;">' +
                             brand_info.Description + "</p></body></html>")
        layout.addWidget(browser_show, 1, 0, 1, 10)

        line_time = QLineEdit()
        line_time.setFont(QFont(font, 18))
        line_time.setAlignment(Qt.AlignCenter)
        line_time.setText(interface_lang.get("AchieveTime") + self.get_local_time(self.acc.save.brand_date))
        layout.addWidget(line_time, 2, 0, 1, 10)

        btn_back = PySide2.QtWidgets.QPushButton("<")
        btn_back.setFont(QFont(font, 18))
        btn_back.clicked.connect(lambda: self.callback())
        layout.addWidget(btn_back, 3, 0, 1, 2)

        btn_cheatsheet = PySide2.QtWidgets.QPushButton()
        btn_cheatsheet.setText("🛈 " + interface_lang.get("Cheatsheet"))
        btn_cheatsheet.setFont(QFont(font, 18))
        btn_cheatsheet.clicked.connect(lambda: self.show_cheatsheet())
        layout.addWidget(btn_cheatsheet, 3, 2, 1, 4)

        btn_congrat = PySide2.QtWidgets.QPushButton()
        btn_congrat.setFont(QFont(font, 18))
        btn_congrat.setText("🎉 " + interface_lang.get("Congrats"))
        btn_congrat.clicked.connect(lambda: self.show_congrat())
        layout.addWidget(btn_congrat, 3, 6, 1, 4)

        self.app_window.setCentralWidget(window)

    def show_cheatsheet(self):
        interface_lang = InterfaceLangString()

        window = QWidget()
        layout = QGridLayout()
        layout.setSpacing(5)
        window.setLayout(layout)

        dialog = QDialog()
        dialog.setWindowTitle(interface_lang.get("Cheatsheet"))
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.setFixedWidth(calc_font_size(900))
        dialog.setFixedHeight(calc_font_size(300))

        dialog.setLayout(layout)

        browser = QTextBrowser()
        with open("data/page/brand_cheatsheet.html", mode="r", encoding="UTF-8") as file: html_content = file.read()
        with open("data/page/css/brand_cheatsheet.css", mode="r", encoding="UTF-8") as file:
            css_content = file.read()
            css_content = css_content.replace("[FONTSIZE_TABLE]", str(int(calc_font_size(18))))
            css_content = css_content.replace("[FONTSIZE_CREDIT]", str(int(calc_font_size(10))))
            html_content = html_content.format(css_here=css_content)
        browser.setHtml(html_content)
        layout.addWidget(browser, 0, 0, 1, 10)

        dialog.exec_()

    def show_congrat(self):
        lang = LangString().mapping
        interface_lang = InterfaceLangString()
        font = FONTNAMES.get_font(lang.get_language_code())

        window = QWidget()
        layout = QGridLayout()
        layout.setSpacing(5)
        window.setLayout(layout)

        dialog = QDialog()
        dialog.setWindowTitle(interface_lang.get("Congrats"))
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.setFixedWidth(calc_font_size(600))
        dialog.setFixedHeight(calc_font_size(600))

        dialog.setLayout(layout)

        browser = QTextBrowser()
        browser.setFont(QFont(font, 18))
        browser.insertHtml("<center><h1>" + lang.get("Summer21_Badge_Congrats1") + \
                           lang.get("Summer21_Badge_Unlocked_Title") + "</h1></center>" + \
                           "<hr /><p>" + lang.get("Summer21_Badge_Unlocked_Description") + "</p>")
        layout.addWidget(browser, 0, 0, 1, 10)

        dialog.exec_()

    def get_local_time(self, timestamp: int):
        """https://stackoverflow.com/a/4771733/16205869"""
        local_zone = tz.tzlocal()

        utc = datetime.datetime.fromtimestamp(timestamp)
        local_time = utc.astimezone(local_zone)
        print(local_zone)

        return local_time.strftime("%Y-%m-%d %H:%M:%S")
