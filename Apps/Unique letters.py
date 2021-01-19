""" Write a program that takes in two words as input and returns a list containing three elements, in the following order:

Shared letters between two words.
Letters unique to word 1.
Letters unique to word 2.
Each element of the output should have unique letters, and should be alphabetically sorted. Useset operations. 
The strings will always be in lowercase and will not contain any punctuation. """
while True:
    try:
        
        first_word = set(input("Enter first word: ")) # user enters first word
        second_word = set(input("Enter second word: ")) # user enters second word

        words_intersection = "".join(sorted(first_word & second_word)) # We are making a intersection + sort + join method
        first_difference = "".join(sorted(first_word - second_word)) # We are making a difference + sort + join method
        second_difference = "".join(sorted(second_word - first_word)) # We are making a difference + sort + join method

        result = [words_intersection,first_difference,second_difference] # new list with result
        print(result)

    except:
        print("You made a falty input. Please try again!")



