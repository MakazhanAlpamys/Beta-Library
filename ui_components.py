from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

def create_back_button():
    """Create a standardized back button with arrow icon"""
    back_button = QPushButton()
    back_pixmap = QPixmap("arrow.png")
    back_icon = QIcon(back_pixmap)
    back_button.setIcon(back_icon)
    back_button.setIconSize(back_pixmap.size())
    return back_button

def create_logo():
    """Create a standardized logo label"""
    logo_label = QLabel()
    logo_pixmap = QPixmap("logo.png")
    logo_label.setPixmap(logo_pixmap.scaled(200, 200, Qt.KeepAspectRatio))
    logo_label.setAlignment(Qt.AlignCenter)
    return logo_label

def create_title(text):
    """Create a standardized title label"""
    title_label = QLabel(text)
    title_label.setObjectName("titleLabel")
    title_label.setAlignment(Qt.AlignCenter)
    return title_label