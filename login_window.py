from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                             QLineEdit, QPushButton, QMessageBox)
from PyQt5.QtCore import Qt
from register_window import RegisterWindow
from reset_password_window import ResetPasswordWindow
from main_window import MainWindow
from utils.db_operations import DatabaseOperations
from utils.ui_components import create_logo, create_title

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Кіру")
        self.setFixedSize(400, 600)
        self.db_ops = DatabaseOperations()
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignCenter)
        
        layout.addWidget(create_logo())
        
        layout.addWidget(create_title("Кіру"))
        
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Пайдаланушы аты")
        layout.addWidget(self.username_input)
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Құпия сөз")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)
        
        login_button = QPushButton("Кіру")
        login_button.clicked.connect(self.login)
        layout.addWidget(login_button)
        
        register_button = QPushButton("Аккаунтыңыз жоқ па?")
        register_button.setObjectName("linkButton")
        register_button.clicked.connect(self.show_register)
        layout.addWidget(register_button)
        
        reset_button = QPushButton("Құпия сөзді өзгерту")
        reset_button.setObjectName("linkButton")
        reset_button.clicked.connect(self.show_reset)
        layout.addWidget(reset_button)
    
    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        
        if not username or not password:
            QMessageBox.warning(self, "Қате", "Барлық өрістерді толтырыңыз")
            return
            
        if self.db_ops.login_user(username, password):
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
        else:
            QMessageBox.warning(self, "Қате", "Қате логин немесе құпия сөз")
    
    def show_register(self):
        self.register_window = RegisterWindow()
        self.register_window.show()
        self.hide()
    
    def show_reset(self):
        self.reset_window = ResetPasswordWindow()
        self.reset_window.show()
        self.hide()