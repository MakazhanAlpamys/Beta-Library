from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                             QLineEdit, QPushButton, QStackedWidget, QMessageBox)
from PyQt5.QtCore import Qt
from utils.db_operations import DatabaseOperations
from utils.email_service import EmailService
from utils.ui_components import create_back_button, create_logo, create_title

class ResetPasswordWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Растау")
        self.setFixedSize(400, 600)
        self.db_ops = DatabaseOperations()
        self.email_service = EmailService()
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.stacked_widget = QStackedWidget()
        self.layout.addWidget(self.stacked_widget)
        
        self.create_email_page()
        self.create_code_page()
        self.create_new_password_page()
    
    def create_email_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setAlignment(Qt.AlignCenter)
        
        back_button = create_back_button()
        back_button.clicked.connect(self.go_back)
        layout.addWidget(back_button, alignment=Qt.AlignLeft)
        
        layout.addWidget(create_logo())
        layout.addWidget(create_title("Растау"))
        
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("email")
        layout.addWidget(self.email_input)
        
        submit_button = QPushButton("Код алу")
        submit_button.clicked.connect(self.send_code)
        layout.addWidget(submit_button)
        
        self.stacked_widget.addWidget(page)
    
    def create_code_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setAlignment(Qt.AlignCenter)
        
        back_button = create_back_button()
        back_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        layout.addWidget(back_button, alignment=Qt.AlignLeft)
        
        layout.addWidget(create_logo())
        layout.addWidget(create_title("Растау"))
        
        self.code_input = QLineEdit()
        self.code_input.setPlaceholderText("Код")
        layout.addWidget(self.code_input)
        
        submit_button = QPushButton("Растау")
        submit_button.clicked.connect(self.verify_code)
        layout.addWidget(submit_button)
        
        resend_button = QPushButton("Қайта жіберу")
        resend_button.setObjectName("linkButton")
        resend_button.clicked.connect(self.send_code)
        layout.addWidget(resend_button)
        
        self.stacked_widget.addWidget(page)
    
    def create_new_password_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setAlignment(Qt.AlignCenter)
        
        back_button = create_back_button()
        back_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        layout.addWidget(back_button, alignment=Qt.AlignLeft)
        
        layout.addWidget(create_logo())
        layout.addWidget(create_title("Құпия сөзді өзгерту"))
        
        self.new_password = QLineEdit()
        self.new_password.setPlaceholderText("Құпия сөз")
        self.new_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.new_password)
        
        self.confirm_password = QLineEdit()
        self.confirm_password.setPlaceholderText("Құпия сөз")
        self.confirm_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.confirm_password)
        
        submit_button = QPushButton("Өзгерту")
        submit_button.clicked.connect(self.change_password)
        layout.addWidget(submit_button)
        
        self.stacked_widget.addWidget(page)
    
    def send_code(self):
        email = self.email_input.text()
        if not email:
            QMessageBox.warning(self, "Қате", "Email енгізіңіз")
            return
            
        if not self.db_ops.verify_email(email):
            QMessageBox.warning(self, "Қате", "Email табылмады")
            return
            
        if self.email_service.send_verification_code(email):
            self.stacked_widget.setCurrentIndex(1)
        else:
            QMessageBox.warning(self, "Қате", "Код жіберу кезінде қате орын алды")
    
    def verify_code(self):
        code = self.code_input.text()
        email = self.email_input.text()
        
        if not code:
            QMessageBox.warning(self, "Қате", "Кодты енгізіңіз")
            return
            
        if self.email_service.verify_code(email, code):
            self.stacked_widget.setCurrentIndex(2)
        else:
            QMessageBox.warning(self, "Қате", "Қате код")
    
    def change_password(self):
        new_password = self.new_password.text()
        confirm_password = self.confirm_password.text()
        
        if not new_password or not confirm_password:
            QMessageBox.warning(self, "Қате", "Барлық өрістерді толтырыңыз")
            return
            
        if new_password != confirm_password:
            QMessageBox.warning(self, "Қате", "Құпия сөздер сәйкес келмейді")
            return
            
        email = self.email_input.text()
        if self.db_ops.update_password(email, new_password):
            QMessageBox.information(self, "Сәтті", "Құпия сөз өзгертілді")
            self.go_back()
        else:
            QMessageBox.warning(self, "Қате", "Құпия сөзді өзгерту кезінде қате орын алды")
    
    def go_back(self):
        from login_window import LoginWindow
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()