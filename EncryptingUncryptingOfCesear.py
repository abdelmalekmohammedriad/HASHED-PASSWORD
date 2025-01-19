def caesar_encrypt(text, shift):
    encrypted_text = []
    for ch in text:
        if ch.isalpha():  
            base = ord('a') if ch.islower() else ord('A')
            encrypted_text.append(chr((ord(ch) - base + shift) % 26 + base))
        elif ch.isdigit():  
            encrypted_text.append(chr((ord(ch) - ord('0') + shift) % 10 + ord('0')))
        else:  
            encrypted_text.append(ch)
    return ''.join(encrypted_text)

def caesar_uncrypt(text, shift):
    decrypted_text = []
    for ch in text:
        if ch.isalpha(): 
            base = ord('a') if ch.islower() else ord('A')
            decrypted_text.append(chr((ord(ch) - base - shift) % 26 + base))
        elif ch.isdigit():  
            decrypted_text.append(chr((ord(ch) - ord('0') - shift) % 10 + ord('0')))
        else:  
            decrypted_text.append(ch)
    return ''.join(decrypted_text)

def main():
    while True:
        text = input("Enter the text you want to encrypt: ")
        shift = int(input("Enter the shift value: "))

        encrypted_text = caesar_encrypt(text, shift)
        print(f"Encrypted text: {encrypted_text}")

        decrypted_text = caesar_uncrypt(encrypted_text, shift)
        print(f"Original text: {decrypted_text}")

        continue_choice = input("Do you want to perform another operation? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            break

if __name__ == "__main__":
    main()
