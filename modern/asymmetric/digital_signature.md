# Digital Signature Concept

A digital signature is a cryptographic mechanism used to verify the authenticity  
and integrity of a message, document, or data.

Digital signatures are built using asymmetric cryptography together with cryptographic hash functions.

## What Problems Digital Signatures Solve

Digital signatures provide three main guarantees:

- **Authentication**  
  Verifies the identity of the sender.

- **Integrity**  
  Ensures that the data has not been modified.

- **Non-repudiation**  
  Prevents the sender from denying that the message was sent.

## How Digital Signatures Work

1. The original message is hashed using a cryptographic hash function.  
2. The resulting hash is encrypted using the sender’s private key.  
3. This encrypted hash becomes the digital signature.  
4. The receiver hashes the received message.  
5. The receiver decrypts the signature using the sender’s public key.  
6. If both hash values match, the signature is considered valid.

## Role of Hash Functions

- Hashing reduces the size of the data being signed.  
- Any small change in the message results in a completely different hash.  
- Common hash algorithms include SHA-256.

## Role of Asymmetric Cryptography

- The private key is used to create the signature.  
- The public key is used to verify the signature.  
- Only the owner of the private key can generate a valid signature.

## Common Use Cases

- Software distribution  
- Secure email  
- HTTPS and TLS certificates  
- Blockchain transactions
