import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QFormLayout, QInputDialog, QMessageBox

# Global değişkenler
tarifler = []  # tarifler: Eklenen tüm tariflerin tutulduğu liste
aktif_kullanici = None  # Şu an giriş yapmış olan kullanıcı

class Malzeme:
    def __init__(self, malzeme_adi, miktar):
        self.malzeme_adi = malzeme_adi
        self.miktar = miktar

    def bilgileri_goster(self):
        return f"Malzeme: {self.malzeme_adi}, Miktar: {self.miktar}"

class Kullanici:
    def __init__(self, ad_soyad, sifre):
        self.ad_soyad = ad_soyad
        self.sifre = sifre

    def bilgileri_goster(self):
        return f"Kullanıcı: {self.ad_soyad}"

class Tarif:
    def __init__(self, tarif_adi, tarif_icerigi, ekleyen_kullanici):
        self.tarif_adi = tarif_adi
        self.tarif_icerigi = tarif_icerigi
        self.malzemeler = []
        self.puan = None
        self.ekleyen_kullanici = ekleyen_kullanici

    def malzeme_ekle(self, malzeme):
        self.malzemeler.append(malzeme)

    def puan_ver(self, puan):
        if 1 <= puan <= 5:
            self.puan = puan
            return True
        return False

    def tarif_bilgisi_goster(self):
        bilgiler = f"\nTarif Adı: {self.tarif_adi}\n"
        bilgiler += f"Tarif İçeriği: {self.tarif_icerigi}\n"
        bilgiler += "Malzemeler:\n"
        for malzeme in self.malzemeler:
            bilgiler += f"- {malzeme.bilgileri_goster()}\n"
        bilgiler += f"Puan: {self.puan if self.puan else 'Henüz değerlendirilmedi'}\n"
        bilgiler += f"Tarifi Ekleyen: {self.ekleyen_kullanici.ad_soyad}\n"
        return bilgiler


# PyQt5 Arayüz
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Yemek Tarifi Uygulaması")

        # Layout
        layout = QVBoxLayout()

        # Kullanıcı girişi
        self.ad_soyad_input = QLineEdit(self)
        self.sifre_input = QLineEdit(self)
        self.sifre_input.setEchoMode(QLineEdit.Password)

        # Butonlar
        self.giris_button = QPushButton('Giriş Yap', self)
        self.giris_button.clicked.connect(self.kullanici_girisi)

        layout.addWidget(QLabel('Ad Soyad:'))
        layout.addWidget(self.ad_soyad_input)
        layout.addWidget(QLabel('Şifre:'))
        layout.addWidget(self.sifre_input)
        layout.addWidget(self.giris_button)

        # Tarif ekleme, arama ve değerlendirme butonları
        self.tarif_ekle_button = QPushButton('Tarif Ekle', self)
        self.tarif_ara_button = QPushButton('Tarif Ara', self)
        self.tarif_degerlendir_button = QPushButton('Tarif Değerlendir', self)

        self.tarif_ekle_button.clicked.connect(self.tarif_ekle)
        self.tarif_ara_button.clicked.connect(self.tarif_ara)
        self.tarif_degerlendir_button.clicked.connect(self.tarif_degerlendir)

        layout.addWidget(self.tarif_ekle_button)
        layout.addWidget(self.tarif_ara_button)
        layout.addWidget(self.tarif_degerlendir_button)

        self.setLayout(layout)
        self.show()

    def kullanici_girisi(self):
        ad_soyad = self.ad_soyad_input.text()
        sifre = self.sifre_input.text()

        if ad_soyad and sifre:
            global aktif_kullanici
            aktif_kullanici = Kullanici(ad_soyad, sifre)
            QMessageBox.information(self, 'Hoş Geldiniz', f"Hoş geldiniz, {aktif_kullanici.ad_soyad}!")
        else:
            QMessageBox.warning(self, 'Hata', 'Ad, soyad ve şifre boş olamaz!')

    def tarif_ekle(self):
        if not aktif_kullanici:
            QMessageBox.warning(self, 'Hata', 'Önce kullanıcı girişi yapmalısınız!')
            return

        tarif_adi, ok = QInputDialog.getText(self, 'Tarif Adı', 'Tarifin adını giriniz:')
        if not ok:
            return

        tarif_icerigi, ok = QInputDialog.getText(self, 'Tarif İçeriği', 'Tarifin içeriğini giriniz:')
        if not ok:
            return

        yeni_tarif = Tarif(tarif_adi, tarif_icerigi, aktif_kullanici)

        while True:
            malzeme_adi, ok = QInputDialog.getText(self, 'Malzeme Adı', 'Malzeme adı giriniz (Çıkmak için "q" tuşlayın):')
            if malzeme_adi.lower() == 'q':
                break

            miktar, ok = QInputDialog.getText(self, 'Malzeme Miktarı', 'Malzeme miktarını giriniz:')
            if not ok:
                continue

            malzeme = Malzeme(malzeme_adi, miktar)
            yeni_tarif.malzeme_ekle(malzeme)

        tarifler.append(yeni_tarif)
        QMessageBox.information(self, 'Başarı', f"'{tarif_adi}' tarifiniz başarıyla eklendi!")

    def tarif_ara(self):
        aranan_tarif, ok = QInputDialog.getText(self, 'Tarif Arama', 'Aramak istediğiniz tarifin adını giriniz:')
        if not ok:
            return

        bulundu = False
        for tarif in tarifler:
            if tarif.tarif_adi.lower() == aranan_tarif.lower():
                QMessageBox.information(self, 'Tarif Bilgisi', tarif.tarif_bilgisi_goster())
                bulundu = True
                break

        if not bulundu:
            QMessageBox.warning(self, 'Hata', 'Bu isimde bir tarif bulunamadı.')

    def tarif_degerlendir(self):
        if not tarifler:
            QMessageBox.warning(self, 'Hata', 'Henüz eklenmiş tarif yok!')
            return

        tarif_adi, ok = QInputDialog.getText(self, 'Tarif Değerlendir', 'Değerlendirmek istediğiniz tarifin adını giriniz:')
        if not ok:
            return

        for tarif in tarifler:
            if tarif.tarif_adi.lower() == tarif_adi.lower():
                puan, ok = QInputDialog.getInt(self, 'Tarif Puanı', '1 ile 5 arasında bir puan veriniz:', min=1, max=5)
                if ok:
                    tarif.puan_ver(puan)
                    QMessageBox.information(self, 'Puan Verildi', f"'{tarif.tarif_adi}' tarifine {puan} puan verildi.")
                return

        QMessageBox.warning(self, 'Hata', 'Tarif bulunamadı.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
