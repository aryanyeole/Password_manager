1. Master Key Security:
  The user must log in using a master key to access the password manager.
  The master key is hashed using SHA-256 and stored securely in the master.key file.

2. Password Encryption:
  Passwords are encrypted using the cryptography library's Fernet encryption mechanism.
  The encryption key is saved in a key.key file and used for both encryption and decryption.

3. Persistent Storage:
  Passwords are saved in a file named passwords.txt.
  The master key and encryption key files ensure security across program runs.

4. User Authentication:
  If the master key is incorrect, access is denied, and the program exits.
