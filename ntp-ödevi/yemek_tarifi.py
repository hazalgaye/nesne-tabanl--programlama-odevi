class Malzeme:
    def __init__(self, malzeme_adi, miktar):#self:Python'da sınıf içindeki verilere (özelliklere) erişmek için self kullanılır
        self.malzeme_adi = malzeme_adi
        self.miktar = miktar

    def bilgileri_goster(self):#Bu metod, malzemenin bilgilerini düzgün formatta gösterir.
        return f"Malzeme: {self.malzeme_adi}, Miktar: {self.miktar}"

class Kullanici:#Kullanıcıların ad-soyad ve şifresi tutuluyor.Sisteme giriş yapan her kullanıcı, bir Kullanici nesnesi oluyor.
    def __init__(self, ad_soyad, sifre):
        self.ad_soyad = ad_soyad
        self.sifre = sifre

    def bilgileri_goster(self):#Kullanıcının adını ve soyadını gösteren bir metod.
        return f"Kullanıcı: {self.ad_soyad}"

class Tarif:#Bir tarifin:Adı (tarif_adi)İçeriği (tarif_icerigi)Malzemeleri (malzemeler, başlangıçta boş liste)Puanı (puan, başlangıçta yok)Ekleyen kullanıcısı (ekleyen_kullanici) tutuluyor.
    def __init__(self, tarif_adi, tarif_icerigi, ekleyen_kullanici):
        self.tarif_adi = tarif_adi
        self.tarif_icerigi = tarif_icerigi
        self.malzemeler = []
        self.puan = None
        self.ekleyen_kullanici = ekleyen_kullanici

    def malzeme_ekle(self, malzeme):#Bir tarifin malzeme listesine yeni malzeme ekler.
        self.malzemeler.append(malzeme)

    def puan_ver(self, puan):#Tarife 1 ile 5 arasında bir puan verilebilir.Geçersiz puan verilirse reddediliyor.
        if 1 <= puan <= 5:
            self.puan = puan
            return True
        return False

    def tarif_bilgisi_goster(self): #Tarifin tüm bilgilerini (adı, içeriği, malzemeler, puan, kim eklemiş) ekrana yazdırır.
        bilgiler = f"\nTarif Adı: {self.tarif_adi}\n"#bilgiler, tarifin detaylarını içeren string bir değişken.
        bilgiler += f"Tarif İçeriği: {self.tarif_icerigi}\n"
        bilgiler += "Malzemeler:\n"
        for malzeme in self.malzemeler:
            bilgiler += f"- {malzeme.bilgileri_goster()}\n"
        bilgiler += f"Puan: {self.puan if self.puan else 'Henüz değerlendirilmedi'}\n"
        bilgiler += f"Tarifi Ekleyen: {self.ekleyen_kullanici.ad_soyad}\n"
        print(bilgiler)

# --- Global değişkenler ---
tarifler = [] #tarifler: Eklenen tüm tariflerin tutulduğu liste.aktif_kullanici: Şu an giriş yapmış olan kullanıcı.
aktif_kullanici = None

# --- Fonksiyonlar ---

def kullanici_girisi():
    global aktif_kullanici
    while True:
        ad_soyad = input("Adınızı ve soyadınızı giriniz: ").strip()#Bir yazının (stringin) başındaki ve sonundaki boşlukları siler.
        sifre = input("Şifrenizi giriniz: ").strip()
        if ad_soyad and sifre:
            aktif_kullanici = Kullanici(ad_soyad, sifre)
            print(f"Hoş geldiniz, {aktif_kullanici.ad_soyad}!")
            break
        else:
            print("Ad, soyad ve şifre boş olamaz. Lütfen tekrar deneyin.")

def tarif_ekle():
    if not aktif_kullanici:
        print("Önce kullanıcı girişi yapmalısınız!")
        return

    tarif_adi = input("Tarifin adını giriniz: ")
    tarif_icerigi = input("Tarifin içeriğini kısaca açıklayın: ")

    yeni_tarif = Tarif(tarif_adi, tarif_icerigi, aktif_kullanici)

    while True:
        malzeme_adi = input("Malzeme adı giriniz (Çıkmak için 'q' tuşlayın): ")
        if malzeme_adi.lower() == "q":
            break
        miktar = input("Bu malzemenin miktarını giriniz: ")

        malzeme = Malzeme(malzeme_adi, miktar)
        yeni_tarif.malzeme_ekle(malzeme)

    tarifler.append(yeni_tarif)
    print(f"'{tarif_adi}' tarifiniz başarıyla eklendi!")

def tarif_ara():
    aranan_tarif = input("Aramak istediğiniz tarifin adını giriniz: ")
    bulundu = False
    for tarif in tarifler:
        if tarif.tarif_adi.lower() == aranan_tarif.lower():
            tarif.tarif_bilgisi_goster()
            bulundu = True
            break
    if not bulundu:
        print("Bu isimde bir tarif bulunamadı.")

def tarif_degerlendir():
    if not tarifler:
        print("Henüz eklenmiş tarif yok!")
        return

    print("\nMevcut Tarifler:")
    for index, tarif in enumerate(tarifler):
        print(f"{index + 1}. {tarif.tarif_adi}")

    secim = input("Değerlendirmek istediğiniz tarifin numarasını giriniz: ")
    try:
        secim = int(secim)
        if 1 <= secim <= len(tarifler):
            tarif = tarifler[secim - 1]
            puan = input("Bu tarife 1 ile 5 arasında bir puan veriniz: ")
            try:
                puan = int(puan)
                if tarif.puan_ver(puan):
                    print(f"'{tarif.tarif_adi}' tarifine {puan} puan verildi.")
                else:
                    print("Geçersiz puan! Lütfen 1 ile 5 arasında bir puan giriniz.")
            except ValueError:
                print("Lütfen geçerli bir sayı giriniz.")
        else:
            print("Geçersiz seçim!")
    except ValueError:
        print("Lütfen geçerli bir numara giriniz.")

def menu():
    kullanici_girisi()  # Program başlar başlamaz kullanıcı giriş yapacak
    while True:
        print("\n--- Yemek Tarifi Uygulaması ---")
        print("1. Tarif Ekle")
        print("2. Tarif Ara")
        print("3. Tarif Değerlendir")
        print("4. Çıkış")
        secim = input("Lütfen bir seçenek giriniz (1-4): ")

        if secim == "1":
            tarif_ekle()
        elif secim == "2":
            tarif_ara()
        elif secim == "3":
            tarif_degerlendir()
        elif secim == "4":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen tekrar deneyiniz.")

# --- Programı Başlat ---
menu()
