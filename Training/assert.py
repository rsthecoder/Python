"""
Assert deyimi “iddia etmek” anlamına geliyor.
Yani bir iddiada bulunduğumuz zaman, o iddiamız doğruysa sorun yok
ancak yanlışsa AssertionError isimli bir hata alırız.
Konuyla ilgili basit örnekler yapmaya çalışalım.
"""

def fonksiyon(liste):
    for i in liste:
        try:
            assert i <= 5
            #İddianın doğru olduğu durumda, bu aralıkta yeni işlemler de tanımlanabilir.
        except AssertionError:
            print("{} sayısı 5'den büyük".format(i))

liste = [1, 2, 3, 4, 5, 6]
fonksiyon(liste)


#Baska bir ornek

def fonksiyon(liste):
    for i in liste:
        try:
            assert str(i).isnumeric()
            #İddianın doğru olduğu durumda, bu aralıkta yeni işlemler de tanımlanabilir.
        except AssertionError:
            print("{} karakteri sayı değil.".format(repr(i)))

liste = [1, 2, 3, 4, 5, "a"]
fonksiyon(liste)

#Baska bir ornek

liste = [0, 2, 45, 11, 19]
sözlük = {0: "a", 11: "b", 34: "c", 2: "d"}
for i in liste:
    try:
        assert i in sözlük
        #İddianın doğru olduğu durumda, bu aralıkta yeni işlemler de tanımlanabilir.
    except AssertionError:
        print("{} sözlük anahtarı değil.".format(repr(i)))


