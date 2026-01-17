# Hash Functions and SHA-256

Hashing is a cryptographic technique used to transform data into a fixed-size value called a hash.  
Unlike encryption, hashing is a one-way process and cannot be reversed.

SHA-256 is one of the most widely used secure hash algorithms.  
It produces a 256-bit hash value regardless of the input size.

## Properties of Cryptographic Hash Functions

A secure hash function should satisfy the following properties:

- **Deterministic**  
  The same input always produces the same hash.

- **Fixed Output Length**  
  The output size is always the same.

- **Fast Computation**  
  Hashing should be efficient to compute.

- **Pre-image Resistance**  
  It should be computationally infeasible to recover the original input from the hash.

- **Collision Resistance**  
  It should be computationally infeasible to find two different inputs that produce the same hash.

## How Hashing Works

1. Input data of any size is provided.  
2. The hash function processes the data.  
3. A fixed-length hash value is generated.  
4. Any small change in the input results in a completely different hash.

## Common Use Cases

- Password storage  
- Data integrity verification  
- Digital signatures  
- Message authentication

## Hashing vs Encryption

- Hashing is one-way and irreversible.  
- Encryption is reversible using a key.  
- Hashing does not use keys.  
- Encryption requires keys.

## Relation Between Hashing and RSA

- RSA does not sign the original message directly.  
- The message is hashed first.  
- The resulting hash is signed using the RSA private key.  
- This approach makes digital signatures more efficient and secure.
