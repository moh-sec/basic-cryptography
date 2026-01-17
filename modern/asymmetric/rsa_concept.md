# RSA Cryptography Concept

RSA is one of the most well-known asymmetric cryptographic algorithms.  
It is based on the computational difficulty of factoring large prime numbers.

Unlike symmetric encryption, RSA uses two separate keys: a public key and a private key.

## Key Pairs

- **Public Key**  
  Used to encrypt data.  
  Can be shared openly.

- **Private Key**  
  Used to decrypt data.  
  Must be kept secret.

## How RSA Works (High Level)

1. Two large prime numbers are generated.  
2. The primes are multiplied to create a modulus.  
3. The modulus is used to generate both the public and private keys.  
4. Data encrypted with the public key can only be decrypted using the private key.  
5. Data encrypted with the private key can be verified using the public key.

## Why RSA Is Important

- Solves the key exchange problem.  
- Enables secure communication over insecure channels.  
- Used in protocols such as HTTPS, SSL/TLS, and digital signatures.

## Limitations

- Slower than symmetric encryption algorithms.  
- Not suitable for encrypting large amounts of data.  
- Commonly combined with symmetric algorithms such as AES.

## Common Use Cases

- Secure key exchange  
- Digital signatures  
- Authentication

