# this program calculates the hypotenus
# we are going to use math -> sqrt() function to calculate hypotenus

#To-Do
#Add input check -> integer


from math import sqrt
import time, sys

while True:
    short_edge = int(input("\nEnter the short edge length: "))
    long_edge = int(input("\nEnter the long edge length: "))
    
    print("\nThe hypotenuse is calculating...")
    time.sleep(2)

    hypotenus = float(sqrt((short_edge**2) + (long_edge**2)))

    result = "\nHypotenus length is: " + str(hypotenus)

    def print_slow(str):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.1)
        print("")

    print_slow(result)

    # print("\n"*2 + "Hypotenus length is: " + str(hypotenus))

    print(input("\nPress any key to a new calculation..."))



