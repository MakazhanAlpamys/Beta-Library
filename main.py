import sys
from PyQt5.QtWidgets import QApplication
from login_window import LoginWindow
from styles import STYLE_SHEET

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(STYLE_SHEET)
    
    login_window = LoginWindow()
    login_window.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()