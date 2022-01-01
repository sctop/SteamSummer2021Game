from collections import namedtuple

__all__ = ["LangStringMap"]

StoryInfo = namedtuple("StoryInfo", ["Title", "Genre", "GenreId", "Intro", "Choice1", "Choice2"])
StoryIntro = namedtuple("StoryIntro", ["Content", "Page"])
StoryChoice = namedtuple("StoryChoice", ["Content", "Outcome"])
StoryOutcome = namedtuple("StoryOutcome", ["Content", "Page", "Summary"])
BadgeInfo = namedtuple("BadgeInfo", ["Numbering", "Title", "Description"])


class LangStringMap:
    def __init__(self, dictionary: dict):
        self._dictionary = dictionary
        self.load()

    def load(self):
        # For each story
        self.ALL_STORIES = dict()

        def build_story(genre: str):
            def get(*keys):
                id_ = f"Summer21_Story_{genre}_{'_'.join(keys)}"
                return self._dictionary[id_]

            outcome1 = StoryOutcome(get("Outcome1"), get("Outcome1", "Pg"),
                                    get("Outcome1", "Summary"))
            choice1 = StoryChoice(get("Choice1"), outcome1)
            outcome2 = StoryOutcome(get("Outcome2"), get("Outcome2", "Pg"),
                                    get("Outcome2", "Summary"))
            choice2 = StoryChoice(get("Choice2"), outcome2)
            intro = StoryIntro(get("Intro"), get("Pg"))
            story = StoryInfo(get("Title"), get("Genre"), genre, intro, choice1, choice2)
            self.ALL_STORIES[genre] = story
            return story

        self.STORY_HORROR = build_story("Horror")
        self.STORY_ACTION = build_story("Action")
        self.STORY_ADVENTURE = build_story("Adventure")
        self.STORY_RPG = build_story("RPG")
        self.STORY_SIM = build_story("Sim")
        self.STORY_STRATEGY = build_story("Strategy")
        self.STORY_SPORTS = build_story("Sports")
        self.STORY_SURVIVAL = build_story("Survival")
        self.STORY_OPEN = build_story("Open")
        self.STORY_SCIFI = build_story("SciFi")
        self.STORY_SPACE = build_story("Space")
        self.STORY_MYSTERY = build_story("Mystery")
        self.STORY_ROGUELIKE = build_story("Roguelike")
        self.STORY_ANIME = build_story("Anime")

        # For each brand
        def build_badge(number: int):
            def get(*keys):
                id_ = f"Summer21_Badge_Outcome{number}_{'_'.join(keys)}"
                return self._dictionary[id_]

            badge = BadgeInfo(number, get("Title"), get("Description"))
            return badge

        self.ALL_BADGES = [build_badge(i) for i in range(1, 6)]

        # Common
        self.END_TEXT = self._dictionary["Summer21_Story_End"]
        self.TEXT_WALLPAPER = self._dictionary["Summer21_Story_DownloadWallpaper"]

    def story_hint(self, *keys):
        return self._dictionary.get(f"Summer_21_Story_{'_'.join(keys)}", "None")

    def story_overview(self, *keys):
        return self._dictionary.get(f"Summer_21_Overview_{'_'.join(keys)}", "None")

    def badge_info(self, *keys):
        return self._dictionary.get(f"Summer_21_Badge_{'_'.join(keys)}", "None")

    def get(self, key):
        return self._dictionary.get(key, "None")

    def get_language_code(self):
        return self.get("language")

    def get_storyinfo(self, genre: str) -> StoryInfo:
        return self.ALL_STORIES[genre]

    def get_brandinfo(self, number:int) -> BadgeInfo:
        """Starts from 1 to the end of 5"""
        return self.ALL_BADGES[number-1]
