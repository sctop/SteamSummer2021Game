import os
import json
from constant import Singleton, PATH_INTERFACE_LANG
from Lang.Steam.LangString import LangString


class InterfaceLangString(metaclass=Singleton):
    _lang_code = "None"

    def __init__(self):
        self.reload()

    def __load(self):
        filepath = os.path.join(PATH_INTERFACE_LANG, f"{self._lang_code}.json")
        try:
            with open(filepath, mode="r", encoding="UTF-8") as file:
                self.data = json.load(file)
        except Exception:
            filepath = os.path.join(PATH_INTERFACE_LANG, f"english.json")
            with open(filepath, mode="r", encoding="UTF-8") as file:
                self.data = json.load(file)

    def reload(self):
        current = LangString().get_language_code()
        if current != self._lang_code:
            self._lang_code = current
            self.__load()

    def get(self, key):
        self.reload()
        return self.data.get(key, "Unknown")
