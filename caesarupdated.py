alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
block = str(input("type encode if you want to encrypt and decode if you want to decrypt"))
text = input('type your message: ').lower()
shift = int(input("type the shift number: "))
end = False
while not end:
 def caesar(plain_text,shift_amount,direction):
    cipher_text = ''
    for letter in text:
        position = alphabet.index(letter)
        if direction == "encode":
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        elif direction == "decode":
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
    print(cipher_text)



 caesar(plain_text=text, shift_amount=shift, direction=block)






