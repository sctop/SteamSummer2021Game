import PySide2.QtWidgets
import re
from PySide2.QtWidgets import QWidget, QGridLayout, QLabel, QMainWindow, QLineEdit, QTextBrowser, QFileDialog, \
    QMessageBox
from PySide2.QtCore import Qt, QUrl, QSize
from PySide2.QtGui import QMovie
from Lang.Steam.LangString import LangString
from Qt.constants import FONTNAMES
from Lang.Interface.InterfaceLangString import InterfaceLangString
from Qt.ImageHandler import ImageHandler
from Qt.tool import QFont_recreate as QFont


class PageStoryOutcome:
    def __init__(self, app_window: QMainWindow, genre: str, choice: int, callback):
        self.app_window = app_window
        self.genre = genre
        self.choice = choice
        self.callback = callback

    def load(self):
        self.window = QWidget()

        layout = QGridLayout()
        layout.setSpacing(5)
        self.window.setLayout(layout)

        lang = LangString().mapping
        interface_lang = InterfaceLangString()
        font = FONTNAMES.get_font(lang.get_language_code())

        lb_you_got_sticker = QLabel(lang.get("Summer_21_Story_Sticker_Unlock"))
        lb_you_got_sticker.setAlignment(Qt.AlignCenter)
        lb_you_got_sticker.setFont(QFont(font, 28))
        layout.addWidget(lb_you_got_sticker, 0, 0, 1, 10)

        size_width = self.app_window.size().width()

        """
        browser_sticker = QTextBrowser()
        browser_sticker.setFixedWidth(size_width / 10 * 3)
        browser_sticker.setFixedHeight(size_width / 10 * 3)
        browser_sticker.insertHtml('<div style="margin:5px; border:0px; padding:0px">' + \
                                   f'<center><img src="{ImageHandler.get_outcome_filepath(self.genre, self.choice)}"'
                                   f'style="width: {size_width / 10 * 3 - 10}"></center></div>')
        layout.addWidget(browser_sticker, 1, 0, 3, 3)
        """

        lb_sticker = QLabel()
        lb_sticker.setFixedWidth(size_width / 10 * 3)
        lb_sticker.setFixedHeight(size_width / 10 * 3)
        layout.addWidget(lb_sticker, 1, 0, 3, 3)
        movie_sticker = QMovie(ImageHandler.get_outcome_gif_filepath(self.genre, self.choice))
        lb_sticker.setMovie(movie_sticker)
        movie_sticker.setScaledSize(QSize(size_width / 10 * 3 - 5, size_width / 10 * 3 - 5))
        movie_sticker.start()

        lb_inventory = QLabel(lang.get("Summer_21_Story_Sticker_Inventory"))
        lb_inventory.setFont(QFont(font, 20))
        lb_inventory.setAlignment(Qt.AlignTop)
        layout.addWidget(lb_inventory, 1, 3, 2, 7)

        btn_save_image = PySide2.QtWidgets.QPushButton(interface_lang.get("SaveSticker"))
        btn_save_image.setFont(QFont(font, 20))
        btn_save_image.clicked.connect(lambda: self.save_image())
        layout.addWidget(btn_save_image, 3, 3, 1, 7)

        browser_outcome = QTextBrowser()
        if self.choice == 1: choice = lang.ALL_STORIES[self.genre].Choice1
        else: choice = lang.ALL_STORIES[self.genre].Choice2
        browser_outcome.insertHtml(f'<b><p>{choice.Content}</p></b><hr />' + \
                                   f'<p>{choice.Outcome.Content}</p><p>> {choice.Outcome.Summary}</p>')
        browser_outcome.setFont(QFont(font, 18))
        layout.addWidget(browser_outcome, 4, 0, 1, 10)

        btn_back = PySide2.QtWidgets.QPushButton("<")
        btn_back.setFont(QFont(font, 18))
        btn_back.clicked.connect(lambda: self.callback(self.genre))
        layout.addWidget(btn_back, 5, 0, 1, 2)

        line_page_number = QLineEdit(str(choice.Outcome.Page))
        line_page_number.setAlignment(Qt.AlignCenter)
        line_page_number.setFont(QFont(font, 18))
        line_page_number.setReadOnly(True)
        layout.addWidget(line_page_number, 5, 8, 1, 2)

        self.app_window.setCentralWidget(self.window)

    def save_image(self):
        filename, _ = QFileDialog.getSaveFileUrl(caption="Save Image", dir=QUrl("C:\\"),
                                                 filter="Animated PNG (*.png)")

        filename = re.search("file:///(.*?)'", str(filename)).group(1)
        interface_lang = InterfaceLangString()
        try:
            # Open Original file
            with open(ImageHandler.get_outcome_filepath(self.genre, self.choice), mode="rb") as file:
                content = file.read()
            with open(str(filename), mode="wb") as file:
                file.write(content)
        except Exception:
            QMessageBox.warning(self.window, interface_lang.get("SaveErrorTitle"), interface_lang.get("SaveErrorDesc"),
                                QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.information(self.window, interface_lang.get("SaveOKTitle"), interface_lang.get("SaveOKDesc"),
                                    QMessageBox.Ok, QMessageBox.Ok)
