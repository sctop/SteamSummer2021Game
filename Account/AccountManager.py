import os
from constant import Singleton
from Account.SaveManager import SaveManager
from Account.AnswerManager import AnswerManager


class AccountInitError(Exception):
    def __init__(self):
        super(AccountInitError, self).__init__()


class AccountManager(metaclass=Singleton):
    __is_initilalized = False
    username = None

    def __init__(self, username: str = None):
        if not self.__is_initilalized:
            if username is None:
                raise AccountInitError
            self.reload(username)
        elif self.__is_initilalized:
            if username is not None:
                self.reload(username)

    def reload(self, username):
        self.save = SaveManager(username)
        self.answer = AnswerManager(self.save)
        self.username = username

    def reset(self, username):
        os.unlink(self.save.filepath)
        self.save = SaveManager(username)
        self.answer = AnswerManager(self.save)
        self.username = username
