print("This program will find the sum of all even numbers between the two numbers you selected. \n")

total_sum = 0

while True:
    number_1 = int(input("Enter first number: "))   #User enters a number
    number_2 = int(input("Enter Second number: "))   #User enters a second number

    
     
    try:
        for i in range(number_1, number_2 +1):
            if i % 2 == 0 :
                total_sum += i
        
        print("Sum of all even numbers between " + str(number_1) + " and " + str(number_2) + " is : " + str(total_sum))
    except: 
        print("\nPlease enter a number!")
