# Syadza Oktifani 23343019
daftar_angka = [8, 3, 5, 1, 3, 8, 6, 4, 3]

nilai_maksimum = max(daftar_angka)

print(nilai_maksimum)

ukuran_baru = nilai_maksimum + 1

daftar_baru = [0] * ukuran_baru
print(daftar_baru)

for angka in daftar_angka:
    daftar_baru[angka] += 1

print(daftar_baru)

for i in range(1, len(daftar_baru)):
    daftar_baru[i] = daftar_baru[i] + daftar_baru[i - 1]

print(daftar_baru)

daftar_terurut = [0] * len(daftar_angka)

for i in range(len(daftar_angka) - 1, -1, -1):
    posisi_di_terurut = daftar_baru[daftar_angka[i]] - 1
    daftar_terurut[posisi_di_terurut] = daftar_angka[i]
    daftar_baru[daftar_angka[i]] -= 1

print(daftar_terurut)
