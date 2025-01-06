import os
from cryptography.fernet import Fernet
from hashlib import sha256

# Function to generate and save the encryption key
# This key is used for encrypting and decrypting passwords
def write_key():
    key = Fernet.generate_key()
    with open("key.key", 'wb') as key_file:
        key_file.write(key)

# Function to load the encryption key
def load_key():
    if not os.path.exists("key.key") or os.path.getsize("key.key") == 0:
        print("No encryption key found. Generating a new one...")
        write_key()
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

# Function to save the hashed master key
def save_master_key(master_key):
    hashed_key = sha256(master_key.encode()).hexdigest()
    with open("master.key", "w") as f:
        f.write(hashed_key)

# Function to load and verify the master key
def verify_master_key():
    if not os.path.exists("master.key") or os.path.getsize("master.key") == 0:
        print("No valid master key found. Setting up a new master key.")
        master_key = input("Enter a new master key: ")
        save_master_key(master_key)
        print("Master key set successfully!")
    else:
        master_key = input("Enter your master key to login: ")
        with open("master.key", "r") as f:
            stored_hashed_key = f.read()
        if sha256(master_key.encode()).hexdigest() != stored_hashed_key:
            print("Invalid master key. Access denied.")
            exit()
    return master_key

print("Welcome to your password manager")
master_key = verify_master_key()
key = load_key()
fer = Fernet(key)

# Function to view saved passwords
def view():
    if not os.path.exists("passwords.txt"):
        print("No passwords saved yet.")
        return
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

# Function to add a new password
def add():
    name = input('Account name: ')
    pwd = input("Password: ")
    
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

# Main
while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
