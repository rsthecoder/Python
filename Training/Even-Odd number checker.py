
while True:
    number = int(input("\nEnter a numnber to check even or odd: ")) #User enters a number
    try:
        if number % 2 == 0: # then this is an even number
            print("\nNumber is even")
            continue
        else:  # then this is an odd number
            print("\nNumber is an odd number")
            continue
    except: 
        print("\nPlease enter a number!")
