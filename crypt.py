# make a cryptomachine
# we can enter a message
# we can encrypte and decrypte a message
# and then we get a plain text message
# we send it back into the same machine to get decrypted message back

# create fucntion 4 crypto machine
def enigma():
    # create keys string
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    # autogenerate the values string by offsetting original string
    values = keys[::-1]
    # create two dictionaries
    dict_encrypt = dict(zip(keys,values))
    #print(f'encrypted dict:{dict_encrypt}')
    dict_decrypt = dict(zip(values,keys))
    #print(f'encrypted dict:{[dict_decrypt]}')
    # user input 'the message' and mode
    msg = input("write your secret code here: ")
    mode = input("Write (e) for encrypte, decrypte is by default. ")
    # run encode or decode
    if mode == 'e':
        # we encrypt a message here
        new_msg = ''.join([dict_encrypt[letter] for letter in msg.lower()])
        # and we print it here on the next line
    else:
        # we decrypt a msg over here
        new_msg = ''.join([dict_decrypt[letter] for letter in msg.lower()])
    # return result
    return new_msg.capitalize()
    # clean and beautify the code 
print(enigma())