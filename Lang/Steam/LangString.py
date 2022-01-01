import os
import pickle
from constant import Singleton, PATH_LANGPACK
from Lang.Steam.constants import *
from Lang.Steam.LangStringMapping import *
from Lang.Steam.exceptions import *


class LangString(metaclass=Singleton):
    __lang_name = None
    __is_initialized = False

    def __init__(self, lang_code: str = None):
        if not self.__is_initialized:
            if lang_code is None:
                raise LangStringInitError
            self.__lang_name = lang_code
            self.__load()
            self._mapping = LangStringMap(self._dictionary)
            self.__is_initialized = True

    def __load(self):
        filename = LANGPACK_NAME[self.__lang_name]
        try:
            with open(os.path.join(PATH_LANGPACK, filename), mode="rb") as file:
                self._dictionary = pickle.load(file)
        except Exception:
            try:
                with open(os.path.join(PATH_LANGPACK, "english.pickle"), mode="rb") as file:
                    self._dictionary = pickle.load(file)
            except Exception as e:
                raise LangStringLoadError(str(e))

    def reload(self, lang):
        self.__lang_name = lang
        self.__load()
        self._mapping = LangStringMap(self._dictionary)
        self.__is_initialized = True

    def check_if_initalized(self):
        return False if not self.__is_initialized else True

    def get(self, key: str):
        if not self.__is_initialized: raise LangStringInitError
        return self._dictionary[key]

    def get_language_code(self):
        return self._dictionary["language"]

    @property
    def mapping(self):
        if not self.__is_initialized: raise LangStringInitError
        return self._mapping

    @property
    def lang_name(self): return self.__lang_name
