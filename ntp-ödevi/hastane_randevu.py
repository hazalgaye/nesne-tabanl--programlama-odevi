class Hasta:
    def __init__(self, isim, tc):
        self.isim = isim
        self.tc = tc
        self.randevu = None  # Bir hastanın sadece bir randevusu olabilir

class Doktor:
    def __init__(self, isim, uzmanlik):
        self.isim = isim
        self.uzmanlik = uzmanlik
        self.musaitlik = True  # Başlangıçta doktorlar müsait

class Randevu:
    def __init__(self, tarih, doktor, hasta):
        self.tarih = tarih
        self.doktor = doktor
        self.hasta = hasta #Bu sınıf, bir randevuyu temsil eder. Her randevu bir tarih, bir doktor ve bir hasta ile ilişkilidir.

# Örnek veriler
doktorlar = [Doktor("Ahmet Yılmaz", "Dahiliye"), Doktor("Elif Demir", "Kardiyoloji")]
hastalar = [Hasta("Ayşe Koç", "12345678901"), Hasta("Ali Can", "23456789012")]

# Randevu alma fonksiyonu randevu_al(): Bu fonksiyon, hasta adı ve TC kimlik numarasına göre hasta arar, ardından mevcut müsait doktorları listeleyip birini seçmek için kullanıcıdan giriş alır. Seçilen doktordan bir randevu alır ve doktoru meşgul yapar.
def randevu_al():
    isim = input("Adınızı girin: ")
    tc = input("TC kimlik numaranızı girin: ")
    hasta = next((h for h in hastalar if h.tc == tc and h.isim == isim), None)  # Hem TC hem de isim kontrolü

    if not hasta:
        print("Hasta bulunamadı! TC veya isim yanlış olabilir.")
        return

    print("\nMüsait Doktorlar:")
    for idx, doktor in enumerate(doktorlar):
        if doktor.musaitlik:
            print(f"{idx + 1}. Dr. {doktor.isim} - {doktor.uzmanlik}")

    secim = int(input("Randevu almak istediğiniz doktoru seçin: ")) - 1
    if 0 <= secim < len(doktorlar) and doktorlar[secim].musaitlik:
        tarih = input("Randevu tarihini girin (GG/AA/YYYY): ")
        randevu = Randevu(tarih, doktorlar[secim], hasta)
        hasta.randevu = randevu
        doktorlar[secim].musaitlik = False  # Doktoru meşgul yapıyoruz
        print(f"Randevunuz alındı: {tarih} tarihinde Dr. {doktorlar[secim].isim} ile.")
    else:
        print("Geçersiz seçim veya doktor müsait değil.")

# Randevu iptal fonksiyonu randevu_iptal(): Bu fonksiyon, hasta adı ve TC kimlik numarasına göre hastanın mevcut randevusunu bulur ve randevuyu iptal eder. İptal edilen randevunun ardından doktor tekrar müsait yapılır.
def randevu_iptal():
    isim = input("Adınızı girin: ")
    tc = input("TC kimlik numaranızı girin: ")
    hasta = next((h for h in hastalar if h.tc == tc and h.isim == isim), None)  # Hem TC hem de isim kontrolü

    if not hasta or not hasta.randevu:
        print("Randevu bulunamadı! TC veya isim yanlış olabilir.")
        return

    print(f"Randevu iptal ediliyor: {hasta.randevu.tarih} tarihinde Dr. {hasta.randevu.doktor.isim}")
    hasta.randevu.doktor.musaitlik = True  # Doktoru tekrar müsait yapıyoruz
    hasta.randevu = None  # Randevuyu siliyoruz

# Hasta ekleme fonksiyonu hasta_ekle(): Bu fonksiyon, yeni bir hasta eklemek için kullanılır. Kullanıcıdan hasta adı ve TC kimlik numarası alınır ve bu bilgilerle yeni bir hasta nesnesi oluşturulup hastalar listesine eklenir.
def hasta_ekle():
    isim = input("Hasta ismini girin: ")
    tc = input("Hasta TC kimlik numarasını girin: ")

    # Yeni hasta nesnesi oluşturuluyor ve hastalar listesine ekleniyor
    hasta = Hasta(isim, tc)
    hastalar.append(hasta)
    print(f"{isim} başarıyla kaydedildi.")

# Doktor ekleme fonksiyonu doktor_ekle(): Bu fonksiyon, yeni bir doktor eklemek için kullanılır. Kullanıcıdan doktor adı ve uzmanlık alanı alınır ve yeni bir doktor nesnesi oluşturulup doktorlar listesine eklenir.
def doktor_ekle():
    isim = input("Doktor ismini girin: ")
    uzmanlik = input("Doktor uzmanlık alanını girin: ")

    # Yeni doktor nesnesi oluşturuluyor ve doktorlar listesine ekleniyor
    doktor = Doktor(isim, uzmanlik)
    doktorlar.append(doktor)
    print(f"Dr. {isim} başarıyla kaydedildi.")

# Ana Menü ana_menu(): Bu, ana menüyü oluşturur ve kullanıcıdan seçim yapmasını ister. Seçime göre randevu_al(), randevu_iptal(), hasta_ekle(), doktor_ekle() gibi fonksiyonlar çalıştırılır.
def ana_menu():
    while True:
        print("\n1. Randevu Al\n2. Randevu İptal Et\n3. Hasta Ekle\n4. Doktor Ekle\n5. Çıkış")
        secim = input("Bir işlem seçin (1-5): ")

        if secim == "1":
            randevu_al()
        elif secim == "2":
            randevu_iptal()
        elif secim == "3":
            hasta_ekle()
        elif secim == "4":
            doktor_ekle()
        elif secim == "5":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim!")

ana_menu()
