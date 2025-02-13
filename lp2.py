from cryptography.fernet import Fernet
import os

# Function to generate a key and save it to a file
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Function to load the key from a file
def load_key():
    return open("secret.key", "rb").read()

# Function to encrypt a file
def encrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)

    with open(file_name, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(file_name, "wb") as encrypted_file:
        encrypted_file.write(encrypted)

    print(f"{file_name} has been encrypted.")

# Function to decrypt a file
def decrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)

    with open(file_name, "rb") as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(file_name, "wb") as decrypted_file:
        decrypted_file.write(decrypted)

    print(f"{file_name} has been decrypted.")

# Main function to run the tool
def main():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a file? (q to quit): ").lower()
        if choice == 'e':
            file_name = input("Enter the file name to encrypt: ")
            if os.path.exists(file_name):
                encrypt_file(file_name)
            else:
                print("File does not exist.")
        elif choice == 'd':
            file_name = input("Enter the file name to decrypt: ")
            if os.path.exists(file_name):
                decrypt_file(file_name)
            else:
                print("File does not exist.")
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please choose 'e', 'd', or 'q'.")

if __name__ == "__main__":
    # Generate a key if it doesn't exist
    if not os.path.exists("secret.key"):
        generate_key()
    
    main()