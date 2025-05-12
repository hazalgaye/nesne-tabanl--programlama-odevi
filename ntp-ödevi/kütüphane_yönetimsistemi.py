import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QListWidget, QMessageBox
from PyQt5.QtCore import Qt

kitap_listesi = []
uye_listesi = []
odunc_listesi = []

class Kitap:
    def __init__(self, kitap_id, kitap_adi, yazar, sayfa_sayisi):
        self.kitap_id = kitap_id
        self.kitap_adi = kitap_adi
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.durum = "Mevcut"

    def durum_guncelle(self, yeni_durum):
        self.durum = yeni_durum

class Uye:
    def __init__(self, uye_id, uye_adi, uye_soyadi):
        self.uye_id = uye_id
        self.uye_adi = uye_adi
        self.uye_soyadi = uye_soyadi

class Odunc:
    def __init__(self, uye, kitap):
        self.uye = uye
        self.kitap = kitap

class AnaMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ana Menü")
        self.setGeometry(200, 200, 400, 400)

        self.layout = QVBoxLayout()

        self.label = QLabel("Ana Menü")
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        self.buton_kitap_ekle = QPushButton("Kitap Ekle")
        self.buton_uye_ekle = QPushButton("Üye Ekle")
        self.buton_odunc_al = QPushButton("Ödünç Kitap Al")
        self.buton_odunc_listele = QPushButton("Ödünç Kitaplar")

        self.layout.addWidget(self.buton_kitap_ekle)
        self.layout.addWidget(self.buton_uye_ekle)
        self.layout.addWidget(self.buton_odunc_al)
        self.layout.addWidget(self.buton_odunc_listele)

        self.buton_kitap_ekle.clicked.connect(self.kitap_ekle)
        self.buton_uye_ekle.clicked.connect(self.uye_ekle)
        self.buton_odunc_al.clicked.connect(self.odunc_al)
        self.buton_odunc_listele.clicked.connect(self.odunc_listele)

        self.setLayout(self.layout)

    def kitap_ekle(self):
        self.pencere = KitapEklePenceresi()
        self.pencere.show()

    def uye_ekle(self):
        self.pencere = UyeEklePenceresi()
        self.pencere.show()

    def odunc_al(self):
        self.pencere = OduncAlPenceresi()
        self.pencere.show()

    def odunc_listele(self):
        self.pencere = OduncListelePenceresi()
        self.pencere.show()

class KitapEklePenceresi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kitap Ekle")
        self.setGeometry(300, 300, 300, 300)

        self.layout = QVBoxLayout()

        self.label_id = QLabel("Kitap ID:")
        self.input_id = QLineEdit()

        self.label_adi = QLabel("Kitap Adı:")
        self.input_adi = QLineEdit()

        self.label_yazar = QLabel("Yazar:")
        self.input_yazar = QLineEdit()

        self.label_sayfa = QLabel("Sayfa Sayısı:")
        self.input_sayfa = QLineEdit()

        self.buton_kaydet = QPushButton("Kaydet")
        self.buton_kaydet.clicked.connect(self.kitap_kaydet)

        self.layout.addWidget(self.label_id)
        self.layout.addWidget(self.input_id)
        self.layout.addWidget(self.label_adi)
        self.layout.addWidget(self.input_adi)
        self.layout.addWidget(self.label_yazar)
        self.layout.addWidget(self.input_yazar)
        self.layout.addWidget(self.label_sayfa)
        self.layout.addWidget(self.input_sayfa)
        self.layout.addWidget(self.buton_kaydet)

        self.setLayout(self.layout)

    def kitap_kaydet(self):
        kitap_id = self.input_id.text()
        kitap_adi = self.input_adi.text()
        yazar = self.input_yazar.text()
        sayfa_sayisi = self.input_sayfa.text()

        if kitap_id and kitap_adi and yazar and sayfa_sayisi.isdigit():
            sayfa_sayisi = int(sayfa_sayisi)
            if sayfa_sayisi > 0:
                yeni_kitap = Kitap(kitap_id, kitap_adi, yazar, sayfa_sayisi)
                kitap_listesi.append(yeni_kitap)
                QMessageBox.information(self, "Başarılı", "Kitap kaydedildi.")
                self.close()
            else:
                QMessageBox.warning(self, "Hata", "Sayfa sayısı 0 veya negatif olamaz.")
        else:
            QMessageBox.warning(self, "Hata", "Tüm alanları doğru doldurun.")

class UyeEklePenceresi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Üye Ekle")
        self.setGeometry(350, 350, 300, 250)

        self.layout = QVBoxLayout()

        self.label_id = QLabel("Üye ID:")
        self.input_id = QLineEdit()

        self.label_adi = QLabel("Üye Adı:")
        self.input_adi = QLineEdit()

        self.label_soyadi = QLabel("Üye Soyadı:")
        self.input_soyadi = QLineEdit()

        self.buton_kaydet = QPushButton("Kaydet")
        self.buton_kaydet.clicked.connect(self.uye_kaydet)

        self.layout.addWidget(self.label_id)
        self.layout.addWidget(self.input_id)
        self.layout.addWidget(self.label_adi)
        self.layout.addWidget(self.input_adi)
        self.layout.addWidget(self.label_soyadi)
        self.layout.addWidget(self.input_soyadi)
        self.layout.addWidget(self.buton_kaydet)

        self.setLayout(self.layout)

    def uye_kaydet(self):
        uye_id = self.input_id.text()
        uye_adi = self.input_adi.text()
        uye_soyadi = self.input_soyadi.text()

        if uye_id and uye_adi and uye_soyadi:
            yeni_uye = Uye(uye_id, uye_adi, uye_soyadi)
            uye_listesi.append(yeni_uye)
            QMessageBox.information(self, "Başarılı", "Üye kaydedildi.")
            self.close()
        else:
            QMessageBox.warning(self, "Hata", "Tüm alanları doldurun.")

class OduncAlPenceresi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ödünç Kitap Al")
        self.setGeometry(400, 400, 300, 200)

        self.layout = QVBoxLayout()

        self.label_uye = QLabel("Üye ID:")
        self.input_uye = QLineEdit()

        self.label_kitap = QLabel("Kitap ID:")
        self.input_kitap = QLineEdit()

        self.buton_al = QPushButton("Ödünç Al")
        self.buton_al.clicked.connect(self.odunc_al)

        self.layout.addWidget(self.label_uye)
        self.layout.addWidget(self.input_uye)
        self.layout.addWidget(self.label_kitap)
        self.layout.addWidget(self.input_kitap)
        self.layout.addWidget(self.buton_al)

        self.setLayout(self.layout)

    def odunc_al(self):
        uye_id = self.input_uye.text()
        kitap_id = self.input_kitap.text()

        uye = next((uye for uye in uye_listesi if uye.uye_id == uye_id), None)
        kitap = next((kitap for kitap in kitap_listesi if kitap.kitap_id == kitap_id), None)

        if uye and kitap:
            if kitap.durum == "Mevcut":
                kitap.durum_guncelle("Ödünç Alındı")
                yeni_odunc = Odunc(uye, kitap)
                odunc_listesi.append(yeni_odunc)
                QMessageBox.information(self, "Başarılı", "Kitap ödünç alındı.")
                self.close()
            else:
                QMessageBox.warning(self, "Uyarı", "Kitap zaten ödünç alınmış.")
        else:
            QMessageBox.warning(self, "Hata", "Üye veya kitap bulunamadı.")

class OduncListelePenceresi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ödünç Kitaplar")
        self.setGeometry(450, 450, 400, 300)

        self.layout = QVBoxLayout()

        self.liste = QListWidget()

        if odunc_listesi:
            for odunc in odunc_listesi:
                bilgi = f"{odunc.uye.uye_adi} {odunc.uye.uye_soyadi} --> {odunc.kitap.kitap_adi}"
                self.liste.addItem(bilgi)
        else:
            self.liste.addItem("Henüz ödünç alınan kitap yok.")

        self.layout.addWidget(self.liste)
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ana_menu = AnaMenu()
    ana_menu.show()
    sys.exit(app.exec_())