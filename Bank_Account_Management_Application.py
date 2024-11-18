class BankaHesabi:
    def __init__(self, hesap_no, bakiye = 0):
        self.hesap_no = hesap_no
        self.bakiye = bakiye

    def para_yatir(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            print(f"{miktar} TL hesaba yatırıldı. Yeni Bakiye: {self.bakiye} TL")
            
        else: 
            print("Geçersiz miktar. Pozitif bir değer girin.")

    def para_cek(self, miktar):
        if miktar > 0:
            if miktar <= self.bakiye:
                self.bakiye -= miktar 
                print(f"{miktar} TL hesaptan çekildi. Kalan Bakiye: {self.bakiye} TL")
                
            else:
                print("Yetersiz bakiye. Çekmek istediğiniz miktar, bakiyenizden fazla.")

        else:
            print("Geçersiz miktar. Pozitif bir değer girin.")

    def  bakiye_goster(self):
        print(f"Mevcut Bakiye: {self.bakiye} TL")

hesaplar = {}

while True:
    print("\nAna Menü")
    print("a.Hesap Oluştur")
    print("b.Para Yatır")
    print("c.Para Çek")
    print("d.Bakiyeyi Göster")
    print("e.Çıkış")

    secim = input("Bir Seçenek Girin(a/b/c/d/e):")

    if secim == "a":
        hesap_no = input("Hesap numarasını girin:").strip()
        if hesap_no in hesaplar:
            print("Bu hesap numarası zaten mevcut!")

        else:
            hesap = BankaHesabi(hesap_no)
            hesaplar[hesap_no] = hesap
            print(f"{hesap_no} numaralı hesap oluşturuldu.")

    elif secim == "b":
        hesap_no = input("Hesap numarasını girin:").strip()
        if hesap_no in hesaplar:
            miktar = float(input("Yatırılacak miktarı girin:"))
            hesaplar[hesap_no].para_yatir(miktar)

        else: 
            print("Hesap bulunamadı!")

    elif secim == "c":
        hesap_no = input("Hesap numarasını girin:").strip()
        if hesap_no in hesaplar:
            miktar = float(input("Çekilecek miktarı girin:"))
            hesaplar[hesap_no].para_cek(miktar)

        else:
            print("Hesap bulunamdı.")

    elif secim == "d":
        hesap_no = input("Hesap numarasını girin:").strip()
        if hesap_no in hesaplar:
            hesaplar[hesap_no].bakiye_goster()

        else:
            print("Hesap bulunamadı.")

    elif secim == "e":
        print("Programdan çıkılıyor...")
        break
        
    else:
        print("Geçersiz seçenek! Lütfen geçerli bir seçenek girin.")
