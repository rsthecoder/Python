""" Write a program that takes two inputs; one of them is a list and the other is a number, 
and returns the list obtained by shifting the elements in the list n places to the right (left) 
when n is positive (negative). 
Use wrap-around: if an element is shifted beyond the end of the list, 
then continue to shift starting at the beginning of the list. """

while True:
    try:
        
        user_list = list(input("Enter your list: ")) # User enters a list
        
        user_shift = -1 * int(input("Enter a number for rotating: ")) # user enters a number to rotate and * -1 because we want to rotate the list to right or left
        
        new_list =  user_list[user_shift:] + user_list[:user_shift] # getting a new list
        
        print(user_list)
        print(new_list)
        

    except:
        
        print("You made a faulty input, please try again!")
