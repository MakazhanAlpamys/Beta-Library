import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailService:
    def __init__(self):
        self.verification_codes = {}
    
    def generate_code(self, email):
        code = str(random.randint(100000, 999999))
        self.verification_codes[email] = code
        return code
    
    def verify_code(self, email, code):
        stored_code = self.verification_codes.get(email)
        if stored_code and stored_code == code:
            del self.verification_codes[email]
            return True
        return False
    
    def send_verification_code(self, email):
        code = self.generate_code(email)
        print(f"Verification code for {email}: {code}")
        return True