while True:   # True olldugu surece calisacak
    try:   # once bunu deneyecek ama baska bir secenek olursa Except'e gececek
        process = int(input("\nSelect a number between 1-5: "))  # Process ile 1-5 arasinda bir secenek girmesini istiyoruz
        if process < 1 or process > 5:  
            print("\nNumber must be between 1-5. Please select correct numer!")
            continue   # Continue ile girilen rakam 1 -5 arasinda degilse tekrar basa donecek

        #break    # Girilen rakam 1-5 arasinda ise While dongusunu sonlandiracak.
    except ValueError:   # Eger integer'a cevirilemeyen bir sey girildiyse hata ver
        print("\nIt must be a number. Please choose a correct type!")


        
