def asal_sayi_kontrol():
    sayi = int(input("Lutfen bir sayi giriniz:\t "))
    sonuc_listesi = []
    for i in range(1,sayi):
        if (sayi % i) == 0:
            sonuc_listesi.append(i)
    
    if len(sonuc_listesi) == 1:
        sonuc = str(sayi) + " sayisi ASAL "
        return sonuc
    else:
        sonuc = str(sayi) + " sayisi ASAL DEGIL"
        return sonuc

while True:
    try:
        print(asal_sayi_kontrol())
    except:
        print("Hatali giris yaptiniz!")

inpput()