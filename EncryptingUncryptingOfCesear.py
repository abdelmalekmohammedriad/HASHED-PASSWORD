def caesar_encrypt(text, shift):
    encrypted_text = []
    for ch in text:
        if ch.isalpha():
            base = ord('a') if ch.islower() else ord('A')
            encrypted_text.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            encrypted_text.append(chr((ord(ch) + shift) % 128))
    return ''.join(encrypted_text)

def caesar_uncrypt(text, shift):
    decrypted_text = []
    for ch in text:
        if ch.isalpha():
            base = ord('a') if ch.islower() else ord('A')
            decrypted_text.append(chr((ord(ch) - base - shift) % 26 + base))
        else:
            decrypted_text.append(ch)
    return ''.join(decrypted_text)

def main():
    text = input("Enter the text that you want to encrypt: ")
    shift = int(input("Enter the shift value: "))

    encrypted_text = caesar_encrypt(text, shift)
    print(f"Encrypted text: {encrypted_text}")

    decrypted_text = caesar_uncrypt(encrypted_text, shift)
    print(f"The original text: {decrypted_text}")

if __name__ == "__main__":
    main()
