# Caesar Cipher Program

import string

# Key Generation
key = int(input("Enter Caesar Cipher Key (1-25): "))

# Encryption Function
def encrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            shift = key % 26

            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char

    return result


# Decryption Function
def decrypt(cipher, key):
    result = ""

    for char in cipher:
        if char.isalpha():
            shift = key % 26

            if char.isupper():
                result += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            result += char

    return result


# Input
plaintext = input("Enter Plain Text: ")

# Encryption
ciphertext = encrypt(plaintext, key)

# Decryption
decrypted_text = decrypt(ciphertext, key)

# Output
print("\n--- Caesar Cipher ---")
print("Key:", key)
print("Encrypted Text:", ciphertext)
print("Decrypted Text:", decrypted_text)