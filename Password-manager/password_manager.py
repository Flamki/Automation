# Key + Password + text_to_encrypt = random_text     (Encryption)
# random_text + key + password = text_to_encrypt     (Decryption)
from cryptography.fernet import Fernet

master_passw = input("Enter a master password -> ")

''' 
def write_value():
    key = Fernet.generate_key()
    with open("key.key",'wb') as key_file:
        key_file.write(key)
'''



def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():  # Corrected line
            data = line.rstrip()
            org, user, password = data.split("|")
            print(f"organization: {org} | user: {user} | password: {password}")


def add():
    app = input("Enter the name of website/application -> ")
    email_id = input("Enter your ID -> ")
    passw = input("Enter your password -> ")
    with open("password.txt", "a") as f:
        f.write(f"{app} | {email_id} | {passw}\n")


while True:
    user_input = input("Would you like to view passwords, add a password, or quit (view|add|q) -> ").lower()
    if user_input == 'q':
        break  # It's better to use break instead of quit() for normal loop termination
    elif user_input == 'view':
        view()
    elif user_input == 'add':
        add()
    else:
        print("Invalid option, please choose 'view', 'add', or 'q' to quit.")
        continue
