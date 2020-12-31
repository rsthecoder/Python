

def hello():
    print("Hello world!")

hello()

# hello() We can  not call the function before define it (At first line we can not call the function)

input()

def print_with_exclamation(word):
   print(word + "!")
    
print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")

input()


def print_sum_twice(x, y):
   print(x + y)
   print(x + y)

print_sum_twice(5, 8)

input()

def function(variable):  # Takes one argument
    variable += 1
    print(variable)

function(7)

input()

#Function voor even numbers

def even(x):
    
    if x % 2 == 0:
        print("Number is Even.")
    else:
        print("Number is Odd")

even(5)
even(6)
input()



