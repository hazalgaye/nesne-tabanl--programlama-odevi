
import tkinter as tk
from tkinter import messagebox


kullanicilar = [] 
kitaplar = []
yorumlar = []


class Kullanici:
    def __init__(self, kullanici_adi, sifre):
        self.kullanici_adi = kullanici_adi
        self.sifre = sifre
        self.okuma_listesi = []

class Kitap:
    def __init__(self, ad, yazar, yayinevi):
        self.ad = ad
        self.yazar = yazar
        self.yayinevi = yayinevi

class Yorum:
    def __init__(self, kitap_adi, kullanici_adi, yorum_metni):
        self.kitap_adi = kitap_adi
        self.kullanici_adi = kullanici_adi
        self.yorum_metni = yorum_metni


def kullanici_olustur(): 
    ad = kullanici_entry.get()
    sifre = sifre_entry.get()
    if ad and sifre:
        kullanicilar.append(Kullanici(ad, sifre))
        messagebox.showinfo("Başarılı", "Kullanıcı oluşturuldu!")
    else:
        messagebox.showerror("Hata", "Kullanıcı adı ve şifre boş olamaz.")

def kitap_ekle():
    ad = kitap_entry.get()
    yazar = yazar_entry.get()
    yayinevi = yayinevi_entry.get()
    if ad and yazar and yayinevi:
        kitaplar.append(Kitap(ad, yazar, yayinevi))
        messagebox.showinfo("Başarılı", "Kitap eklendi!")
    else:
        messagebox.showerror("Hata", "Tüm kitap bilgileri doldurulmalıdır.")

def yorum_yap():
    kitap_adi = kitap_entry.get()
    kullanici_adi = kullanici_entry.get()
    yorum_metni = yorum_entry.get()
    if kitap_adi and kullanici_adi and yorum_metni:
        yorumlar.append(Yorum(kitap_adi, kullanici_adi, yorum_metni))
        messagebox.showinfo("Başarılı", "Yorum yapıldı!")
    else:
        messagebox.showerror("Hata", "Tüm alanlar doldurulmalıdır.")

def okuma_listesini_goster():
    if not kitaplar:
        messagebox.showinfo("Liste Boş", "Henüz kitap eklenmedi.")
        return
    liste = ""
    for kitap in kitaplar:
        liste += f"Kitap: {kitap.ad}, Yazar: {kitap.yazar}, Yayınevi: {kitap.yayinevi}\n"
    messagebox.showinfo("Okuma Listesi", liste)


pencere = tk.Tk()
pencere.title("Çevrimiçi Kitap Okuma Platformu")
pencere.geometry("400x600") 
pencere.resizable(False, False) 


baslik = tk.Label(pencere, text="Kitap Okuma ve Paylaşım Platformu", font=("Arial", 16, "bold"))
baslik.pack(pady=20)


kullanici_entry = tk.Entry(pencere, width=30)
kullanici_entry.pack(pady=5)
kullanici_entry.insert(0, "Kullanıcı Adı")

sifre_entry = tk.Entry(pencere, width=30, show="*")
sifre_entry.pack(pady=5)
sifre_entry.insert(0, "Şifre")

kullanici_olustur_buton = tk.Button(pencere, text="Kullanıcı Oluştur", width=25, command=kullanici_olustur)
kullanici_olustur_buton.pack(pady=10)


kitap_entry = tk.Entry(pencere, width=30)
kitap_entry.pack(pady=5)
kitap_entry.insert(0, "Kitap Adı")

yazar_entry = tk.Entry(pencere, width=30)
yazar_entry.pack(pady=5)
yazar_entry.insert(0, "Yazar")

yayinevi_entry = tk.Entry(pencere, width=30)
yayinevi_entry.pack(pady=5)
yayinevi_entry.insert(0, "Yayınevi")

kitap_ekle_buton = tk.Button(pencere, text="Kitap Ekle", width=25, command=kitap_ekle)
kitap_ekle_buton.pack(pady=10)


yorum_entry = tk.Entry(pencere, width=30)
yorum_entry.pack(pady=5)
yorum_entry.insert(0, "Yorum")

yorum_yap_buton = tk.Button(pencere, text="Yorum Yap", width=25, command=yorum_yap)
yorum_yap_buton.pack(pady=10)


okuma_listesi_buton = tk.Button(pencere, text="Okuma Listesini Göster", width=30, command=okuma_listesini_goster)
okuma_listesi_buton.pack(pady=20)

pencere.mainloop()
