import PySide2.QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QGridLayout, QLabel, QMainWindow, QLineEdit, QMessageBox, QFontDialog
from Account.AccountManager import AccountManager
from Account.SettingManager import SettingManager
from Lang.Interface.InterfaceLangString import InterfaceLangString
from Lang.Steam.LangString import LangString
from Lang.Steam.constants import LANGPACK_NAME
from Qt.constants import FONTNAMES
from Qt.tool import QFont_recreate as QFont


class PageSetting:
    def __init__(self, app_window: QMainWindow, acc: AccountManager, callback):
        self.setting = SettingManager()
        self.app_window = app_window
        self.callback = callback
        self.acc = acc

    def load(self):
        self.window = QWidget()

        layout = QGridLayout()
        layout.setSpacing(5)
        self.window.setLayout(layout)

        lang = LangString()
        interface_lang = InterfaceLangString()
        font = FONTNAMES.get_font(lang.get_language_code())

        lb_title = QLabel(interface_lang.get("Settings"))
        lb_title.setFont(QFont(font, 40))
        lb_title.setAlignment(Qt.AlignCenter)
        layout.addWidget(lb_title, 0, 0, 1, 10)

        lb_interface_section = QLabel(interface_lang.get("Settings_Interface_Title"))
        lb_interface_section.setFont(QFont(font, 30))
        layout.addWidget(lb_interface_section, 1, 0, 1, 10)

        lb_language = QLabel(interface_lang.get("Settings_Interface_Language_Label"))
        lb_language.setFont(QFont(font, 20))
        layout.addWidget(lb_language, 2, 0, 1, 4)

        combo_language = PySide2.QtWidgets.QComboBox()
        combo_language.addItems(sorted(LANGPACK_NAME.keys(), key=str.lower))
        combo_language.setCurrentText(lang.lang_name)
        combo_language.setFont(QFont(font, 20))
        combo_language.currentTextChanged.connect(lambda: self.change_curr_language(combo_language.currentText()))
        layout.addWidget(combo_language, 2, 4, 1, 6)

        lb_preferred_language = QLabel(interface_lang.get("Settings_Interface_PreferredLanguage_Label"))
        lb_preferred_language.setFont(QFont(font, 20))
        layout.addWidget(lb_preferred_language, 3, 0, 1, 4)

        combo_preferred_language = PySide2.QtWidgets.QComboBox()
        combo_preferred_language.addItems(sorted(LANGPACK_NAME.keys(), key=str.lower))
        combo_preferred_language.setCurrentText(lang.lang_name)
        combo_preferred_language.setFont(QFont(font, 20))
        combo_preferred_language.currentTextChanged.connect(
            lambda: self.change_preferred_lang(combo_preferred_language.currentText()))
        layout.addWidget(combo_preferred_language, 3, 4, 1, 6)

        lb_font_scale = QLabel(interface_lang.get("Settings_Interface_Fontscale_Label"))
        lb_font_scale.setFont(QFont(font, 20))
        layout.addWidget(lb_font_scale, 4, 0, 1, 4)

        counter_fontscale = PySide2.QtWidgets.QSpinBox()
        counter_fontscale.setFont(QFont(font, 20))
        counter_fontscale.setMinimum(-20)
        counter_fontscale.setMaximum(20)
        counter_fontscale.setValue(SettingManager().fontScale)
        counter_fontscale.valueChanged.connect(lambda: self.change_fontscale(counter_fontscale.value()))
        layout.addWidget(counter_fontscale, 4, 4, 1, 6)

        lb_select_font = QLabel(interface_lang.get("Settings_Interface_FontSelect_Label"))
        lb_select_font.setFont(QFont(font, 20))
        layout.addWidget(lb_select_font, 5, 0, 1, 5)

        btn_select_font = PySide2.QtWidgets.QPushButton()
        btn_select_font.setFont(QFont(font, 20))
        btn_select_font.setText(interface_lang.get("Settings_Interface_FontSelect_Button"))
        btn_select_font.clicked.connect(lambda: self.select_font())
        layout.addWidget(btn_select_font, 5, 5, 1, 5)

        lb_save_section = QLabel(interface_lang.get("Settings_Save_Title"))
        lb_save_section.setFont(QFont(font, 30))
        layout.addWidget(lb_save_section, 6, 0, 1, 10)

        lb_change_username = QLabel(interface_lang.get("Settings_Save_ChangeUsername_Label"))
        lb_change_username.setFont(QFont(font, 20))
        layout.addWidget(lb_change_username, 7, 0, 1, 4)

        line_change_username = QLineEdit()
        line_change_username.setText(self.acc.username)
        line_change_username.setFont(QFont(font, 20))
        layout.addWidget(line_change_username, 7, 4, 1, 6)

        btn_change_username = PySide2.QtWidgets.QPushButton()
        btn_change_username.setFont(QFont(font, 20))
        btn_change_username.setText(interface_lang.get("Settings_Save_ChangeUsername_Button"))
        btn_change_username.clicked.connect(lambda: self.change_username(line_change_username.text()))
        layout.addWidget(btn_change_username, 8, 4, 1, 6)

        lb_reset_save = QLabel(interface_lang.get("Settings_Save_ResetSave_Label"))
        lb_reset_save.setFont(QFont(font, 20))
        layout.addWidget(lb_reset_save, 9, 0, 1, 6)

        btn_reset_save = PySide2.QtWidgets.QPushButton()
        btn_reset_save.setFont(QFont(font, 20))
        btn_reset_save.setText(interface_lang.get("Settings_Save_ResetSave_Button"))
        btn_reset_save.clicked.connect(lambda: self.reset_save())
        layout.addWidget(btn_reset_save, 9, 6, 1, 4)

        layout.addWidget(QLabel("\n" * 500), 10, 0, 1, 10)

        btn_reset_save = PySide2.QtWidgets.QPushButton("<")
        btn_reset_save.setFont(QFont(font, 25))
        btn_reset_save.clicked.connect(lambda: self.callback())
        layout.addWidget(btn_reset_save, 11, 0, 1, 10)

        self.app_window.setCentralWidget(self.window)

    def change_curr_language(self, value):
        LangString().reload(value)
        self.load()

    def change_preferred_lang(self, value):
        self.setting.defaultLanguage = value

    def change_fontscale(self, value):
        self.setting.fontScale = value
        self.load()

    def select_font(self):
        ok, font = QFontDialog.getFont()
        if ok:
            self.setting.fontName = font.family()
            self.load()

    def change_username(self, value):
        self.acc.save.username = value
        self.acc.reload(value)

    def reset_save(self):
        interface_lang = InterfaceLangString()

        reply = QMessageBox.question(self.window, interface_lang.get("ResetProgress_WarningTitle"),
                                     interface_lang.get("ResetProgress_WarningDescription"),
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == PySide2.QtWidgets.QMessageBox.StandardButton.Yes:
            self.acc.reset(self.acc.username)

