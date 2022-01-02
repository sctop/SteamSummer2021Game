from Account.SaveManager import SaveManager
from constant import ALL_GENRES


class AnswerManager:
    def __init__(self, save_manager: SaveManager):
        self.manager = save_manager

    def get_choice(self, genre: str):
        """:returns: 0-None, 1/2-Okay"""
        return self.manager.get_choice(genre)

    def get_brand(self):
        return self.manager.brand

    def update_brand(self):
        action_first, action_second = 0, 0
        for i in ALL_GENRES:
            choice = self.get_choice(i)
            if choice == 0: return -1
            elif choice == 1: action_first += 1
            elif choice == 2: action_second += 1
        if 0 <= action_first <= 2: brand = 5
        elif 3 <= action_first <= 5: brand = 4
        elif 6 <= action_first <= 8: brand = 3
        elif 9 <= action_first <= 11: brand = 2
        elif 12 <= action_first <= 14: brand = 1
        else: raise ValueError(f"{action_first}/{action_second}")
        self.manager.brand = brand
        return brand

    def update_choice(self, genre: str, choice: int):
        if self.manager.get_choice(genre) == -1:
            self.manager.update_choice(genre, choice)
            self.update_brand()

    @property
    def is_finished(self):
        for i in ALL_GENRES:
            if self.get_choice(i) == -1:
                return False
        return True
