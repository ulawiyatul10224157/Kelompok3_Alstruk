import random

print("=== GAME SUIT GUNTING - BATU - KERTAS ===")
print("Pilih salah satu: gunting, batu, atau kertas.\n")

opsi = ["gunting", "batu", "kertas"]

player = input("Pilihan kamu: ").lower()

# Validasi input
if player not in opsi:
    print("Pilihan tidak valid! Harus gunting, batu, atau kertas.")
    exit()

komputer = random.choice(opsi)

print(f"Komputer memilih: {komputer}")

# Tentukan pemenang
if player == komputer:
    print("Hasil: SERI!")
elif (player == "gunting" and komputer == "kertas") or \
     (player == "batu" and komputer == "gunting") or \
     (player == "kertas" and komputer == "batu"):
    print("Hasil: KAMU MENANG! ")
else:
    print("Hasil: KAMU KALAH!")