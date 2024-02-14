def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption and Decryption")
    message = input("Enter the message: ")

    while True:
        operation = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
        if operation in ['E', 'D']:
            break
        else:
            print("Invalid input. Please enter 'E' for encrypt or 'D' for decrypt.")

    while True:
        try:
            shift = int(input("Enter the shift value (an integer): "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    if operation == 'E':
        result = encrypt(message, shift)
        print("\nEncrypted Message:", result)
    else:
        result = decrypt(message, shift)
        print("\nDecrypted Message:", result)

if __name__ == "__main__":
    main()
