class CustomizedGetDict(dict):
    def get_font(self, language_code):
        from Account.SettingManager import SettingManager
        if SettingManager().fontName != "":
            return SettingManager().fontName
        if language_code not in self.keys():
            return self["global"]
        return self[language_code]


def calc_font_size(original_size: int):
    from PySide2.QtWidgets import QDesktopWidget
    screen = QDesktopWidget().screenGeometry()
    return original_size * screen.width() / 1920


def QFont_recreate(fontname, fontsize):
    from PySide2.QtGui import QFont as QF
    from Account.SettingManager import SettingManager
    target_size = calc_font_size(fontsize+SettingManager().fontScale)
    return QF(fontname, target_size)


def calc_screen_size(screen_width: int):
    # 以1920*1080,16:9为基础
    # 1920*1080 16:9 600,900
    # 1280*720  16:9 400,600
    # 一次缩放函数 - height = (3/2) * width
    # 一次缩放函数 - width = (5/16) * screen_width
    target_width = (5 / 16) * screen_width
    target_height = (3 / 2) * target_width
    return target_width, target_height
