import hashlib

def sha256_hash(message):
    message_bytes = message.encode()
    hash_object = hashlib.sha256(message_bytes)
    return hash_object.hexdigest()

def main():
    message = input("Enter a message: ")
    hashed = sha256_hash(message)
    print("SHA-256 Hash:", hashed)

if __name__ == "__main__":
    main()

