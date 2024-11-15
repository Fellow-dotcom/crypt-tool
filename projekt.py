import argparse
from cryptography.fernet import Fernet
import pyfiglet

title = pyfiglet.figlet_format("JellyCrypt", font="slant")
print(title)


ascii_art = """
⠀⠀⠀⠀⡴⠂⢩⡉⠉⠉⡖⢄⠀
⠀⠀⠀⢸⠪⠄⠀⠀⠀⠀⠐⠂⢧
⠀⠀⠀⠙⢳⣢⢬⣁⠀⠛⠀⠂⡞
⠀⣀⡤⢔⠟⣌⠷⠡⢽⢭⠝⠭⠁
⡸⣡⠴⡫⢺⠏⡇⢰⠸⠘⡄⠀⠀
⡽⠁⢸⠀⢸⡀⢣⠀⢣⠱⡈⢦⠀
⡇⠀⠘⣆⠀⢣⡀⣇⠈⡇⢳⠀⢣
⠰⠀⠀⠘⢆⠀⠑⢸⢀⠃⠈⡇⢸
⠀⠀⠀⠀⠈⠣⠀⢸⠀⠀⢠⠇⠀
⠀⠀⠀⠀⠀⠀⢠⠃⠀⠔⠁⠀⠀
"""


bold_text = "\033[1mEncrypt your secrets with JellyCrypt - It's as safe as the depths of the ocean.\033[0m"

print(ascii_art)
print(bold_text, "\n\n")



parser = argparse.ArgumentParser(
    description=(
        "Cryptography tool \n\n"
        "Observe: You can choose your own custom name for the key file instead of the following example: ultrasecret.key \n \n"
        "Example commands: \n \n"
        "Generate: python projekt.py -o generate ultrasecret \n \n"
        "Encrypt: python projekt.py -o encrypt -f rockyou.txt ultrasecret.key \n \n"
        "Decrypt: python project.py -o decrypt -f rockyou.txt.enc ultrasecret.key \n \n"
        "Finally: remember to include the new file extensions that is added to the filename when decrypting \n \n"),
formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument("key_filename", type=str, help="Type the name of your new key without file extension")
parser.add_argument("-o","--operation", choices= ["generate","encrypt","decrypt"],
    help=
        "Choose operation: generate, encrypt or decrypt")
parser.add_argument("-f","--filename", type= str,
    help=
        "Provide the name of the file you wish to encrypt or decrypt, and name of the generated key (with .key as file extension)")
args = parser.parse_args()


def generate_key(key_filename):
    if not key_filename.endswith(".key"):
        key_filename += ".key"
        
    key = Fernet.generate_key()
    
    with open(f"{key_filename}", 'wb') as key_file:
        key_file.write(key)
    print(f"key was generated and saved in {key_filename}" )

def load_key(key_filename):
    with open(f"{key_filename}", 'rb') as key_file:
        return key_file.read()  

def encrypt_file(filename, key_filename):
    key = load_key(key_filename)
    object_key = Fernet(key)
    with open(filename, 'rb') as original_file:
        original = original_file.read()
   
    encrypted = object_key.encrypt(original)
    with open(f"{filename}.enc", 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    print(f"The file: {filename} was encrypted and saved as {filename}.enc") 

def decrypt_file(filename, key_filename):   

    key = load_key(key_filename)
    object_key = Fernet(key)
    
    with open(filename, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
        
    decrypted = object_key.decrypt(encrypted)
    decrypted_file_name = "decrypted_" + filename [:-4] #[:-4] betyder att vi tar bort .enc och döper om filen så den inte skriver över original
    
    with open(decrypted_file_name, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    print(f"The file: '{filename}' was decrypted and saved as '{decrypted_file_name}'")
    

try:
    if args.operation == "generate":
        generate_key(args.key_filename)

    elif args.operation == "encrypt":
         encrypt_file(args.filename, args.key_filename)
       
    elif args.operation == "decrypt":
        decrypt_file(args.filename, args.key_filename)
    
except FileNotFoundError:
    print("The key or file does not exist, try again with a valid key or file name")
                








