import time

from PySide2.QtWidgets import QDesktopWidget, QApplication, QMainWindow
import sys
from Qt.PageContext import PageContext

app = QApplication(sys.argv)
screen = QDesktopWidget().screenGeometry()


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Steam Summer Sale 2021 Game")
        self.center()
        self.init_other()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        self.setFixedSize((5 / 16) * screen.width(), (3 / 2) * ((5 / 16) * screen.width()))

        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2 - 30)

    def init_other(self):
        # Init the stuff
        import Qt.Initialization
        Qt.Initialization.load_font()


if __name__ == '__main__':
    window = Window()
    window.show()

    page_context = PageContext(window)
    page_context.login()

    app.exec_()
