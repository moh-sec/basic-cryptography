import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend


def generate_key() -> bytes:
    # Create a random 256-bit key for AES
    return os.urandom(32)


def generate_iv() -> bytes:
    # Generate a random IV (AES block size is 16 bytes)
    return os.urandom(16)


def encrypt(plaintext: bytes, key: bytes) -> tuple:
    # Encrypt data using AES in CBC mode

    iv = generate_iv()

    # Add padding so the data fits AES block size
    padder = padding.PKCS7(128).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()

    # Set up the AES cipher
    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
        backend=default_backend()
    )

    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    return iv, ciphertext


def decrypt(ciphertext: bytes, key: bytes, iv: bytes) -> bytes:
    # Decrypt data that was encrypted with AES-CBC

    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
        backend=default_backend()
    )

    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Remove padding after decryption
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext


if __name__ == "__main__":
    key = generate_key()
    message = b"Hello symmetric cryptography!"

    iv, ciphertext = encrypt(message, key)
    decrypted_message = decrypt(ciphertext, key, iv)

    print("Original Message :", message)
    print("Encrypted Message:", ciphertext)
    print("Decrypted Message:", decrypted_message)

