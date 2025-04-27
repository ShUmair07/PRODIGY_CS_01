def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine the base (A=65, a=97)
            base = ord('A') if char.isupper() else ord('a')
            # Shift the character
            shifted = (ord(char) - base + shift * mode) % 26
            result += chr(base + shifted)
        else:
            # Non-alphabetic characters (e.g., spaces, numbers) remain unchanged
            result += char
    return result
def main():
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (1-25): "))
    mode = input("Encrypt (E) or Decrypt (D)? ").upper()

    if mode == 'E':
        encrypted = caesar_cipher(message, shift, 1)
        print(f"Encrypted message: {encrypted}")
    elif mode == 'D':
        decrypted = caesar_cipher(message, shift, -1)
        print(f"Decrypted message: {decrypted}")
    else:
        print("Invalid mode. Choose 'E' or 'D'.")

if __name__ == "__main__":
    main()