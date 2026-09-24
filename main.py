angka = [" ", "satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan", "sembilan", "sepuluh", "sebelas"]
#output = string
#n = integer
def terbilang(n):
    if n >=  0 and n <11:
        return angka[n]
    elif n < 20:
        return terbilang(n - 10) + " belas"
    elif n < 100:
        return terbilang(n // 10) + " puluh" + (" " + terbilang(n % 10) if n % 10 != 0 else "")
    elif n < 200:
        return "seratus" + (" " + terbilang(n - 100) if n > 100 else "")
    elif n < 1000:
        return terbilang(n // 100) + " ratus" + (" " + terbilang(n % 100) if n % 100 != 0 else "")
    elif n < 2000:
        return "seribu" + (" " + terbilang(n - 1000) if n > 1000 else "")
    elif n < 1000000:
        return terbilang(n // 1000) + " ribu" + (" " + terbilang(n % 1000) if n % 1000 != 0 else "")
    elif n < 1000000000:
        return terbilang(n // 1000000) + " juta" + (" " + terbilang(n % 1000000) if n % 1000000 != 0 else "")
    elif n < 1000000000000:
        return terbilang(n // 1000000000) + " milyar" + (" " + terbilang(n % 1000000000) if n % 1000000000 != 0 else "")
    elif n < 1000000000000000:
        return terbilang(n // 1000000000000) + " triliun" + (" " + terbilang(n % 1000000000000) if n % 1000000000000 != 0 else "")
    else:
        return "maksimum satu kuadriliun"

input_number = int(input("Masukkan angka: "))
if input_number < 0:
    print("Angka harus lebih besar dari atau sama dengan 0")
else:
    print(terbilang(input_number))
    #code writted by lyvo
