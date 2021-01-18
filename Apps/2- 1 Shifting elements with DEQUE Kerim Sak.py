""" Write a program that takes two inputs; one of them is a list and the other is a number, 
and returns the list obtained by shifting the elements in the list n places to the right (left) 
when n is positive (negative). 
Use wrap-around: if an element is shifted beyond the end of the list, 
then continue to shift starting at the beginning of the list. """

import collections # importing collections module

while True:
    try:
        user_list = list(input("Enter a list: ")) # user enters a list

        a_list = collections.deque(user_list) # making a Deque list

        shift = int(input("Shift: ")) # user enters a number to rotate the list

        a_list.rotate(shift) # using rotate method

        print(list(a_list)) # printing the list

    except:
        print("You made a faulty input, please try again!")

