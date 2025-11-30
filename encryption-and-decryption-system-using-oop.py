class Cipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, text):
        result = ""
        for char in text:
            result += chr(ord(char) + self.key)
        return result

    def decrypt(self, encrypted_text):
        result = ""
        for char in encrypted_text:
            result += chr(ord(char) - self.key)
        return result


cipher = Cipher(key=3)

text = "hello"
encrypted = cipher.encrypt(text)
decrypted = cipher.decrypt(encrypted)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
