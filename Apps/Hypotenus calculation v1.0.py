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

    print("\n"*2 + "Hypotenus length is: " + str(hypotenus))
    time.sleep(1)

    print(input("\nPress any key to a new calculation..."))



