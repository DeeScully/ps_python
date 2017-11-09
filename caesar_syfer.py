import string

def cipher():
    msg = input('Type in the message to encrypt here> ').lower()
    shift = int(input('Type in an integer as an encryption key> '))
    ltr_map = string.ascii_lowercase
    encrypted_str = ''

    for i in msg:
        if i == ' ':
            encrypted_str += ' '
        else:
            ltr_location = ltr_map.find(i)
            new_location = (ltr_location + shift) % 26
            encrypted_str += ltr_map[new_location]

    return encrypted_str



def decipher():
    msg = input('Type in the message to decrypt here> ').lower()
    shift = int(input('Type in the encryption key> '))
    ltr_map = string.ascii_lowercase
    decrypted_str = ''

    for i in msg:
        if i == ' ':
            decrypted_str += ' '
        else:
            ltr_location = ltr_map.find(i)
            new_location = (ltr_location - shift) % 26
            decrypted_str += ltr_map[new_location]

    return decrypted_str

print(cipher())
print(decipher())
