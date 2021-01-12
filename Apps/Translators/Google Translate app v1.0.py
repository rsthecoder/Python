# pip install googletrans==3.1.0a0
# https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group
from googletrans import Translator

#translator = Translator()

translator = Translator()

while True:
    giris = """
Ingilizce-Turkce ceviri icin 1 'e basiniz
Turkce-Ingilizce ceviri icin 2 'ye basiniz


---Ilk secimi yaptiktan sonra tekrar Dil secimine geri donmek icin 3 'e basiniz---

Secimi yapiniz:"""
    print(giris)
    secim = int(input(""))
    loop = True

    while loop:
        try:
            if secim == 1:
                print("\nIngilizceden Turkceye ceviri yapilacaktir!")
                text_1 = input("Cevirisini gormek istediginiz ingilizce kelimeyi veya cumleyi giriniz: ")
                if text_1 == "3":
                    print("3'e basildi!")
                    loop = False
                sonuc = translator.translate(text_1, src = "en", dest = "tr")
                print("\n" + sonuc.text + "\n" )
            elif secim == 2:
                print("\nTurkceden Ingilizceye ceviri yapilacaktir!")
                text_2 = input("Cevirisini gormek istediginiz Turkce kelimeyi  veya cumleyi giriniz: ")
                if text_2 == "3":
                    print("3'e basildi!")
                    loop = False
                sonuc = translator.translate(text_2, src = "tr", dest = "en")
                print("\n" + sonuc.text + "\n" )

        except:
            print("Hatali giris yaptiniz lutfen tekrar deneyiniz!")

print("looptan cikildi")
input("Enter a bas ve cik")




