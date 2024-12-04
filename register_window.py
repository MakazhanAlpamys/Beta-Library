from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                             QLineEdit, QPushButton, QMessageBox)
from PyQt5.QtCore import Qt
from utils.db_operations import DatabaseOperations
from utils.ui_components import create_back_button, create_logo, create_title

class RegisterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Тіркелу")
        self.setFixedSize(400, 600)
        self.db_ops = DatabaseOperations()
        
        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignCenter)
        
        # Back button
        back_button = create_back_button()
        back_button.clicked.connect(self.go_back)
        layout.addWidget(back_button, alignment=Qt.AlignLeft)
        
        # Logo
        layout.addWidget(create_logo())
        
        # Title
        layout.addWidget(create_title("Тіркелу"))
        
        # Username input
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Пайдаланушы аты")
        layout.addWidget(self.username_input)
        
        # Password input
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Құпия сөз")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)
        
        # Email input
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("email")
        layout.addWidget(self.email_input)
        
        # Custom ID input
        self.custom_id_input = QLineEdit()
        self.custom_id_input.setPlaceholderText("ID номер")
        layout.addWidget(self.custom_id_input)
        
        # Register button
        register_button = QPushButton("Тіркелу")
        register_button.clicked.connect(self.register)
        layout.addWidget(register_button)
        
        # Login link
        login_button = QPushButton("Кіру")
        login_button.setObjectName("linkButton")
        login_button.clicked.connect(self.go_back)
        layout.addWidget(login_button)
    
    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        email = self.email_input.text()
        custom_id = self.custom_id_input.text()
        
        success, message = self.db_ops.register_user(username, password, email, custom_id)
        
        if success:
            QMessageBox.information(self, "Сәтті", message)
            self.go_back()
        else:
            QMessageBox.warning(self, "Қате", message)
    
    def go_back(self):
        from login_window import LoginWindow
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()