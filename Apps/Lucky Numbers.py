"""
Kerim Sak - Lucky numbers
Write a programme to generate the lucky numbers from the range(n). 
These are generated starting with the sequence s=[1,2,...,n]. 
At the first pass, we remove every second element fromthe sequence, resulting in s2. 
At the second pass, we remove every third element from the sequence s2, resulting in s3, and we proceed in this way until no elements can be removed. 
The resulting sequence are the numbers lucky enough to have survived elimination.
The following example describes the entire process for n=22:
"""
while True:     # Program main loop
    try:        # Try first
        range_number = int(input("\nEnter the range: "))  # We are getting an input from user to calculate Range

        lucky_numbers = [x for x in range(1, range_number + 1)] # We are making a list from 1 to input number

        i = 1
        while len(lucky_numbers) >= i+1: # Checking Length of the list 
            del lucky_numbers[i:range_number:i+1] # Deleting elements
            i += 1

        result = ("\nLucky numbers are: {}".format(lucky_numbers)) # Result
        print(result)

    except:
        print("Hatali giris yaptiniz, lutfen tekrar deneyiniz!")

