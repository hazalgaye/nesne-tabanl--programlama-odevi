import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QMessageBox

class Hasta:
    def __init__(self, isim, tc):
        self.isim = isim
        self.tc = tc
        self.randevu = None

class Doktor:
    def __init__(self, isim, uzmanlik):
        self.isim = isim
        self.uzmanlik = uzmanlik
        self.musaitlik = True

class Randevu:
    def __init__(self, tarih, doktor, hasta):
        self.tarih = tarih
        self.doktor = doktor
        self.hasta = hasta

doktorlar = [Doktor("Ahmet Yılmaz", "Dahiliye"), Doktor("Elif Demir", "Kardiyoloji")]
hastalar = [Hasta("Ayşe Koç", "12345678901"), Hasta("Ali Can", "23456789012")]

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hastane Randevu Sistemi")
        self.setGeometry(100, 100, 300, 300)
        
        layout = QVBoxLayout()

        self.label = QLabel("Bir işlem seçin:")
        layout.addWidget(self.label)

        self.randevu_al_btn = QPushButton("Randevu Al")
        self.randevu_al_btn.clicked.connect(self.randevu_al)
        layout.addWidget(self.randevu_al_btn)

        self.randevu_iptal_btn = QPushButton("Randevu İptal Et")
        self.randevu_iptal_btn.clicked.connect(self.randevu_iptal)
        layout.addWidget(self.randevu_iptal_btn)

        self.hasta_ekle_btn = QPushButton("Hasta Ekle")
        self.hasta_ekle_btn.clicked.connect(self.hasta_ekle)
        layout.addWidget(self.hasta_ekle_btn)

        self.doktor_ekle_btn = QPushButton("Doktor Ekle")
        self.doktor_ekle_btn.clicked.connect(self.doktor_ekle)
        layout.addWidget(self.doktor_ekle_btn)

        self.setLayout(layout)

    def randevu_al(self):
        self.randevu_penceresi = RandevuAlPenceresi()
        self.randevu_penceresi.show()

    def randevu_iptal(self):
        self.iptal_penceresi = RandevuIptalPenceresi()
        self.iptal_penceresi.show()

    def hasta_ekle(self):
        self.hasta_penceresi = HastaEklePenceresi()
        self.hasta_penceresi.show()

    def doktor_ekle(self):
        self.doktor_penceresi = DoktorEklePenceresi()
        self.doktor_penceresi.show()

class RandevuAlPenceresi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Randevu Al")
        self.setGeometry(150, 150, 300, 200)
        layout = QVBoxLayout()

        self.isim_input = QLineEdit()
        self.isim_input.setPlaceholderText("İsim girin")
        layout.addWidget(self.isim_input)

        self.tc_input = QLineEdit()
        self.tc_input.setPlaceholderText("TC kimlik numarası girin")
        layout.addWidget(self.tc_input)

        self.tarih_input = QLineEdit()
        self.tarih_input.setPlaceholderText("Tarih girin (GG/AA/YYYY)")
        layout.addWidget(self.tarih_input)

        self.doktor_input = QLineEdit()
        self.doktor_input.setPlaceholderText("Doktor numarası seçin (1,2...)")
        layout.addWidget(self.doktor_input)

        self.bilgi_label = QLabel(self.musait_doktorlar())
        layout.addWidget(self.bilgi_label)

        self.al_btn = QPushButton("Randevu Al")
        self.al_btn.clicked.connect(self.randevu_al)
        layout.addWidget(self.al_btn)

        self.setLayout(layout)

    def musait_doktorlar(self):
        bilgi = "Müsait Doktorlar:\n"
        for idx, doktor in enumerate(doktorlar):
            if doktor.musaitlik:
                bilgi += f"{idx + 1}. {doktor.isim} ({doktor.uzmanlik})\n"
        return bilgi

    def randevu_al(self):
        isim = self.isim_input.text()
        tc = self.tc_input.text()
        tarih = self.tarih_input.text()
        doktor_secim = int(self.doktor_input.text()) - 1

        hasta = next((h for h in hastalar if h.tc == tc and h.isim == isim), None)
        if hasta and 0 <= doktor_secim < len(doktorlar) and doktorlar[doktor_secim].musaitlik:
            randevu = Randevu(tarih, doktorlar[doktor_secim], hasta)
            hasta.randevu = randevu
            doktorlar[doktor_secim].musaitlik = False
            QMessageBox.information(self, "Başarılı", "Randevunuz alındı.")
            self.close()
        else:
            QMessageBox.warning(self, "Hata", "Bilgiler yanlış veya doktor müsait değil.")

class RandevuIptalPenceresi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Randevu İptal Et")
        self.setGeometry(150, 150, 300, 150)
        layout = QVBoxLayout()

        self.isim_input = QLineEdit()
        self.isim_input.setPlaceholderText("İsim girin")
        layout.addWidget(self.isim_input)

        self.tc_input = QLineEdit()
        self.tc_input.setPlaceholderText("TC kimlik numarası girin")
        layout.addWidget(self.tc_input)

        self.iptal_btn = QPushButton("Randevu İptal Et")
        self.iptal_btn.clicked.connect(self.randevu_iptal)
        layout.addWidget(self.iptal_btn)

        self.setLayout(layout)

    def randevu_iptal(self):
        isim = self.isim_input.text()
        tc = self.tc_input.text()

        hasta = next((h for h in hastalar if h.tc == tc and h.isim == isim), None)
        if hasta and hasta.randevu:
            hasta.randevu.doktor.musaitlik = True
            hasta.randevu = None
            QMessageBox.information(self, "Başarılı", "Randevu iptal edildi.")
            self.close()
        else:
            QMessageBox.warning(self, "Hata", "Randevu bulunamadı.")

class HastaEklePenceresi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hasta Ekle")
        self.setGeometry(150, 150, 300, 150)
        layout = QVBoxLayout()

        self.isim_input = QLineEdit()
        self.isim_input.setPlaceholderText("Hasta ismi girin")
        layout.addWidget(self.isim_input)

        self.tc_input = QLineEdit()
        self.tc_input.setPlaceholderText("TC kimlik numarası girin")
        layout.addWidget(self.tc_input)

        self.ekle_btn = QPushButton("Hasta Ekle")
        self.ekle_btn.clicked.connect(self.hasta_ekle)
        layout.addWidget(self.ekle_btn)

        self.setLayout(layout)

    def hasta_ekle(self):
        isim = self.isim_input.text()
        tc = self.tc_input.text()

        hastalar.append(Hasta(isim, tc))
        QMessageBox.information(self, "Başarılı", "Hasta eklendi.")
        self.close()

class DoktorEklePenceresi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Doktor Ekle")
        self.setGeometry(150, 150, 300, 150)
        layout = QVBoxLayout()

        self.isim_input = QLineEdit()
        self.isim_input.setPlaceholderText("Doktor ismi girin")
        layout.addWidget(self.isim_input)

        self.uzmanlik_input = QLineEdit()
        self.uzmanlik_input.setPlaceholderText("Uzmanlık alanı girin")
        layout.addWidget(self.uzmanlik_input)

        self.ekle_btn = QPushButton("Doktor Ekle")
        self.ekle_btn.clicked.connect(self.doktor_ekle)
        layout.addWidget(self.ekle_btn)

        self.setLayout(layout)

    def doktor_ekle(self):
        isim = self.isim_input.text()
        uzmanlik = self.uzmanlik_input.text()

        doktorlar.append(Doktor(isim, uzmanlik))
        QMessageBox.information(self, "Başarılı", "Doktor eklendi.")
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
