from cryptography.fernet import Fernet
import os
from tkinter import filedialog
from tkinter import *
import threading

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
                commentsvar.set("Encrypted " + filepath)
        commentsvar.set("Encrypted all successfully")
        commentsvar.set("Your safe key is " + key.decode('utf-8') + "  Please keep this safe or will not be able to decrypt your files")
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
        commentsvar.set("key loaded successfully")
        for root,directories,files in os.walk(dirpath):
            for name in files:
                filepath = os.path.join(root, name)
                decrypt(filepath,key)
                commentsvar.set("Decrypted " + filepath)
        commentsvar.set("Decrypted all Successfully")
    except Exception as e:
        print(e)

dirpath = r'Paste your Directory path here'

# encryptdirs(dirpath)
# decryptdirs(dirpath)

def browse_button():
    global folder_path
    path = filedialog.askdirectory()
    folder_path.set(path)
    
    
def encryptdirsgui():
    global folder_path
    strdirpath = folder_path.get()
    try:
        # encryptdirs(strdirpath)
        encryptThread = threading.Thread(target=encryptdirs, args=(strdirpath,))
        encryptThread.start()
        # thread.start_new_thread(encryptdirs,(strdirpath))
    except Exception as e:
        print(e)

def decryptdirsgui():
    global folder_path
    strdirpath = folder_path.get()
    try:
        # decryptdirs(strdirpath)
        decryptThread = threading.Thread(target=decryptdirs, args=(strdirpath,))
        decryptThread.start()
    except Exception as e:
        print(e)

root = Tk()
root.geometry('700x300') 
folder_path = StringVar()
commentsvar = StringVar()


browseBtn = Button(text="Browse drive or Folder to Encrypt/Decrypt", command=browse_button)
browseBtn.grid(row=0, column=10)

pathLabel = Label(master=root,textvariable=folder_path)
pathLabel.grid(row=2, column=10)

encryptBtn = Button(text="Encrypt", command=encryptdirsgui)
encryptBtn.grid(row=4, column=10)

decryptBtn = Button(text="Decrypt", command=decryptdirsgui)
decryptBtn.grid(row=6, column=10)

commentsLabel = Label(master=root,textvariable=commentsvar)
commentsLabel.grid(row = 8,column =10)

mainloop()
