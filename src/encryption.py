from cryptography.fernet import Fernet


class Encryption:
    
    def __init__(self):
        # Stores the encryption key and Fernet object
        self.key = None
        self.cipher = None


    def create_key(self, path):
        
        self.key = Fernet.generate_key()

        # Save the key as bytes
        with open(path, "wb") as file:
            file.write(self.key)
            
            
    def load_key(self, path):
        
        with open(path, "rb") as file:
            self.key = file.read()

        # Create a Fernet object using the loaded key
        self.cipher = Fernet(self.key)


    def encrypt(self, text):
        # Fernet encrypts bytes, not strings
        text = text.encode()
        return self.cipher.encrypt(text)


    def decrypt(self, encrypted_text):
        # Decrypt bytes and convert back to a string
        decrypted = self.cipher.decrypt(encrypted_text)
        return decrypted.decode()