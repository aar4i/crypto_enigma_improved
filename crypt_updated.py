# Fernet module is imported from the 
# cryptography package
from cryptography.fernet import Fernet

# create function for crypto machine
def enigma():
    # create key string
    key = Fernet.generate_key()
    # value of key is assigned to a variable
    f = Fernet(key)
    # user input 'the message' and mod'
    msg = input("write your secret code here: ")
    mode = input("Write (e) for encrypte, decrypte is by default. ")
    # we encrypt a message here
    token = f.encrypt(msg.encode())
    # run encode or decode
    if mode == 'e':
        # return the ciphertext
        return token
    else:
        # we decrypt a msg over here
        decrypted_msg = (f.decrypt(token)).decode()
        # return the plaintext
        return decrypted_msg
print(enigma())