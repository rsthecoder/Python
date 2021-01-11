"""
2- Ders Puani Hesaplama
Kullanıcıdan Adi, Soyadi, Ogrenci Numarasi, 4 ders adi, bu derslerin Vize ve Final notlari istenecektir. 
Vize notunun % 40′ı ile Final Notunun %60′ınin toplamı yil sonu ortalamasini verecektir. 
Ortalama 50‘den küçükse ekranda “KALDI“, 50 ve üstüyse ekranda “GEÇTİ” yazdırılacaktır. 
Bu yazdirma islemi 4 ders icinde yapilacak ve dersler alt alta yazdirilacaktir.
"""
while True:
    try:
        ad_soyad= input("\nAdinizi ve Soyadinizi giriniz: ")
        og_no = input("\nOgrenci numaranizi giriniz: ")

        dersler = []
        vizeler = []
        finaller = []
        notlar_sonuc = []

        for i in range(1,5):
            print("-"*50)
            ders = input(str(i) + ". dersin adini giriniz: ")
            dersler.append(ders)
            vize = int(input(ders + " dersi Vize notunuzu giriniz: "))
            vizeler.append(vize)
            final = int(input(ders + " dersi Final notunuzu giriniz: "))
            finaller.append(final)
            print("")

        for i in range(4):
            notlar_sonuc.append(vizeler[i]*0.4 + finaller[i]*0.6)
            if notlar_sonuc[i] >= 50:
                print(dersler[i] + " dersinden " + str(notlar_sonuc[i]) + " notu ile GECTINIZ!")
            elif notlar_sonuc[i] < 50:
                print(dersler[i] + " dersinden " + str(notlar_sonuc[i]) + " notu ile malesef KALDINIZ!")
        
    except:
        print("Hatali giris yaptiniz!")




    