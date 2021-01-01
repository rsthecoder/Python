#--------Opening Files--------#

""" 
You can use Python to read and write the contents of files.
Text files are the easiest to manipulate. Before a file can be edited, it must be opened, using the open function.
"""

myfile = open("filename.txt")

""" 
The argument of the open function is the path to the file. If the file is in the current working directory of the program, you can specify only its name.
"""

#--------Opening Files--------#


""" 
You can specify the mode used to open a file by applying a second argument to the open function.
Sending "r" means open in read mode, which is the default.
Sending "w" means write mode, for rewriting the contents of a file.
Sending "a" means append mode, for adding new content to the end of the file.

Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files).
For example:
"""
# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# binary write mode
open("filename.txt", "wb")


""" 
You can use the + sign with each of the modes above to give them extra access to files. For example, r+ opens the file for both reading and writing.
"""

#--------Opening Files--------#

""" 
Once a file has been opened and used, you should close it.
This is done with the close method of the file object.
"""

file = open("filename.txt", "w")
# do stuff to the file
file.close()

""" 
We will read/write content to files in the upcoming lessons.
"""



#--------Reading Files--------#

""" 
The contents of a file that has been opened in text mode can be read using the read method.
"""

file = open("filename.txt", "r")
cont = file.read()
print(cont)
file.close()

""" 
This will print all of the contents of the file "filename.txt".
"""



#--------Reading Files--------#

""" 
To read only a certain amount of a file, you can provide a number as an argument to the read function. This determines the number of bytes that should be read.
You can make more calls to read on the same file object to read more of the file byte by byte. With no argument, read returns the rest of the file.
"""

file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()

""" 
Just like passing no arguments, negative values will return the entire contents.
"""


#--------Reading Files--------#

""" 
To retrieve each line in a file, you can use the readlines method to return a list in which each element is a line in the file.
For example:
"""
file = open("filename.txt", "r")
print(file.readlines())
file.close()


""" 
You can also use a for loop to iterate through the lines in the file:

In the output, the lines are separated by blank lines, as the print function automatically adds a new line at the end of its output.
"""

file = open("filename.txt", "r")

for line in file:
    print(line)

file.close()  




#--------Writing Files--------#

""" 
To write to files you use the write method, which writes a string to the file.

The "w" mode will create a file, if it does not already exist.
"""

file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()

#--------Writing Files--------#

""" 
When a file is opened in write mode, the file's existing content is deleted.
"""

file = open("newfile.txt", "w")
file.write("Some new text")
file.close()

file = open("newfile.txt", "r")
print("Reading new contents")
print(file.read())
print("Finished")
file.close()



#--------Writing Files--------#

""" 
The write method returns the number of bytes written to a file, if successful.

To write something other than a string, it needs to be converted to a string first.

"""
msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written) # 12
file.close()

#--------Working with Files--------#

""" 
It is good practice to avoid wasting resources by making sure that files are always closed after they have been used. One way of doing this is to use try and finally
"""

try:
   f = open("filename.txt")
   print(f.read())
finally:
   f.close()

""" 
This ensures that the file is always closed, even if an error occurs.
"""


#--------Working with Files--------#

""" 
*** An alternative way of doing this is using with statements. This creates a temporary variable (often called f), which is only accessible in the indented block of the with statement.
"""

with open("filename.txt") as f:
   print(f.read())

""" 
The file is automatically closed at the end of the with statement, even if exceptions occur within it.
"""



