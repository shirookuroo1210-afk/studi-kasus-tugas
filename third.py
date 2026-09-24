# Program enkripsi dan dekripsi kode Morse

def enkripsi(pesan):
    kode_morse = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        ' ': '/'
    }

    cipher = ""
    for huruf in pesan.upper():
        if huruf in kode_morse:
            cipher += kode_morse[huruf] + " "
        else:
            cipher += huruf + " "
    return cipher.strip()


def dekripsi(pesan_morse):
    kode_morse = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
        '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
        '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z',
        '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
        '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
        '/': ' '
    }

    decipher = ""
    for simbol in pesan_morse.split(" "):
        if simbol == "":
            continue
        if simbol in kode_morse:
            decipher += kode_morse[simbol]
        else:
            decipher += simbol
    return decipher


while True:
    pilihan = input("Apakah Anda ingin mengenkripsi atau mendekripsi pesan? (e/d/q): ").lower()

    if pilihan == 'e':
        pesan = input("Masukkan pesan: ")
        print("Cipher:", enkripsi(pesan))
    elif pilihan == 'd':
        pesan_morse = input("Masukkan pesan morse: ")
        print("Decipher:", dekripsi(pesan_morse))
    elif pilihan == 'q':
        print("Program berhenti.")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan 'e' untuk enkripsi, 'd' untuk dekripsi, atau 'q' untuk keluar.")
