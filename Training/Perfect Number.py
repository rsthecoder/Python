
# Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.

# The smallest perfect number is 6, which is the sum of 1, 2, and 3.

# Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.

# Write a function that finds perfect numbers between 1 and 1000. Check perfect numbers between 1 and 1000 and find the sum of the perfect numbers using reduce and filter functions.

### First Solution ###

def perfect_numbers(given_number = 1000): # Takes 1000 as an argument if not given
    my_list = [x for x in range(1,given_number +1)]  # List comprehension
    result = []

    for i in my_list: # Takes every number between 1-1000
        sum_divisors = 0  # sum of the divisors
        for y in range(1,i): 
            if i % y == 0: # Checking for every proper divisors
                sum_divisors + = y 

        if i == sum_divisors: # Checking the if it is equal to sum of the divisors
            result.append(i)   

    return (', '.join(map(str, result))) # Print list elements seperated with comas

print(perfect_numbers())


### Second Solution -> Reduce and Filter wil be added ###
















