#algoritma operasi string
#data_string = string
#jumlah = integer
#indeks = integer
#menghitung jumlah huruf dalam string dan indeks huruf a,A
#jumlah karakter a,A dalam string
def hitung_huruf_a(data_string):
    jumlah = 0
    indeks = []
    for i in range(len(data_string)):
        if data_string[i] == 'a' or data_string[i] == 'A':
            jumlah += 1
            indeks.append(i)
    return jumlah, indeks

#main program
data_string = input("Masukkan string: ")
jumlah, indeks = hitung_huruf_a(data_string)    

print(f"Jumlah huruf 'a' atau 'A' dalam string: {jumlah}")
if jumlah > 0:
    print(f"Indeks huruf 'a' atau 'A' dalam string: {indeks}")

hitung_huruf_a(data_string)
    
#code writted by lyvo
