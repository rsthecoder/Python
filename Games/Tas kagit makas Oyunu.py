from random import randint

#Oyuncularin isimlerini aliyoruz
oyuncu_1_isim = input("Ilk oyuncunun ismini giriniz: ")
oyuncu_2_isim = input("Ikinci oyuncunun ismini giriniz: ")

#Tas Kagit Makas seceneklerimizi belirliyoruz
secenekler = ["Tas","Kagit","Makas"]

# 10 a ulasanin kazanmasi icin skorbordu hazirliyoruz
skor_oyuncu_1 = 0
skor_oyuncu_2 = 0

#Dongumuz basliyor
while True:
    try:
        # Oyuncularin hamleleri her seferde Secenkler listesinden rastgele seciliyor.
        hamle_oyuncu_1 = secenekler[randint(0,2)]
        hamle_oyuncu_2 = secenekler[randint(0,2)]
        #Skor 10 olmadigi durumlarda oyuna devam ediliyor
        if skor_oyuncu_1 < 10 and skor_oyuncu_2 < 10:
            # Oyuncu 1'in kazandigi durumlar belirleniyor
            if (hamle_oyuncu_1 == "Tas" and hamle_oyuncu_2 == "Makas") or (hamle_oyuncu_1 == "Kagit" and hamle_oyuncu_2 == "Tas") or (hamle_oyuncu_1 == "Makas" and hamle_oyuncu_2 == "Kagit") :
                print(oyuncu_1_isim + " hamlesi: " + hamle_oyuncu_1 + " --> Bu elin kazanani: " + oyuncu_1_isim)
                print(oyuncu_2_isim + " hamlesi: " + hamle_oyuncu_2 + "\n")
                skor_oyuncu_1 += 1
            # Oyuncu 2'nin kazandigi durumlar belirleniyor
            elif(hamle_oyuncu_2 == "Tas" and hamle_oyuncu_1 == "Makas") or (hamle_oyuncu_2 == "Kagit" and hamle_oyuncu_1 == "Tas") or (hamle_oyuncu_2 == "Makas" and hamle_oyuncu_1 == "Kagit") :
                print(oyuncu_1_isim + " hamlesi: " + hamle_oyuncu_1 )
                print(oyuncu_2_isim + " hamlesi: " + hamle_oyuncu_2 + "--> Bu elin kazanani: " + oyuncu_2_isim  + "\n")
                skor_oyuncu_2 += 1
            # Her iki durum da gerceklesmemis ise Berabere durumu olusuyor
            else:
                print(oyuncu_1_isim + " hamlesi: " + hamle_oyuncu_1 + "--> Berabere")
                print(oyuncu_2_isim + " hamlesi: " + hamle_oyuncu_2 + "--> Berabere" + "\n")
                skor_oyuncu_1 += 1
                skor_oyuncu_2 += 1
        # Oyuncu 1'in skoru 10 olursa kazandigi mesaji yayinlaniyor
        elif skor_oyuncu_1 == 10 and skor_oyuncu_2 < 10:
            print("-"*50)
            print(oyuncu_1_isim + " toplam puani: " + str(skor_oyuncu_1) + " --> Toplam skorda kazanan->" + oyuncu_1_isim.upper())
            print(oyuncu_2_isim + " toplam puani: " + str(skor_oyuncu_2))
            print("-"*50)
            #Dongunun tekrar devam edebilmesi icin skor'u sifirliyoruz
            skor_oyuncu_1 = 0
            skor_oyuncu_2 = 0
            # Dongu otomatik olarak kendiliginden devam etmemesi icin kullanicidan Enter a basmasini istiyoruz
            input("Bu oyun tamamlandi bir daha oynamak icin Enter'a basiniz: ")
        # Oyuncu 1'in skoru 10 olursa kazandigi mesaji yayinlaniyor
        elif skor_oyuncu_1 < 10 and skor_oyuncu_2 == 10:
            print("-"*50)
            print(oyuncu_1_isim + "  toplam puani: " + str(skor_oyuncu_1))
            print(oyuncu_2_isim + "  toplam puani: " + str(skor_oyuncu_2) + " --> Toplam skorda kazanan->" + oyuncu_2_isim.upper())
            print("-"*50)
            skor_oyuncu_1 = 0
            skor_oyuncu_2 = 0
            input("Bu oyun tamamlandi bir daha oynamak icin Enter'a basiniz: ")
        # Berabere oldugu durumlar belirleniyor
        else:
            print("-"*50)
            print("Dostluk kazandi! Mac sonucu: BERABERE")
            print("-"*50)
            skor_oyuncu_1 = 0
            skor_oyuncu_2 = 0
            input("Bu oyun tamamlandi bir daha oynamak icin Enter'a basiniz: ")
    except:
        print("Bir hata olustu!")
        break
    
