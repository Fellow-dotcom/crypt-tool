# Welcome to JellyCrypt!

JellyCrypt is a secure tool for file encryption and decryption. It utilizes Fernet from the cryptography library to safely protect any file you wish. A .txt file and a jpg-file has been added to the repository, so you can easily try the tool.

### Features:
Generate key: choose a name for your key and generate it. It is saved as a .key file.
Encrypt file: Encrypt a given file using the generated key.
Decrypt file: Decrypt a given file using the generated key.

### Commands:
To generate a key use the following command: python projekt.py -o generate your_key_name
To encrypt a file use the following command: python projekt.py -o encrypt -f filename your_key_name.key
To decrypt a file use the following command: python projekt.py -o decrypt -f filename.enc your_key_name.key

### Example commands: 
Generate: python projekt.py -o generate secret_key
Encrypt: python projekt.py -o encrypt -f picture.jpg secret_key.key
Decrypt: python project.py -o decrypt -f picture.jpg.enc secret_key.key
