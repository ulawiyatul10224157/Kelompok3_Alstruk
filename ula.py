import random

welcome_message = "WELCOME TO CUYPY GAMES!"
cuypy_position = random.randint(1,4)

print("------------------")
print(f"-- {welcome_message} --")
print("------------------")

nama_user = input("masukkan nama kamu: ")

print(f'''
     Halo {nama_user}! Coba perhatikan goa dibawah ini
      |_| |_| |_| |_|
       ''')

pilihan_user = int(input("Menurut kamu di goa nomor berapa CUYPY berada? [1/2/3/4]: "))

if pilihan_user == cuypy_position:
    print(f"Selamat {nama_user} kamu menang! posisi cuypy ada di goa nomor {cuypy_position} dan pilihanmu adalah goa nomor {pilihan_user}.")
else:
    print(f"KAMU KALAH! cuypy bukan berada disitu, tapi ada di goa nomor {cuypy_position}. Sedangkan kamu memilih goa nomor {pilihan_user}")