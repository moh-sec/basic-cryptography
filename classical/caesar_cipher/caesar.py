def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift = key % 26
            if char.isupper():
                ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key):
    return encrypt(ciphertext, -key)

def main():
    message = input("Enter your message: ")
    key = int(input("Enter the key (shift number): "))
    
    encrypted = encrypt(message, key)
    print("Encrypted message:", encrypted)
    
    decrypted = decrypt(encrypted, key)
    print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()

