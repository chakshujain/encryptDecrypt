from cryptography.fernet import Fernet
import os

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def encrypt(filename, key):
    try:
        f = Fernet(key)
        with open(filename, "rb") as file:
            # read all file data
            file_data = file.read()
        # encrypt data
        encrypted_data = f.encrypt(file_data)
        # write the encrypted file
        with open(filename, "wb") as file:
            file.write(encrypted_data)
    except Exception as e:
        print(e)

def encryptdirs(dirpath):
    try:
        write_key()
        print("New Key Generated")
        key = load_key()
        print("Key Loaded Successfully")
        for root,directories,files in os.walk(dirpath):
            for name in files:
                filepath = os.path.join(root, name)
                encrypt(filepath,key)
                print("Encrypted " + filepath)
        print("Encrypted all successfully")
        print("Your safe key is " + key.decode('utf-8') + "  Please keep this safe or will not be able to decrypt your files")
    except Exception as e:
        print(e)

def decrypt(filename, key):
    try:
        f = Fernet(key)
        with open(filename, "rb") as file:
            # read the encrypted data
            encrypted_data = file.read()
        # decrypt data
        decrypted_data = f.decrypt(encrypted_data)
        # write the original file
        with open(filename, "wb") as file:
            file.write(decrypted_data)
    except Exception as e:
        print(e)

def decryptdirs(dirpath):
    try:
        key = load_key()
        print("key loaded successfully")
        for root,directories,files in os.walk(dirpath):
            for name in files:
                filepath = os.path.join(root, name)
                decrypt(filepath,key)
                print("Decrypted " + filepath)
        print("Decrypted all Successfully")
    except Exception as e:
        print(e)

dirpath = r'Paste your Directory path here'

encryptdirs(dirpath)
# decryptdirs(dirpath)
