from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QTextEdit

class Urun:
    def _init_(self, ad, stok):
        self.ad = ad
        self.stok = stok

    def stok_guncelle(self, miktar):
        self.stok += miktar

class StokSistemi(QWidget):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("Stok Takip Sistemi")
        self.urunler = {}

        self.layout = QVBoxLayout()

        self.ad_label = QLabel("Ürün Adı:")
        self.ad_input = QLineEdit()
        self.layout.addWidget(self.ad_label)
        self.layout.addWidget(self.ad_input)

        self.stok_label = QLabel("Stok Miktarı:")
        self.stok_input = QLineEdit()
        self.layout.addWidget(self.stok_label)
        self.layout.addWidget(self.stok_input)

        self.urun_ekle_btn = QPushButton("Ürün Ekle")
        self.urun_ekle_btn.clicked.connect(self.urun_ekle)
        self.layout.addWidget(self.urun_ekle_btn)

        self.siparis_label = QLabel("Sipariş Ürün Adı:")
        self.siparis_input = QLineEdit()
        self.layout.addWidget(self.siparis_label)
        self.layout.addWidget(self.siparis_input)

        self.siparis_btn = QPushButton("Sipariş Oluştur")
        self.siparis_btn.clicked.connect(self.siparis_olustur)
        self.layout.addWidget(self.siparis_btn)

        self.stok_goster_btn = QPushButton("Stok Durumunu Göster")
        self.stok_goster_btn.clicked.connect(self.stok_goster)
        self.layout.addWidget(self.stok_goster_btn)

        self.stok_text = QTextEdit()
        self.stok_text.setReadOnly(True)
        self.layout.addWidget(self.stok_text)

        self.setLayout(self.layout)

    def urun_ekle(self):
        ad = self.ad_input.text()
        try:
            stok = int(self.stok_input.text())
            if ad and stok >= 0:
                if ad in self.urunler:
                    self.urunler[ad].stok_guncelle(stok)
                else:
                    self.urunler[ad] = Urun(ad, stok)
                QMessageBox.information(self, "Başarılı", f"{ad} ürünü eklendi.")
            else:
                QMessageBox.warning(self, "Hata", "Geçerli bir ürün adı ve stok giriniz.")
        except ValueError:
            QMessageBox.warning(self, "Hata", "Stok miktarı bir sayı olmalıdır.")

    def siparis_olustur(self):
        ad = self.siparis_input.text()
        if ad in self.urunler:
            if self.urunler[ad].stok > 0:
                self.urunler[ad].stok_guncelle(-1)
                QMessageBox.information(self, "Sipariş", f"{ad} ürünü için sipariş oluşturuldu.")
            else:
                QMessageBox.warning(self, "Stok Yok", f"{ad} ürününün stoğu tükenmiş.")
        else:
            QMessageBox.warning(self, "Bulunamadı", "Bu isimde bir ürün yok.")

    def stok_goster(self):
        self.stok_text.clear()
        if not self.urunler:
            self.stok_text.setText("Henüz ürün eklenmedi.")
        else:
            for urun in self.urunler.values():
                self.stok_text.append(f"Ürün: {urun.ad} - Stok: {urun.stok}")

if __name__ == "_main_":
    app = QApplication([])
    pencere = StokSistemi()
    pencere.show()
    app.exec_()