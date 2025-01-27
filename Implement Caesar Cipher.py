def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts a given text using the Caesar Cipher algorithm.

    Parameters:
        text (str): The input text to be encrypted or decrypted.
        shift (int): The number of positions to shift the characters.
        mode (str): The mode of operation, 'encrypt' or 'decrypt'.

    Returns:
        str: The resulting encrypted or decrypted text.
    """
    result = ""
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Determine if the character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around within the alphabet range
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    return result


def main():
    print("Caesar Cipher Program")
    while True:
        print("\nOptions:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        choice = input("Choose an option (1/2/3): ")

        if choice == '1' or choice == '2':
            message = input("Enter the message: ")
            shift = int(input("Enter the shift value (integer): "))
            mode = 'encrypt' if choice == '1' else 'decrypt'
            result = caesar_cipher(message, shift, mode)
            print(f"\nResult ({mode}ed text): {result}")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
