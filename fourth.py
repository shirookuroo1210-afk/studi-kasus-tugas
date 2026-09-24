#algoritma caesar cipher
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result
#main program "algoritma" -> text
#tampilkan plain text
#tampilkan shift pattern
#tampilkan cipher text
text = input("Masukkan teks: ")
shift = int(input("Masukkan jumlah pergeseran (shift): "))
cipher_text = caesar_cipher(text, shift)
print("Plain text:", text)
print("Shift pattern:", shift)
print("Cipher text:", cipher_text)

caesar_cipher(text, shift)