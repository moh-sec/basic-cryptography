
def encrypt(plaintext, keyword):
    ciphertext = ""
    keyword_length = len(keyword)
    keyword_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(keyword[keyword_index % keyword_length].upper()) - 65
            if char.isupper():
                ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
            keyword_index += 1
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, keyword):
    plaintext = ""
    keyword_length = len(keyword)
    keyword_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(keyword[keyword_index % keyword_length].upper()) - 65
            if char.isupper():
                plaintext += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                plaintext += chr((ord(char) - 97 - shift) % 26 + 97)
            keyword_index += 1
        else:
            plaintext += char
    return plaintext

def main():
    message = input("Enter your message: ")
    keyword = input("Enter the keyword: ")

    encrypted = encrypt(message, keyword)
    print("Encrypted message:", encrypted)

    decrypted = decrypt(encrypted, keyword)
    print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()
