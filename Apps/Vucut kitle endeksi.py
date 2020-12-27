 #bu program vucut kitle endeksini hesaplayacak
 #basitce boy ve kilo degeri girildiginde vki degerini verecek

'''
Beden Kitle İndeksi (BKİ)
18,5 kg/m2’nin altında ise - Zayıf
18,5-24,9 kg/m2 aralığında ise - Sağlıklı Kiloda
25-29,9 kg/m2 aralığında ise - Kilolu
30 kg/m2 ve üzerinde ise kişi Obez olarak sınıflandırılır.

Kaynak https://www.diyetkolik.com/beden-kitle-indeksi-nedir/

'''

print('-' * 50)
print ('Bu Program Vucut Kitle Endeksinizi Hesaplayacak')

while True:
        boy = int( input ("\n" + "Boyunuzu cm degeri olarak giriniz: "))
        kilo = int( input("\n" +  "Kilonuzu rakamla giriniz: "))	
	
        a1 = (boy**2)
        vki = int((kilo / a1) * 100000)
        print(vki)

        #print ('vucut kitle endeksiniz: ' + str(vki) + ' degerinde.' )

        if vki < 185:
                print ('\n' + 'Zayifsin: Mutlaka kilo almalisin.')
        elif vki >= 185 and vki <= 249:
                print('\n' + 'Saglikli kilodasin: Formunu koru')
        elif vki >= 250 and vki <= 299:
                print('\n' + 'Kilolu Birisin Ama Sisman degilsin')
        elif vki >= 300:
                print('\n' + 'Obez - Sisman birisin. Az ye ve Mutlaka diyet yap!!!')

        print('-' * 50)