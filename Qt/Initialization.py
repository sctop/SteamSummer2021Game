def load_font():
    from PySide2.QtGui import QFontDatabase

    font_database = QFontDatabase()
    font_database.addApplicationFont("data/fonts/global/NotoSans-Regular.ttf")
    font_database.addApplicationFont("data/fonts/global/NotoSans-Bold.ttf")
    font_database.addApplicationFont("data/fonts/thai/AlibabaSansThai-Rg.otf")
    font_database.addApplicationFont("data/fonts/thai/AlibabaSansThai-Bd.otf")
    font_database.addApplicationFont("data/fonts/firacode/FiraCode-Regular.ttf")
    font_database.addApplicationFont("data/fonts/firacode/FiraCode-Bold.ttf")
    font_database.addApplicationFont("data/fonts/alibaba/AlibabaPuhuiTi-2-55-Regular.ttf")
    font_database.addApplicationFont("data/fonts/alibaba/AlibabaPuhuiTi-2-85-Bold.ttf")
