print("=== GAME TEBAK ANGKA ===")
print("Aku sudah memilih angka dari 1 sampai 20.")
print("Coba tebak ya!\n")

angka_rahasia = random.randint(1, 20)
percobaan = 0

while True:
    tebak = int(input("Masukkan tebakanmu: "))
    percobaan += 1

    if tebak < angka_rahasia:
        print("Terlalu kecil!")
    elif tebak > angka_rahasia:
        print("Terlalu besar!")
    else:
        print(f"Benar! Angkanya adalah {angka_rahasia}.")
        print(f"Kamu menebak dalam {percobaan} percobaan.")
        break