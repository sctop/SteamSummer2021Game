import json
import os
from constant import Singleton, PATH_SETTING


class SettingManager(metaclass=Singleton):
    """全局设置管理器"""

    def __init__(self):
        if not os.path.exists(PATH_SETTING):
            os.mkdir(PATH_SETTING)
        try:
            with open(os.path.join(PATH_SETTING, "global.json"), mode="r", encoding="UTF-8") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self._create()

    def _create(self):
        template = {
            "FontScale": 0,  # 字体缩放，以px为单位
            # 用于手动调整字体大小以适应窗口大小（主要是因为没法自动检测系统的字体缩放大小）
            "FontName": "",  # 字体名称
            # 用于存储手动指定的字体名称
            "DefaultLanguage": ""  # 默认语言
            # 用于存储默认语言，以方便用户无需手动选择自己的语言
        }
        self.data = template
        self._save()

    def _save(self):
        print(self.data)
        with open(os.path.join(PATH_SETTING, "global.json"), mode="w", encoding="UTF-8") as file:
            json.dump(self.data, file)

    @property
    def fontScale(self) -> int: return int(self.data["FontScale"])

    @fontScale.setter
    def fontScale(self, value):
        self.data["FontScale"] = value
        self._save()

    @property
    def fontName(self) -> str: return self.data["FontName"]

    @fontName.setter
    def fontName(self, value):
        self.data["FontName"] = value
        self._save()

    @property
    def defaultLanguage(self) -> str: return self.data["DefaultLanguage"]

    @defaultLanguage.setter
    def defaultLanguage(self, value):
        self.data["DefaultLanguage"] = value
        self._save()

