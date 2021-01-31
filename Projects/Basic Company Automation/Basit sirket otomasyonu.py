# https://www.youtube.com/watch?v=9gCM4Fe4mSw&list=PLK6Whnd55IH5i1klkNSBDasIaO77l-Bm9&index=32


class Sirket():
    def __init__(self,ad):
        self.ad = ad
        self.calisma = True

    def program(self):
        secim = self.menuSecim()

        if secim == 1:
            self.calisanEkle()
        if secim == 2:
            self.calisanCikar()
        if secim == 3:
            self.verilecekMaasGoster()
        if secim == 4:
            self.maaslariVer()
        if secim == 5:
            self.masrafGir()
        if secim == 6:
            self.gelirGir()

    def menuSecim(self):
        
        secim = int(input("\n*** {} Otomasyonuna hos geldiniz ***\n\n1- Calisan Ekle\n2-Calisan Cikar\n3-Verilecek Maas Goster\n4- Maaslari Ver\n5-Masraf Gir\n6- Gelir gir\n\nSeciminizi giriniz: ".format(self.ad)))
        
        while secim < 1 or secim > 6:
            secim = int(input("Lutfen 1 ile 6 arasinda belirtilen seceneklerden birini giriniz: "))        
        
        return secim

    def calisanEkle(self):
        id = 1
        ad = input("Calisanin adini giriniz: ")
        soyad = input("Calisanin soyadini giriniz: ")
        yas = int(input("Calisanin yasini giriniz: "))
        cinsiyet = input("Calisanin cinsiyetini giriniz: ")
        maas = int(input("Calisanin maasini giriniz: "))

        with open("calisanlar.txt","r") as dosya: # Burada dosyanin bos olma durumunu kontrol etmek icin yazdik
            calisanListesi = dosya.readlines() # dosyayi acip readlines ile satirlara bakiyor

        if len(calisanListesi) == 0: # Eger calisanlar listesi bos ise o zaman id 1 olacak
            id = 1
        else:
            with open("calisanlar.txt", "r") as dosya:
                id = int(dosya.readlines()[-1].split(")")[0]) + 1

        with open("calisanlar.txt","a+") as dosya:
            dosya.write("{}) {}-{}-{}-{}-{}\n".format(id, ad.capitalize(), soyad.capitalize(), yas, cinsiyet,maas))# \n onemli cunku bir alt satira gececek



    def calisanCikar(self):
        pass

    def verilecekMaasGoster(self, hesap = "a"):
        """ hesap: a ise aylik, y ise yillik """
        pass

    def maaslariVer(self):
        pass

    def masrafGir(self):
        pass

    def gelirGir(self):
        pass




sirket = Sirket("Kerim A.S.")

while sirket.calisma:
    sirket.program()


        