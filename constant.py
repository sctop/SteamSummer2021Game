class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


import os

PATH_FONT = "data/fonts/"
PATH_FONT_REGULAR = PATH_FONT + "{font_name}-Regular"
PATH_FONT_BOLD = PATH_FONT + "{font_name}-Bold"
PATH_IMAGE = "data/img/"
PATH_LANGPACK = "data/lang/"
PATH_INTERFACE_LANG = "data/interface_lang/"
PATH_DATA = "data/"
PATH_SAVE = os.path.expanduser('~/Documents/SteamSummer2021Game')
PATH_SETTING = os.path.expanduser('~/Documents/SteamSummer2021Game/Setting')

ALL_GENRES = ["Horror", "Action", "Adventure", "RPG", "Sim", "Strategy", "Sports", "Survival", "Open", "SciFi",
              "Space", "Mystery", "Roguelike", "Anime"]
