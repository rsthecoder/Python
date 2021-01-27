# Write a function that controls the given inputs whether they are equal to their reversed order or not.
# Example:
# Input  >>> madam, tacocat, utrecht 
# Output >>> True, True, False


def equal_reverse(*words): # More then one input 
    check_list = [] # Empty list
    for word in words:
        reversed = word[::-1] # reversed word
        if word == reversed:  # If word is equal to reversed order
            check_list.append("True")  # add True to list
        else: # if not equal
            check_list.append("False") # add False to list
    return(", ".join(map(str,check_list))) # print list items comma separated


print(equal_reverse('madam', "tacocat", "utrecht"))
print(equal_reverse("seles", "merhaba", "beb", "madam"))
