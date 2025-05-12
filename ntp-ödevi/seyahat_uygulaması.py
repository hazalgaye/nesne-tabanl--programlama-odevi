from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit

# Seyahat Sınıfı
class Seyahat:
    def _init_(self, ad):
        self.ad = ad
        self.rotalar = []
        self.konaklamalar = []

    def rota_ekle(self, rota):
        self.rotalar.append(rota)

    def konaklama_ekle(self, konaklama):
        self.konaklamalar.append(konaklama)

    def bilgileri_goster(self):
        bilgi = f"Seyahat Adı: {self.ad}\n"
        bilgi += "Rotalar:\n"
        for rota in self.rotalar:
            bilgi += f"- {rota.detaylar}\n"
        bilgi += "Konaklamalar:\n"
        for konaklama in self.konaklamalar:
            bilgi += f"- {konaklama.tesis_adi} ({konaklama.fiyat} TL)\n"
        return bilgi

# Rota Sınıfı
class Rota:
    def _init_(self, detaylar):
        self.detaylar = detaylar

# Konaklama Sınıfı
class Konaklama:
    def _init_(self, tesis_adi, fiyat):
        self.tesis_adi = tesis_adi
        self.fiyat = fiyat

# Ana Uygulama Penceresi
class SeyahatUygulamasi(QWidget):
    def _init_(self):
        super()._init_()

        self.seyahatler = []

        self.setWindowTitle("Seyahat Planlama Uygulaması")
        self.setGeometry(100, 100, 400, 400)

        self.layout = QVBoxLayout()

        self.label_seyahat = QLabel("Seyahat Adı:")
        self.input_seyahat = QLineEdit()

        self.label_rota = QLabel("Rota Detayı:")
        self.input_rota = QLineEdit()

        self.label_konaklama = QLabel("Konaklama Tesisi Adı:")
        self.input_konaklama = QLineEdit()

        self.label_fiyat = QLabel("Konaklama Fiyatı:")
        self.input_fiyat = QLineEdit()

        self.buton_kaydet = QPushButton("Seyahati Kaydet")
        self.buton_kaydet.clicked.connect(self.seyahat_kaydet)

        self.buton_listele = QPushButton("Seyahatleri Listele")
        self.buton_listele.clicked.connect(self.seyahatleri_listele)

        self.text_alan = QTextEdit()
        self.text_alan.setReadOnly(True)

        self.layout.addWidget(self.label_seyahat)
        self.layout.addWidget(self.input_seyahat)
        self.layout.addWidget(self.label_rota)
        self.layout.addWidget(self.input_rota)
        self.layout.addWidget(self.label_konaklama)
        self.layout.addWidget(self.input_konaklama)
        self.layout.addWidget(self.label_fiyat)
        self.layout.addWidget(self.input_fiyat)
        self.layout.addWidget(self.buton_kaydet)
        self.layout.addWidget(self.buton_listele)
        self.layout.addWidget(self.text_alan)

        self.setLayout(self.layout)

    def seyahat_kaydet(self):
        seyahat_adi = self.input_seyahat.text()
        rota_detay = self.input_rota.text()
        konaklama_adi = self.input_konaklama.text()
        konaklama_fiyat = self.input_fiyat.text()

        if seyahat_adi and rota_detay and konaklama_adi and konaklama_fiyat:
            yeni_seyahat = Seyahat(seyahat_adi)
            yeni_rota = Rota(rota_detay)
            yeni_konaklama = Konaklama(konaklama_adi, konaklama_fiyat)

            yeni_seyahat.rota_ekle(yeni_rota)
            yeni_seyahat.konaklama_ekle(yeni_konaklama)

            self.seyahatler.append(yeni_seyahat)

            self.input_seyahat.clear()
            self.input_rota.clear()
            self.input_konaklama.clear()
            self.input_fiyat.clear()

            self.text_alan.append(f"'{seyahat_adi}' seyahati kaydedildi!\n")
        else:
            self.text_alan.append("Lütfen tüm alanları doldurun!\n")

    def seyahatleri_listele(self):
        self.text_alan.clear()
        for seyahat in self.seyahatler:
            self.text_alan.append(seyahat.bilgileri_goster())
            self.text_alan.append("-" * 30)


app = QApplication([])
pencere = SeyahatUygulamasi()
pencere.show()
app.exec_()