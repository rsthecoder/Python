""" Write a code snippet that inputs a sentence from the user, 
then uses a dictionary to summarize the number of occurrences of each letter. 
Ignore case, ignore blanks and assume the user doesnot enter any punctuation. 
Display a two-column table of the letters and their counts with the letters in sorted order. """

while True:
    try:
        user_sentence = input("Please write a sentence to count the letters: ").lower()  # User enters a sentence
        result_dict = {} # Empty dictionary
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # Full alphabet

        for i in user_sentence:
            if i == " " or i not in alphabet: # Fout check for spaces and other characters
                continue # Dont count it if it is not a letter

            letter_count = {i:user_sentence.count(i)} # Making an element and then counting it
            result_dict.update(letter_count) # If the key is in the dictionary, it updates the key with the new value.

        print(sorted(result_dict.items())) # printing sorted item -> https://stackoverflow.com/questions/9001509/how-can-i-sort-a-dictionary-by-key
    except:
        print("You made a faulty inpust, Please try again!")

