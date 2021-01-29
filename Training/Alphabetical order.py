# Write a function that takes an input of different words with hyphen (-) in between them and then:

# sorts the words in alphabetical order,
# adds hyphen icon (-) between them,
# gives the output of the sorted words.
# Example:

# Input  >>> green-red-yellow-black-white
# Output >>> black-green-red-white-yellow 

def alphabetical_order(given_words = "green-red-yellow-black-white"): # Takes a string as an argument
    return ("-".join(map(str,sorted(list(given_words.split("-")))))) # Makes a sorted list and then joins with "-" sign

print(alphabetical_order())
    