import PySide2.QtWidgets
from PySide2.QtWidgets import QLabel, QHBoxLayout
from PySide2.QtGui import Qt
from Qt.tool import QFont_recreate as QFont

def createQPushButtonWithWordWrap(text, label_width=None, label_height=None, fontname=None, fontsize=None):
    # https://stackoverflow.com/a/52053310/16205869 Modified from C++ code
    btn = PySide2.QtWidgets.QPushButton()
    label = QLabel(text, btn)
    label.setStyleSheet("QLabel {width:100%}")
    label.setAlignment(Qt.AlignCenter)
    label.setWordWrap(True)
    if fontsize is not None and fontname is not None: label.setFont(QFont(fontname, fontsize))
    if label_width is not None: label.setFixedWidth(label_width)
    if label_height is not None: label.setFixedHeight(label_height)

    layout_ = QHBoxLayout(btn)
    layout_.addWidget(label, 0, Qt.AlignCenter)
    layout_.setSpacing(0)
    return btn
