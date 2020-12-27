import time # Add to use sleep function.

#alt shift ve yon tuslari ile satiri asagi ve yukari kopyalar
#if yazdiktan sonra 

# Program bir Login yonetimi yapacak
# Eger kullanici ve soyadi dogru ise giris yapilmis olacak
# Eger isim dogru soyad yanlis ise Soyad hatali olarak verilecek
# Eger 

while True:
    name = input("\nWhat is your name: ")
    password = input("\nWhat is your password: ")
    try:
        if name == "kerim" and password == "sak":
            print("\nWelcome " + name)
            pass
        elif name != "kerim" and password != "sak":
            print("\nPlease check your name and password!")
            continue
        elif name == "kerim" and password != "sak":
            print("\npassword is not correct, please check your password!")
            continue
        elif name != "kerim" and password == "sak":
            print("\nName is not correct, please check your name")
            continue
    except ValueError:
        print("\nPlease enter only your name!")

    print("\nYou are logged in, Now you can use the app further\n")
    print(input("\nChoose en option below: "))
    
    