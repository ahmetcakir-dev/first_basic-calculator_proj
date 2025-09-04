import tkinter as tk
from tkinter import messagebox

def hesapla():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        islem = var.get()
        if islem == "Addition":
            sonuc = num1 + num2
        elif islem == "Subtract":
            sonuc = num1 - num2
        elif islem == "Multiply":
            sonuc = num1 * num2
        elif islem == "Divide":
            if num2 == 0:
                sonuc = "Division by zero error!"
            else:
                sonuc = num1 / num2
        else:
            sonuc = "Geçersiz işlem"
        label_sonuc.config(text=f"Result: {sonuc}")
    except ValueError:
        messagebox.showerror("Error", "Invalid Number!")

def renk_degistir():
    renkler = ["#4caf50", "#ff9800", "#e91e63", "#9c27b0"]
    if not hasattr(renk_degistir, 'index'):
        renk_degistir.index = 0

    selam_label.config(fg=renkler[renk_degistir.index])
    renk_degistir.index = (renk_degistir.index + 1) % len(renkler)
    pencere.after(500, renk_degistir)

def sadece_sayi(girilen_karakter):
    """
    Sadece sayı girişine izin veren doğrulama fonksiyonu
    """
    if girilen_karakter == "":  
        return True
    try:
        float(girilen_karakter)  
        return True
    except ValueError:  
        return False

pencere = tk.Tk()
pencere.title("Basic Calculator")
pencere.geometry("1090x510")
pencere.configure(bg="#363636")  # Background Color
pencere.resizable(False, False)

sadece_sayi_komutu = pencere.register(sadece_sayi)
ana_frame = tk.Frame(pencere, bg="#363636")
ana_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.6, relheight=0.8)

tk.Label(ana_frame, text="First Number:", font=("Book Antiqua", 25 , "bold"),bg="#4caf50").grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry1 = tk.Entry(ana_frame, font=("Impact", 25), width=20, validate="key", validatecommand=(sadece_sayi_komutu, '%P'))
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(ana_frame, text="Second Number:", font=("Book Antiqua", 25 , "bold"), bg="#4caf50").grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry2 = tk.Entry(ana_frame, font=("Impact", 25), width=20, validate="key", validatecommand=(sadece_sayi_komutu, '%P'))
entry2.grid(row=1, column=1, padx=10, pady=5)

islem_frame = tk.Frame(ana_frame, bg="#363636")
islem_frame.grid(row=2, column=0, columnspan=2, pady=20)

var = tk.StringVar(value="Addition")
for i, islem in enumerate(["Addition", "Subtract", "Multiply", "Divide"]):
    tk.Radiobutton(islem_frame, text=islem, variable=var, value=islem, font=("Impact", 20), bg="#363636", fg="#ADD8E6", selectcolor="#4caf50", activebackground="#363636", activeforeground="white").grid(row=0, column=i, padx=5)

tk.Button(ana_frame, text="Calculate", bg="#4caf50", fg="white", font=("Arial", 22, "bold"), width=15, command=hesapla).grid(row=3, column=0, columnspan=2, pady=20)
label_sonuc = tk.Label(ana_frame, text="Result: ", bg="#4caf50", fg="white", font=("Arial", 24, "bold"))
label_sonuc.grid(row=4, column=0, columnspan=2, pady=10)

selam_label = tk.Label(pencere, text="Developed By. ahmetcakir-dev ",
                      font=("Arial", 16, "italic"), bg="#363636", fg="white")
selam_label.place(relx=0, rely=1, anchor="sw", x=10, y=-10)

renk_degistir()

pencere.mainloop()
