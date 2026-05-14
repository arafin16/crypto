# Playfair Cipher Program

import string

# Generate Key Matrix
def generate_key_matrix(key):

    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for char in key:
        if char not in used and char.isalpha():
            used.add(char)
            matrix.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used:
            used.add(char)
            matrix.append(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]


# Find Position
def find_position(matrix, char):

    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col


# Prepare Plaintext
def prepare_text(text):

    text = text.upper().replace("J", "I")
    text = ''.join(filter(str.isalpha, text))

    prepared = ""
    i = 0

    while i < len(text):

        a = text[i]

        if i + 1 < len(text):
            b = text[i + 1]
        else:
            b = "X"

        if a == b:
            prepared += a + "X"
            i += 1
        else:
            prepared += a + b
            i += 2

    if len(prepared) % 2 != 0:
        prepared += "X"

    return prepared


# Encryption
def encrypt(text, matrix):

    text = prepare_text(text)
    cipher = ""

    for i in range(0, len(text), 2):

        a, b = text[i], text[i+1]

        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        # Same Row
        if row1 == row2:
            cipher += matrix[row1][(col1 + 1) % 5]
            cipher += matrix[row2][(col2 + 1) % 5]

        # Same Column
        elif col1 == col2:
            cipher += matrix[(row1 + 1) % 5][col1]
            cipher += matrix[(row2 + 1) % 5][col2]

        # Rectangle Rule
        else:
            cipher += matrix[row1][col2]
            cipher += matrix[row2][col1]

    return cipher


# Decryption
def decrypt(cipher, matrix):

    plain = ""

    for i in range(0, len(cipher), 2):

        a, b = cipher[i], cipher[i+1]

        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        # Same Row
        if row1 == row2:
            plain += matrix[row1][(col1 - 1) % 5]
            plain += matrix[row2][(col2 - 1) % 5]

        # Same Column
        elif col1 == col2:
            plain += matrix[(row1 - 1) % 5][col1]
            plain += matrix[(row2 - 1) % 5][col2]

        # Rectangle Rule
        else:
            plain += matrix[row1][col2]
            plain += matrix[row2][col1]

    return plain


# Main Program
key = input("Enter Playfair Key: ")

matrix = generate_key_matrix(key)

print("\nPlayfair Key Matrix:")
for row in matrix:
    print(row)

plaintext = input("\nEnter Plain Text: ")

ciphertext = encrypt(plaintext, matrix)

decrypted = decrypt(ciphertext, matrix)

print("\n--- Playfair Cipher ---")
print("Encrypted Text:", ciphertext)
print("Decrypted Text:", decrypted)