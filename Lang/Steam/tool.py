import json
import os
import pickle

from constant import PATH_LANGPACK

ALL_LANG_KEYS = ["language", "SummerSale2021_CallToAction_FirstLine", "SummerSale2021_CallToAction_NeedToSignIn",
                 "SummerSale2021_CallToAction_SecondLine", "SummerSale2021_LimitedUserDialogTitle",
                 "SummerSale2021_Story_Next", "Summer_21_Overview_Title_Prefix", "Summer_21_Overview_Title",
                 "Summer_21_Overview_Description1", "Summer_21_Overview_Description3",
                 "Summer_21_Overview_Description4", "Summer_21_Overview_Description2", "Summer_21_Story_Intro",
                 "Summer_21_Story_Next", "Summer_21_Story_Next_Intro", "Summer_21_Story_Enter",
                 "Summer_21_Story_Decide_Notice", "Summer_21_Story_Sticker_Unlock", "Summer_21_Story_Sticker_Inventory",
                 "Summer_21_Story_Continue", "Summer_21_Story_Complete", "Summer21_Story_Horror_Title",
                 "Summer21_Story_Horror_Genre", "Summer21_Story_Horror_Pg", "Summer21_Story_Horror_Intro",
                 "Summer21_Story_Horror_Choice1", "Summer21_Story_Horror_Outcome1_Pg", "Summer21_Story_Horror_Outcome1",
                 "Summer21_Story_Horror_Outcome1_Summary", "Summer21_Story_Horror_Choice2",
                 "Summer21_Story_Horror_Outcome2_Pg", "Summer21_Story_Horror_Outcome2",
                 "Summer21_Story_Horror_Outcome2_Summary", "Summer21_Story_Action_Title", "Summer21_Story_Action_Genre",
                 "Summer21_Story_Action_Pg", "Summer21_Story_Action_Intro", "Summer21_Story_Action_Choice1",
                 "Summer21_Story_Action_Outcome1_Pg", "Summer21_Story_Action_Outcome1",
                 "Summer21_Story_Action_Outcome1_Summary", "Summer21_Story_Action_Choice2",
                 "Summer21_Story_Action_Outcome2_Pg", "Summer21_Story_Action_Outcome2",
                 "Summer21_Story_Action_Outcome2_Summary", "Summer21_Story_Adventure_Title",
                 "Summer21_Story_Adventure_Genre", "Summer21_Story_Adventure_Pg", "Summer21_Story_Adventure_Intro",
                 "Summer21_Story_Adventure_Choice1", "Summer21_Story_Adventure_Outcome1_Pg",
                 "Summer21_Story_Adventure_Outcome1", "Summer21_Story_Adventure_Outcome1_Summary",
                 "Summer21_Story_Adventure_Choice2", "Summer21_Story_Adventure_Outcome2_Pg",
                 "Summer21_Story_Adventure_Outcome2", "Summer21_Story_Adventure_Outcome2_Summary",
                 "Summer21_Story_RPG_Title", "Summer21_Story_RPG_Genre", "Summer21_Story_RPG_Pg",
                 "Summer21_Story_RPG_Intro", "Summer21_Story_RPG_Choice1", "Summer21_Story_RPG_Outcome1_Pg",
                 "Summer21_Story_RPG_Outcome1", "Summer21_Story_RPG_Outcome1_Summary", "Summer21_Story_RPG_Choice2",
                 "Summer21_Story_RPG_Outcome2_Pg", "Summer21_Story_RPG_Outcome2", "Summer21_Story_RPG_Outcome2_Summary",
                 "Summer21_Story_Sim_Title", "Summer21_Story_Sim_Genre", "Summer21_Story_Sim_Pg",
                 "Summer21_Story_Sim_Intro", "Summer21_Story_Sim_Choice1", "Summer21_Story_Sim_Outcome1_Pg",
                 "Summer21_Story_Sim_Outcome1", "Summer21_Story_Sim_Outcome1_Summary", "Summer21_Story_Sim_Choice2",
                 "Summer21_Story_Sim_Outcome2_Pg", "Summer21_Story_Sim_Outcome2", "Summer21_Story_Sim_Outcome2_Summary",
                 "Summer21_Story_Strategy_Title", "Summer21_Story_Strategy_Genre", "Summer21_Story_Strategy_Pg",
                 "Summer21_Story_Strategy_Intro", "Summer21_Story_Strategy_Choice1",
                 "Summer21_Story_Strategy_Outcome1_Pg", "Summer21_Story_Strategy_Outcome1",
                 "Summer21_Story_Strategy_Outcome1_Summary", "Summer21_Story_Strategy_Choice2",
                 "Summer21_Story_Strategy_Outcome2_Pg", "Summer21_Story_Strategy_Outcome2",
                 "Summer21_Story_Strategy_Outcome2_Summary", "Summer21_Story_Sports_Title",
                 "Summer21_Story_Sports_Genre", "Summer21_Story_Sports_Pg", "Summer21_Story_Sports_Intro",
                 "Summer21_Story_Sports_Choice1", "Summer21_Story_Sports_Outcome1_Pg", "Summer21_Story_Sports_Outcome1",
                 "Summer21_Story_Sports_Outcome1_Summary", "Summer21_Story_Sports_Choice2",
                 "Summer21_Story_Sports_Outcome2_Pg", "Summer21_Story_Sports_Outcome2",
                 "Summer21_Story_Sports_Outcome2_Summary", "Summer21_Story_Survival_Title",
                 "Summer21_Story_Survival_Genre", "Summer21_Story_Survival_Pg", "Summer21_Story_Survival_Intro",
                 "Summer21_Story_Survival_Choice1", "Summer21_Story_Survival_Outcome1_Pg",
                 "Summer21_Story_Survival_Outcome1", "Summer21_Story_Survival_Outcome1_Summary",
                 "Summer21_Story_Survival_Choice2", "Summer21_Story_Survival_Outcome2_Pg",
                 "Summer21_Story_Survival_Outcome2", "Summer21_Story_Survival_Outcome2_Summary",
                 "Summer21_Story_Open_Title", "Summer21_Story_Open_Genre", "Summer21_Story_Open_Pg",
                 "Summer21_Story_Open_Intro", "Summer21_Story_Open_Choice1", "Summer21_Story_Open_Outcome1_Pg",
                 "Summer21_Story_Open_Outcome1", "Summer21_Story_Open_Outcome1_Summary", "Summer21_Story_Open_Choice2",
                 "Summer21_Story_Open_Outcome2_Pg", "Summer21_Story_Open_Outcome2",
                 "Summer21_Story_Open_Outcome2_Summary", "Summer21_Story_SciFi_Title", "Summer21_Story_SciFi_Genre",
                 "Summer21_Story_SciFi_Pg", "Summer21_Story_SciFi_Intro", "Summer21_Story_SciFi_Choice1",
                 "Summer21_Story_SciFi_Outcome1_Pg", "Summer21_Story_SciFi_Outcome1",
                 "Summer21_Story_SciFi_Outcome1_Summary", "Summer21_Story_SciFi_Choice2",
                 "Summer21_Story_SciFi_Outcome2_Pg", "Summer21_Story_SciFi_Outcome2",
                 "Summer21_Story_SciFi_Outcome2_Summary", "Summer21_Story_Space_Title", "Summer21_Story_Space_Genre",
                 "Summer21_Story_Space_Pg", "Summer21_Story_Space_Intro", "Summer21_Story_Space_Choice1",
                 "Summer21_Story_Space_Outcome1_Pg", "Summer21_Story_Space_Outcome1",
                 "Summer21_Story_Space_Outcome1_Summary", "Summer21_Story_Space_Choice2",
                 "Summer21_Story_Space_Outcome2_Pg", "Summer21_Story_Space_Outcome2",
                 "Summer21_Story_Space_Outcome2_Summary", "Summer21_Story_Mystery_Title",
                 "Summer21_Story_Mystery_Genre", "Summer21_Story_Mystery_Pg", "Summer21_Story_Mystery_Intro",
                 "Summer21_Story_Mystery_Choice1", "Summer21_Story_Mystery_Outcome1_Pg",
                 "Summer21_Story_Mystery_Outcome1", "Summer21_Story_Mystery_Outcome1_Summary",
                 "Summer21_Story_Mystery_Choice2", "Summer21_Story_Mystery_Outcome2_Pg",
                 "Summer21_Story_Mystery_Outcome2", "Summer21_Story_Mystery_Outcome2_Summary",
                 "Summer21_Story_Roguelike_Title", "Summer21_Story_Roguelike_Genre", "Summer21_Story_Roguelike_Pg",
                 "Summer21_Story_Roguelike_Intro", "Summer21_Story_Roguelike_Choice1",
                 "Summer21_Story_Roguelike_Outcome1_Pg", "Summer21_Story_Roguelike_Outcome1",
                 "Summer21_Story_Roguelike_Outcome1_Summary", "Summer21_Story_Roguelike_Choice2",
                 "Summer21_Story_Roguelike_Outcome2_Pg", "Summer21_Story_Roguelike_Outcome2",
                 "Summer21_Story_Roguelike_Outcome2_Summary", "Summer21_Story_Anime_Title",
                 "Summer21_Story_Anime_Genre", "Summer21_Story_Anime_Pg", "Summer21_Story_Anime_Intro",
                 "Summer21_Story_Anime_Choice1", "Summer21_Story_Anime_Outcome1_Pg", "Summer21_Story_Anime_Outcome1",
                 "Summer21_Story_Anime_Outcome1_Summary", "Summer21_Story_Anime_Choice2",
                 "Summer21_Story_Anime_Outcome2_Pg", "Summer21_Story_Anime_Outcome2",
                 "Summer21_Story_Anime_Outcome2_Summary", "Summer21_Badge_Unlocked_Title",
                 "Summer21_Badge_Unlocked_Description", "Summer21_Badge_Prelude", "Summer21_Badge_Outcome1_Title",
                 "Summer21_Badge_Outcome1_Description", "Summer21_Badge_Outcome2_Title",
                 "Summer21_Badge_Outcome2_Description", "Summer21_Badge_Outcome3_Title",
                 "Summer21_Badge_Outcome3_Description", "Summer21_Badge_Outcome4_Title",
                 "Summer21_Badge_Outcome4_Description", "Summer21_Badge_Outcome5_Title",
                 "Summer21_Badge_Outcome5_Description", "Summer21_Badge_View", "Summer21_Story_End",
                 "Summer21_Badge_Congrats1", "Summer21_Badge_Congrats2", "Summer21_Story_DownloadWallpaper",
                 "dummy_for_end_of_file_convenience"]


def load_language_pack_list():
    def check_if_language_pak_complete(filepath):
        try:
            with open(filepath, mode="rb") as file:
                keys = pickle.load(file).keys()
        except Exception: return False
        for i in ALL_LANG_KEYS:
            if i not in keys:
                # print(filepath, i)
                return False
        return True

    with open(os.path.join(PATH_LANGPACK, "all.json"), mode="r", encoding="UTF-8") as file:
        content = json.load(file)

    need_to_delete = []
    for name, path in content.items():
        if check_if_language_pak_complete(os.path.join(PATH_LANGPACK, path)) is False:
            need_to_delete.append(name)
    for i in need_to_delete: content.pop(i)

    return content
