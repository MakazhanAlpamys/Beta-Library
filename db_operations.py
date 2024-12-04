from database import Database
import hashlib
import re

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_custom_id(custom_id):
    if not custom_id:
        return False
    length = len(custom_id)
    return (4 <= length <= 6) or (8 <= length <= 16)

class DatabaseOperations:
    def __init__(self):
        self.db = Database()
    
    def login_user(self, username, password):
        try:
            hashed_password = hash_password(password)
            query = "SELECT user_id FROM users WHERE username = %s AND password = %s"
            result = self.db.fetch_one(query, (username, hashed_password))
            return result is not None
        except Exception as e:
            print(f"Login error: {e}")
            return False
    
    def register_user(self, username, password, email, custom_id):
        try:
            if not all([username, password, email, custom_id]):
                return False, "Барлық өрістерді толтырыңыз"
            
            if not validate_email(email):
                return False, "Жарамсыз email форматы"
                
            if not validate_custom_id(custom_id):
                return False, "ID 4-6 немесе 8-16 таңбадан тұруы керек"
            
            if len(password) < 8 or len(password) > 16:
                return False, "Құпия сөз 8-16 таңбадан тұруы керек"
                
            hashed_password = hash_password(password)
            
            query = "SELECT user_id FROM users WHERE username = %s"
            if self.db.fetch_one(query, (username,)):
                return False, "Бұл пайдаланушы аты бос емес"
            
            query = "SELECT user_id FROM users WHERE email = %s"
            if self.db.fetch_one(query, (email,)):
                return False, "Бұл email тіркелген"
            
            query = "SELECT user_id FROM users WHERE custom_id = %s"
            if self.db.fetch_one(query, (custom_id,)):
                return False, "Бұл ID тіркелген"
            
            query = """
            INSERT INTO users (username, password, email, custom_id)
            VALUES (%s, %s, %s, %s)
            """
            if self.db.execute_query(query, (username, hashed_password, email, custom_id)):
                return True, "Тіркелу сәтті аяқталды"
            return False, "Деректер қорына қосу кезінде қате"
            
        except Exception as e:
            print(f"Registration error: {e}")
            return False, "Тіркелу кезінде қате орын алды"
    
    def verify_email(self, email):
        try:
            query = "SELECT user_id FROM users WHERE email = %s"
            result = self.db.fetch_one(query, (email,))
            return result is not None
        except Exception as e:
            print(f"Email verification error: {e}")
            return False
    
    def update_password(self, email, new_password):
        try:
            if len(new_password) < 8 or len(new_password) > 16:
                return False
            hashed_password = hash_password(new_password)
            query = "UPDATE users SET password = %s WHERE email = %s"
            return self.db.execute_query(query, (hashed_password, email))
        except Exception as e:
            print(f"Password update error: {e}")
            return False