alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
block = str(input("type encode if you want to encrypt and decode if you want to decrypt"))
text = input('type your message: ').lower()
shift = int(input("type the shift number: "))
def encrypt(plain_text, shift_amount):
    cipher_text = ''
    for letter in  text:
        position= alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(cipher_text)

def decrypt(plain_text,shift_amount):
    cipher_text = ''
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(cipher_text)

if block == "decode":
    decrypt(plain_text=text, shift_amount=shift)
elif block == 'encode':
    encrypt(plain_text=text, shift_amount=shift)






