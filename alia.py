import random

def undian_berhadiah():
    peserta = ["Ali", "Budi", "Citra", "Dewi", "Eko", "Fani", "Gita", "Hadi"]
    hadiah = ["TV", "Smartphone", "Laptop", "Sepeda", "Voucher Belanja"]

    print("=== UNDIAN BERHADIAH ===")
    print("Peserta:", peserta)
    print("Hadiah:", hadiah)
    print("\nPENGUMUMAN PEMENANG:")

    random.shuffle(hadiah)
    pemenang = random.sample(peserta, len(hadiah))

    for i, (nama, hadiah_didapat) in enumerate(zip(pemenang, hadiah), 1):
        print(f"{i}. {nama} memenangkan: {hadiah_didapat}")

undian_berhadiah()