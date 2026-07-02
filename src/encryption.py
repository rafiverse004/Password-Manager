from cryptography.fernet import Fernet

"""
Think of Fernet as a machine that knows how to:

Encrypt data
Decrypt data

"""

class Encryption:
    
    def __init__(self):
        self.key = None
        self.cipher = None
    """
    self.key is the key of a car
    self.cipher is the car
    """
    
    def create_key(self, path):
        self.key = Fernet.generate_key()
        
        with open(path, 'wb') as file:
            file.write(self.key)
    """
    Generate a random encryption key
    Open the file in binary write mode (wb)
    Write the key into the file
    
    """
    
    def load_key(self, path):
        with open(path, 'rb') as file:
            self.key = file.read()
    
        self.cipher = Fernet(self.key)
        
    """
    Open the file binary read mode (rb)
    put the value in key
    cipher object will encrypt and decrypt the key
    
    """
    
    def encrypt(self, text):
        text = text.encode()    # String to byte
        return self.cipher.encrypt(text)
    
    """
    Fernet.encrypt() does not accept Python strings
    we convert text string to byte
    We return encrypted text
    
    """
    
    def decrypt(self, encrypted_text):
        decrypted = self.cipher.decrypt(encrypted_text)
        return decrypted.decode()