import turtle

# --- Setup Jendela ---
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Gambar tiang layang layang")
screen.bgcolor("white")

t = turtle.Turtle()
t.pensize(10) # Ketebalan garis salib
t.pencolor("black") # Warna salib
t.speed(3) # Kecepatan sedang

# Fungsi untuk memindahkan pena tanpa menggambar
def go(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# --- Menggambar tiang layang layang ---

# 1. Garis Vertikal (Tiang)
# Mulai dari sedikit di bawah tengah, ke atas
go(0, -100)
t.setheading(90) # Menghadap ke atas
t.forward(300) # Panjang garis vertikal

# 2. Garis Horizontal (Lengan)
# Pindah ke titik di mana garis horizontal harus berada (sekitar 1/4 dari atas)
go(0, 100) # Titik tengah garis horizontal
t.setheading(180) # Menghadap ke kiri
t.forward(100) # Panjang lengan kiri

# Pindah kembali ke tengah horizontal
go(0, 100)
t.setheading(0) # Menghadap ke kanan
t.forward(100) # Panjang lengan kanan

# Selesai menggambar
t.hideturtle()

# Jaga jendela tetap terbuka
turtle.done()