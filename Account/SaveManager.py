import os
import json
import time
from constant import PATH_SAVE


class SaveManager:
    def __init__(self, username: str, basepath: str = PATH_SAVE):
        self.filepath = os.path.join(basepath, f"{username}.json")
        if not os.path.exists(basepath): os.mkdir(basepath)
        try:
            with open(self.filepath, mode="r", encoding="UTF-8") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self._create(username, self.filepath)

    def _create(self, username: str, filepath: str):
        self.data = {
            "username": username,
            "choices": {"Horror": -1, "Action": -1, "Adventure": -1, "RPG": -1, "Sim": -1, "Strategy": -1,
                        "Sports": -1, "Survival": -1, "Open": -1, "SciFi": -1, "Space": -1, "Mystery": -1,
                        "Roguelike": -1, "Anime": -1},
            "brand": {"number": -1, "date": -1, "has_seen": 0}
        }
        self.__save()
        self.__is_new = True

    def __save(self):
        with open(self.filepath, mode="w", encoding="UTF-8") as file:
            json.dump(self.data, file)

    # Username
    @property
    def username(self): return self.data["username"]

    @username.setter
    def username(self, username):
        temp = list(os.path.split(self.filepath))
        temp[-1] = f"{username}.json"
        os.remove(self.filepath)
        self.filepath = os.path.join(*temp)
        self.__save()

    # Brand
    @property
    def brand(self): return self.data["brand"]["number"]

    @brand.setter
    def brand(self, number: int):
        self.data["brand"]["number"] = number
        self.data["brand"]["date"] = time.time()
        self.data["brand"]["has_seen"] = 0
        self.__save()

    # Brand Date
    @property
    def brand_date(self): return self.data["brand"]["date"]

    # Brand Has Seen
    @property
    def brand_has_seen(self):
        if self.brand == -1 or self.data["brand"]["has_seen"] == 0:
            return False
        return True

    def change_brand_has_seen(self):
        self.data["brand"]["has_seen"] = 1
        self.__save()

    # Choice
    def get_choice(self, genre: str):
        return self.data["choices"][genre]

    def update_choice(self, genre: str, number: int):
        self.data["choices"][genre] = number
        self.__save()

    # Is New User?
    @property
    def is_new_user(self):
        try: return self.__is_new
        except Exception: return False
