def caesar_cipher(text, shift, encrypt=True):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            # Determine the offset based on encryption or decryption
            if encrypt:
                offset = shift
            else:
                offset = -shift
            
            # Shift the character
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + offset) % 26 + ord('a'))
            elif char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + offset) % 26 + ord('A'))
        else:
            # If the character is not alphabetical, leave it unchanged
            encrypted_text += char
    return encrypted_text

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
        if choice not in ['e', 'd']:
            print("Please enter 'e' for encrypt or 'd' for decrypt.")
            continue
        
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value: "))
        
        if choice == 'e':
            encrypted_message = caesar_cipher(message, shift)
            print("Encrypted message:", encrypted_message)
        else:
            decrypted_message = caesar_cipher(message, shift, encrypt=False)
            print("Decrypted message:", decrypted_message)
        
        another = input("Do you want to perform another operation? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
