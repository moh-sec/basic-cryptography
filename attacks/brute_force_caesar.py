from typing import Dict


def brute_force_caesar(ciphertext: str) -> Dict[int, str]:
    """
    Try all possible Caesar cipher shifts (1–25) on the given ciphertext.

    Args:
        ciphertext (str): Encrypted message using Caesar cipher.

    Returns:
        Dict[int, str]: Mapping between shift value and decrypted text.
    """
    results: Dict[int, str] = {}

    for shift in range(1, 26):
        decrypted = []

        for char in ciphertext:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                decrypted_char = chr((ord(char) - base - shift) % 26 + base)
                decrypted.append(decrypted_char)
            else:
                decrypted.append(char)

        results[shift] = "".join(decrypted)

    return results


if __name__ == "__main__":
    message = "Khoor zruog"
    attempts = brute_force_caesar(message)

    for shift, text in attempts.items():
        print(f"[Shift {shift:2}] {text}")

