
while True:
    sayi_1 = int(input("sayi giriniz:"))
    sayi_2 = int(input("sayi giriniz:"))
    sayi_3 = int(input("sayi giriniz:"))
    
    if sayi_1 < sayi_2 and sayi_1 > sayi_3:
        print(sayi_1)
    elif sayi_1 > sayi_2 and sayi_1 <sayi_3:
        print(sayi_1)

    elif sayi_2 < sayi_1 and sayi_2 > sayi_3:
        print(sayi_2)
    elif sayi_2 > sayi_1 and sayi_2 <sayi_3:
        print(sayi_2)

    elif sayi_3 < sayi_2 and sayi_3 > sayi_1:
        print(sayi_3)
    elif sayi_3 > sayi_2 and sayi_3 <sayi_1:
        print(sayi_3)