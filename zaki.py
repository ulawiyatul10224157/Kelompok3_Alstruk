import random

print("=== GAME TEBAK ANGKA MISTERI ===")
print("Komputer telah memilih angka dari 1 sampai 10.")
print("Coba tebak angkanya!\n")

angka_rahasia = random.randint(1, 10)

tebak = int(input("Masukkan tebakanmu (1-10): "))

if tebak < 1 or tebak > 10:
    print("Tebakan tidak valid! Masukkan angka 1 sampai 10.")
    exit()

print(f"Komputer memilih: {angka_rahasia}")

if tebak == angka_rahasia:
    print("Hasil: KAMU BENAR! Mantap!")
else:
    print("Hasil: SALAH! Coba lagi lain kali.")