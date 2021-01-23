def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return print(result)

while True:
    try:
        number = int(input("Please enter the number: "))
        factorial(number)
    except:
        print("Try again!")

