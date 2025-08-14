import tkinter as tk

def ekle_deger(deger):
    mevcut = ekran.get()
    ekran.delete(0, tk.END)
    ekran.insert(0, mevcut + str(deger))

def temizle():
    ekran.delete(0, tk.END)

def hesapla():
    try:
        mevcut = ekran.get()
        sonuc = eval(mevcut)
        ekran.delete(0, tk.END)
        ekran.insert(0, sonuc)
    except:
        ekran.delete(0, tk.END)
        ekran.insert(0, "Hata")

def klavye_giris(event):
    # Sayılar ve operatörler
    if event.char.isdigit() or event.char in "+-*/.":
        ekle_deger(event.char)
    # Enter tuşu = hesapla
    elif event.keysym == "Return":
        hesapla()
    # Backspace = silme
    elif event.keysym == "BackSpace":
        mevcut = ekran.get()
        ekran.delete(0, tk.END)
        ekran.insert(0, mevcut[:-1])
    # Esc tuşu = temizle
    elif event.keysym == "Escape":
        temizle()

# Ana pencere
pencere = tk.Tk()
pencere.title("Hesap Makinesi")

# Ekran
ekran = tk.Entry(pencere, width=16, font=('Arial', 24), borderwidth=5)
ekran.grid(row=0, column=0, columnspan=4)

# Klavye olayını pencereye bağla
pencere.bind("<Key>", klavye_giris)

# Butonlar
butonlar = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in butonlar:
    if text == '=':
        btn = tk.Button(pencere, text=text, padx=20, pady=20, command=hesapla)
    elif text == 'C':
        btn = tk.Button(pencere, text=text, padx=20, pady=20, command=temizle)
    else:
        btn = tk.Button(pencere, text=text, padx=20, pady=20, command=lambda t=text: ekle_deger(t))
    
    btn.grid(row=row, column=col)

pencere.mainloop()
