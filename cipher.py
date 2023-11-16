import argparse
#python cipher.py -m caesar -t "texte à chiffrer" -s 3
#python cipher.py -m vigenere -t "texte à chiffrer" -k "clé"
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char
    return result

def vigenere_cipher(text, key):
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            key_shift = ord(key[key_index % len(key)].lower()) - ord('a')
            shifted_char = caesar_cipher(char, key_shift)
            result += shifted_char
            key_index += 1
        else:
            result += char
    return result

def main():
    parser = argparse.ArgumentParser(description='Command Line Cipher')
    parser.add_argument('-m', '--mode', choices=['caesar', 'vigenere'], required=True, help='Cipher mode (caesar or vigenere)')
    parser.add_argument('-t', '--text', required=True, help='Text to encrypt/decrypt')
    parser.add_argument('-s', '--shift', type=int, help='Shift value for Caesar cipher')
    parser.add_argument('-k', '--key', help='Key for Vigenere cipher')

    args = parser.parse_args()

    if args.mode == 'caesar':
        if args.shift is None:
            parser.error("Shift value is required for Caesar cipher")
        result = caesar_cipher(args.text, args.shift)
    else:
        if args.key is None:
            parser.error("Key is required for Vigenere cipher")
        result = vigenere_cipher(args.text, args.key)

    print("Result:", result)

if __name__ == '__main__':
    main()