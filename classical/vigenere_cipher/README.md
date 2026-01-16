# Vigenère Cipher

The Vigenère Cipher is an encryption method that uses a series of Caesar Ciphers based on the letters of a keyword.  
It provides more security than a simple Caesar Cipher by applying multiple shifts.

## How it Works
- Choose a keyword (e.g., `KEY`).  
- Each letter of the plaintext is shifted according to the corresponding letter in the keyword.  
- The keyword repeats as needed to match the length of the plaintext.

## Example
- Plaintext: HELLO  
- Keyword: KEY  
- Ciphertext: RIJVS

## How to Use
- Run `vigenere.py` to encrypt or decrypt messages.  
- Use your own keyword to try different results.
