#algortima hitung huruf vokal
#s = string
# vokal = dictionary
#jumlah vokal = integer
#c = karakter
def hitung_vokal(s):
    vokal = {"a": 0, "i": 0, "u": 0, "e": 0, "o": 0}
    jumlah_vokal = 0
    for c in s:
        if c.lower() in vokal:
            vokal[c.lower()] += 1
            jumlah_vokal += 1
    return jumlah_vokal, vokal
#tampilkan panjang teks dan jumlah vokal
s = input("Masukkan teks: ")
jumlah_vokal, vokal = hitung_vokal(s)
print(f"Panjang teks: {len(s)}")
print(f"Jumlah vokal: {jumlah_vokal}")
print("jumlah masing-masing vokal:")
for huruf, count in vokal.items():
    print(f"  {huruf}: {count}")

hitung_vokal(s)
#code writted by lyvo
