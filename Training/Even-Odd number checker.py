
while True:
    number = int(input("\nEnter a numnber to check even or odd: "))
    try:
        if number % 2 == 0:
            print("\nNumber is even")
            continue
        else:
            print("\nNumber is an odd number")
            continue
    except:
        print("\nPlease enter a number!")