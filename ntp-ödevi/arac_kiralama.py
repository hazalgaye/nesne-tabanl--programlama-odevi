

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QListWidget, QMessageBox, QVBoxLayout
from PyQt5.QtCore import Qt
import sys

arac_listesi = []
musteri_listesi = []
kiralama_listesi = []

class Arac:
    def __init__(self, arac_id, model):
        self.arac_id = arac_id
        self.model = model
        self.kiralama_durumu = False

class Musteri:
    def __init__(self, musteri_id, ad, soyad):
        self.musteri_id = musteri_id
        self.ad = ad
        self.soyad = soyad

class Kiralama:
    def __init__(self, musteri, arac, gun_sayisi):
        self.musteri = musteri
        self.arac = arac
        self.gun_sayisi = gun_sayisi

    def kiralama_yap(self):
        if not self.arac.kiralama_durumu:
            self.arac.kiralama_durumu = True
            return True
        else:
            return False

class AnaMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ana Menü")
        self.setGeometry(200, 200, 350, 400)

        self.layout = QVBoxLayout()

        self.label = QLabel("Ana Menü")
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        self.buton_arac_kayit = QPushButton("Araç Kaydı")
        self.buton_musteri_kayit = QPushButton("Müşteri Kaydı")
        self.buton_arac_kirala = QPushButton("Araç Kirala")
        self.buton_kiralama_iptal = QPushButton("Kiralama İptal")
        self.buton_kiralama_listele = QPushButton("Kiralamaları Listele")

        self.buton_arac_kayit.clicked.connect(self.arac_kayit)
        self.buton_musteri_kayit.clicked.connect(self.musteri_kayit)
        self.buton_arac_kirala.clicked.connect(self.arac_kirala)
        self.buton_kiralama_iptal.clicked.connect(self.kiralama_iptal)
        self.buton_kiralama_listele.clicked.connect(self.kiralamalari_listele)

        self.layout.addWidget(self.buton_arac_kayit)
        self.layout.addWidget(self.buton_musteri_kayit)
        self.layout.addWidget(self.buton_arac_kirala)
        self.layout.addWidget(self.buton_kiralama_iptal)
        self.layout.addWidget(self.buton_kiralama_listele)

        self.setLayout(self.layout)

    def arac_kayit(self):
        self.pencere = AracKayitPenceresi()
        self.pencere.show()

    def musteri_kayit(self):
        self.pencere = MusteriKayitPenceresi()
        self.pencere.show()

    def arac_kirala(self):
        self.pencere = AracKiralamaPenceresi()
        self.pencere.show()

    def kiralama_iptal(self):
        self.pencere = KiralamaIptalPenceresi()
        self.pencere.show()

    def kiralamalari_listele(self):
        self.pencere = KiralamaListelePenceresi()
        self.pencere.show()

class AracKayitPenceresi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Araç Kaydı")
        self.setGeometry(250, 250, 300, 200)

        self.layout = QVBoxLayout()

        self.label_id = QLabel("Araç ID:")
        self.input_id = QLineEdit()
        self.label_model = QLabel("Model:")
        self.input_model = QLineEdit()

        self.buton_kaydet = QPushButton("Kaydet")
        self.buton_kaydet.clicked.connect(self.arac_kaydet)

        self.layout.addWidget(self.label_id)
        self.layout.addWidget(self.input_id)
        self.layout.addWidget(self.label_model)
        self.layout.addWidget(self.input_model)
        self.layout.addWidget(self.buton_kaydet)

        self.setLayout(self.layout)

    def arac_kaydet(self):
        arac_id = self.input_id.text()
        model = self.input_model.text()
        if arac_id and model:
            arac = Arac(arac_id, model)
            arac_listesi.append(arac)
            QMessageBox.information(self, "Başarılı", "Araç kaydedildi.")
            self.close()
        else:
            QMessageBox.warning(self, "Hata", "Bu alan boş bırakılamaz.")

class MusteriKayitPenceresi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Müşteri Kaydı")
        self.setGeometry(300, 300, 300, 250)

        self.layout = QVBoxLayout()

        self.label_id = QLabel("Müşteri ID:")
        self.input_id = QLineEdit()
        self.label_ad = QLabel("Adı:")
        self.input_ad = QLineEdit()
        self.label_soyad = QLabel("Soyadı:")
        self.input_soyad = QLineEdit()

        self.buton_kaydet = QPushButton("Kaydet")
        self.buton_kaydet.clicked.connect(self.musteri_kaydet)

        self.layout.addWidget(self.label_id)
        self.layout.addWidget(self.input_id)
        self.layout.addWidget(self.label_ad)
        self.layout.addWidget(self.input_ad)
        self.layout.addWidget(self.label_soyad)
        self.layout.addWidget(self.input_soyad)
        self.layout.addWidget(self.buton_kaydet)

        self.setLayout(self.layout)

    def musteri_kaydet(self):
        musteri_id = self.input_id.text()
        ad = self.input_ad.text()
        soyad = self.input_soyad.text()
        if musteri_id and ad and soyad:
            musteri = Musteri(musteri_id, ad, soyad)
            musteri_listesi.append(musteri)
            QMessageBox.information(self, "Başarılı", "Müşteri kaydedildi.")
            self.close()
        else:
            QMessageBox.warning(self, "Hata", "Bu alan boş bırakılamaz.")

class AracKiralamaPenceresi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Araç Kiralama")
        self.setGeometry(300, 300, 300, 300)

        self.layout = QVBoxLayout()

        self.label_musteri = QLabel("Müşteri ID:")
        self.input_musteri = QLineEdit()

        self.label_arac = QLabel("Araç ID:")
        self.input_arac = QLineEdit()

        self.label_gun = QLabel("Kaç gün kiralanacak:")
        self.input_gun = QLineEdit()

        self.buton_kirala = QPushButton("Kirala")
        self.buton_kirala.clicked.connect(self.kiralama_yap)

        self.layout.addWidget(self.label_musteri)
        self.layout.addWidget(self.input_musteri)
        self.layout.addWidget(self.label_arac)
        self.layout.addWidget(self.input_arac)
        self.layout.addWidget(self.label_gun)
        self.layout.addWidget(self.input_gun)
        self.layout.addWidget(self.buton_kirala)

        self.setLayout(self.layout)

    def kiralama_yap(self):
        musteri_id = self.input_musteri.text()
        arac_id = self.input_arac.text()
        gun = self.input_gun.text()

        musteri = next((musteri for musteri in musteri_listesi if musteri.musteri_id == musteri_id), None)
        arac = next((arac for arac in arac_listesi if arac.arac_id == arac_id), None)

        if musteri and arac and gun.isdigit():
            gun = int(gun)
            if gun > 0:
                kiralama = Kiralama(musteri, arac, gun)
                if kiralama.kiralama_yap():
                    kiralama_listesi.append(kiralama)
                    QMessageBox.information(self, "Başarılı", "Araç kiralandı!")
                    self.close()
                else:
                    QMessageBox.warning(self, "Uyarı", "Bu araç zaten kiralanmış.")
            else:
                QMessageBox.warning(self, "Hata", "Gün sayısı 0 veya negatif olamaz.")
        else:
            QMessageBox.warning(self, "Hata", "Müşteri ID veya Araç ID hatalı.")

class KiralamaIptalPenceresi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kiralama İptal")
        self.setGeometry(400, 400, 300, 200)

        self.layout = QVBoxLayout()

        self.label_musteri = QLabel("Müşteri ID:")
        self.input_musteri = QLineEdit()
        self.label_arac = QLabel("Araç ID:")
        self.input_arac = QLineEdit()

        self.buton_iptal = QPushButton("İptal Et")
        self.buton_iptal.clicked.connect(self.kiralama_iptal)

        self.layout.addWidget(self.label_musteri)
        self.layout.addWidget(self.input_musteri)
        self.layout.addWidget(self.label_arac)
        self.layout.addWidget(self.input_arac)
        self.layout.addWidget(self.buton_iptal)

        self.setLayout(self.layout)

    def kiralama_iptal(self):
        musteri_id = self.input_musteri.text()
        arac_id = self.input_arac.text()

        kiralama = next((kiralama for kiralama in kiralama_listesi if kiralama.musteri.musteri_id == musteri_id and kiralama.arac.arac_id == arac_id), None)

        if kiralama:
            kiralama.arac.kiralama_durumu = False
            kiralama_listesi.remove(kiralama)
            QMessageBox.information(self, "Başarılı", "İptal edildi.")
            self.close()
        else:
            QMessageBox.warning(self, "Hata", "Kiralama bulunamadı.")

class KiralamaListelePenceresi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kiralamalar")
        self.setGeometry(450, 450, 400, 300)

        self.layout = QVBoxLayout()

        self.liste = QListWidget()
        self.layout.addWidget(self.liste)

        self.setLayout(self.layout)

        self.kiralamalari_goster()

    def kiralamalari_goster(self):
        if kiralama_listesi:
            for kiralama in kiralama_listesi:
                bilgi = f"{kiralama.musteri.ad} {kiralama.musteri.soyad} - {kiralama.arac.model} ({kiralama.gun_sayisi} gün)"
                self.liste.addItem(bilgi)
        else:
            self.liste.addItem("Kiralama bulunamadı.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    giris_ekrani = AnaMenu()
    giris_ekrani.show()
    sys.exit(app.exec_())
