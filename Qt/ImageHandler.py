import os
import constant


class ImageHandler:
    @staticmethod
    def get_outcome_filepath(genre: str, number: int):
        basepath = constant.PATH_IMAGE
        return os.path.join(basepath, f"apng/outcome/{genre}Outcome{number}.png")

    @staticmethod
    def get_brand_filepath(number:int):
        basepath = constant.PATH_IMAGE
        return os.path.join(basepath, f"apng/brand/{number}.png")

    @staticmethod
    def get_outcome_gif_filepath(genre: str, number: int):
        basepath = constant.PATH_IMAGE
        return os.path.join(basepath, f"gif/outcome/{genre}Outcome{number}.gif")
