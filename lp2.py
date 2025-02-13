from cryptography.fernet import Fernet
import os
def gen_key():
    key = Fernet.gen_key()
    with open("secret.key", "wb") as kf:
        kf.write(key)

def load_key():
    return open("secret.key", "rb").read()

def ef(file_name):
    key = load_key()
    fernet = Fernet(key)
    with open(file_name, "rb") as f:
        original = f.read()
    encrypted = fernet.encrypt(original)

    with open(file_name, "wb") as ef:
        ef.write(encrypted)
    print(f"{file_name} has been encrypted.")

def df(file_name):
    key = load_key()
    fernet = Fernet(key)
    with open(file_name, "rb") as ef:
        encrypted = ef.read()
    decrypted = fernet.decrypt(encrypted)

    with open(file_name, "wb") as df:
        df.write(decrypted)
    print(f"{file_name} has been decrypted.")

def main():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a file? (q to quit): ").lower()
        if choice == 'e':
            file_name = input("Enter the file name to encrypt: ")
            if os.path.exists(file_name):
                ef(file_name)
            else:
                print("File does not exist.")
        elif choice == 'd':
            file_name = input("Enter the file name to decrypt: ")
            if os.path.exists(file_name):
                df(file_name)
            else:
                print("File does not exist.")
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please choose 'e', 'd', or 'q'.")

if __name__ == "__main__":
    if not os.path.exists("secret.key"):
        gen_key()
    
    main()
