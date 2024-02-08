from cryptography.fernet import Fernet

# generate key
key = Fernet.generate_key()
f = Fernet(key)
# user_input
user_input = input("enter a string to encrypt -> ")
# converting user_input string to bytes, then encrypt
token = f.encrypt(user_input.encode())
print(token)

#decrypt the tokein
real_value = f.decrypt(token)
print(real_value)