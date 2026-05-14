# Brute Force Attack on Caesar Cipher

def brute_force(ciphertext):

    for key in range(1, 26):

        decrypted = ""

        for char in ciphertext:

            if char.isalpha():

                if char.isupper():
                    decrypted += chr((ord(char) - 65 - key) % 26 + 65)
                else:
                    decrypted += chr((ord(char) - 97 - key) % 26 + 97)

            else:
                decrypted += char

        print(f"Key {key}: {decrypted}")


# Input Cipher Text
cipher = input("Enter Cipher Text: ")

print("\n--- Brute Force Results ---")
brute_force(cipher)