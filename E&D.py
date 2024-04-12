alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position > 25:
            new_position -= 26
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encrypted message is: {cipher_text}")

plain_text = input("Enter Your Message: ").lower()
shift = int(input("Enter your shift Amount: "))
encrypt(plain_text, shift)
def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"The Decrypted Message is: {plain_text}")

cipher_text = input("Enter the Encrypted Message to be Decrypted: ").lower()
decrypt(cipher_text, shift)

