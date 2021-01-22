""" 
first = True
second = False
while first == True:
  print('this is the first level')
  level = input('choose level:\t')
  if level == "second":
    print('going down to second level')
    first = False
    second = True
    while second == True:
      print('this is second level')
      level = input('choose level:\t')
      if level == 'first':
        print('going up to first level')
        first = True
        second = False """


while True:
  print("This is the first level")
  level = input("choose level:\t ")
  while True:
    if level == "second":
      print("this is second level")
      level = input("choose level:\t")
      if level == "first":
        print('going up to first level')
        break
      continue
    break


""" 
while True:
    try:
        secenekler =
Merhaba programin GIRIS ekranindasiniz:

Ogrenci eklemek icin 1 yazip entera basiniz
Ders notu girmek icin 2 yazip entera basiniz

        print(secenekler)
        ilk_secim = int(input("Lutfen seciminizi yapiniz: "))
        while True:
          if ilk_secim == 1:
            print("Ogrenci ekleme ekranina hos geldiniz!")
            print("1- Yeni ogrenci ekle 2- Bir ust menuye don")
            ikinci_secim = int(input("Lutfen seciminizi yapiniz: "))
            if ikinci_secim == 1:
              print("Yeni ogrenci ekleme menusu")
              break
            if ikinci_secim == 2:
              print("Giris ekranina geri donuluyor.")
              break
          if ilk_secim == 2:
            print("Ders notu girme ekranina hos geldiniz!")
            print("1- Final notu gir 2- Bir ust menuye don")
            ikinci_secim = int(input("Lutfen seciminizi yapiniz: "))
            if ikinci_secim == 1:
              print("Final notu ekleme menusu")
              break
            if ikinci_secim == 2:
              print("Giris ekranina geri donuluyor.")
              break
          else:
            print("Yanlis secim yaptiniz tekrar deneyiniz!")
            break
            
    except:
        print("Hatali giris yaptiniz! Tekrar deneyiniz!")

 """


""" first = True
second = True

while first == True:
  print("First While - Main Menu")
  second = True
  while second == True: # Her turlu buradaki While dongusune girecek
    print("Second While - Main Menu")
    secim = int(input("enter 2 to main menu"))
    if secim == 2:
      print(str(secim) + " secenegi ile main menuye gecis yapiliyor!" )
      second = False
  
  print("ikinci while dongusu sonlandi")
  input() """
