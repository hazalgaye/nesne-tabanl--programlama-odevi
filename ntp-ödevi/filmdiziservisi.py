import tkinter as tk
from tkinter import messagebox, simpledialog

class Film: 
    def __init__(self, ad, yonetmen, tur, sure): 
        self.ad = ad    
        self.yonetmen = yonetmen
        self.tur = tur
        self.sure = sure

    def __str__(self):
        return f"{self.ad} ({self.tur}) - {self.sure} dk - Yönetmen: {self.yonetmen}" 

class Kullanici:
    def __init__(self, ad, sifre):
        self.ad = ad
        self.sifre = sifre
        self.izleme_gecmisi = []

    def film_izle(self, film):
        self.izleme_gecmisi.append(film)

class FilmServisiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Film ve Dizi İzleme Servisi")

        self.kullanicilar = []
        self.filmler = []
        self.giris_yapan = None

        self.ana_ekran()

    def ana_ekran(self):
        for widget in self.root.winfo_children(): 
            widget.destroy() 

        tk.Label(self.root, text="Film ve Dizi İzleme Servisi", font=("Arial", 20)).pack(pady=10) 

        tk.Button(self.root, text="Kullanıcı Kaydı", width=20, command=self.kullanici_kaydi).pack(pady=5) 
        tk.Button(self.root, text="Giriş Yap", width=20, command=self.giris_yap).pack(pady=5) 
        tk.Button(self.root, text="Çıkış", width=20, command=self.root.quit).pack(pady=5) 

    def kullanici_kaydi(self):
        ad = simpledialog.askstring("Kayıt", "Kullanıcı Adı:") 
        sifre = simpledialog.askstring("Kayıt", "Şifre:")
        if ad and sifre:
            self.kullanicilar.append(Kullanici(ad, sifre))
            messagebox.showinfo("Başarılı", "Kullanıcı kaydı yapıldı.") 

    def giris_yap(self):
        ad = simpledialog.askstring("Giriş", "Kullanıcı Adı:")
        sifre = simpledialog.askstring("Giriş", "Şifre:")
        for kullanici in self.kullanicilar:
            if kullanici.ad == ad and kullanici.sifre == sifre:
                self.giris_yapan = kullanici
                messagebox.showinfo("Başarılı", f"Hoş geldin {ad}!")
                self.kullanici_ekrani()
                return
        messagebox.showerror("Hata", "Hatalı kullanıcı adı veya şifre.")

    def kullanici_ekrani(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"Hoşgeldin {self.giris_yapan.ad}", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.root, text="Film Ekle", width=20, command=self.film_ekle).pack(pady=5)
        tk.Button(self.root, text="Film İzle", width=20, command=self.film_izle).pack(pady=5)
        tk.Button(self.root, text="İzleme Geçmişi", width=20, command=self.gecmisi_gor).pack(pady=5)
        tk.Button(self.root, text="Çıkış Yap", width=20, command=self.cikis_yap).pack(pady=5)

    def film_ekle(self):
        ad = simpledialog.askstring("Film Ekle", "Film Adı:") 
        yonetmen = simpledialog.askstring("Film Ekle", "Yönetmen:")
        tur = simpledialog.askstring("Film Ekle", "Tür:")
        sure = simpledialog.askinteger("Film Ekle", "Süre (dk):")
        if ad and yonetmen and tur and sure:
            self.filmler.append(Film(ad, yonetmen, tur, sure))
            messagebox.showinfo("Başarılı", "Film eklendi.")

    def film_izle(self):
        if not self.filmler:
            messagebox.showerror("Hata", "İzleyecek film yok.")
            return
        film_listesi = "\n".join([f"{idx+1}. {film}" for idx, film in enumerate(self.filmler)]) 

        secim = simpledialog.askinteger("Film İzle", f"İzlemek istediğin filmi seç:\n\n{film_listesi}")
        if secim and 1 <= secim <= len(self.filmler): 
            film = self.filmler[secim-1]
            self.giris_yapan.film_izle(film)
            messagebox.showinfo("İzleniyor", f"{film.ad} izleniyor...")

    def gecmisi_gor(self):
        if not self.giris_yapan.izleme_gecmisi: 
            messagebox.showinfo("Geçmiş", "Hiç film izlenmemiş.") 
            return
        gecmis = "\n".join([str(film) for film in self.giris_yapan.izleme_gecmisi]) 
        messagebox.showinfo("İzleme Geçmişi", gecmis)

    def cikis_yap(self):
        self.giris_yapan = None
        self.ana_ekran()

root = tk.Tk() 
app = FilmServisiApp(root)
root.mainloop() 