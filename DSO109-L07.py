"""Practices code DSO109 from lesson 7."""
# DSO109 - Programming Foundations - Python
    # Lesson 7 - Standard Library

# Page 3 - Standard Library

    # str() function
pi = 3.1415650
# numeric variable created

piString = str(pi)
# variable converted to a string and saved as a new variable

print('The value of Pi is', piString)
# printed: The value of Pi is 3.141565


    # min() function
numberList = [33, 19, 25, 7, 18]
# numeric variable created

minNumber = min(numberList)
# minimum value from variable saved to new variable

print('The minimum number in the list is', minNumber)
# printed: The minimum number in the list is 7




# Page 5 - Python Standard Modules
    # import Python sys module
import sys
# module imported

    # call that module
print('Python version:', sys.version)
# Python version: 3.9.13 (main, Aug 25 2022, 18:29:29)
    # [Clang 12.0.0 ]

    # call that module again
print('Interpreter Location:', sys.executable)
# Interpreter Location: /Applications/anaconda3/bin/python

    # import Python keyword module
import keyword
# module imported

    # call that module
print('Keywords: ')
for word in keyword.kwlist:
    print(word)
# Keywords:
    # False
    # None
    # True
    # __peg_parser__
    # and
    # as
    # assert
    # async
    # await
    # break
    # class
    # continue
    # def
    # del
    # elif
    # else
    # except
    # finally
    # for
    # from
    # global
    # if
    # import
    # in
    # is
    # lambda
    # nonlocal
    # not
    # or
    # pass
    # raise
    # return
    # try
    # while
    # with
    # yield

    # call that module again
print(keyword.iskeyword('def'))
# printed: True



# Page 6 - Mathematics

    # math module
    # import module
import math
# module imported

    # floor function
        # note: since entire module was imported, the module name
        # has to preceed the function names, using the dot notation
print('Round the number 8.5 down:', math.floor(8.5))
# printed: Round the number 8.5 down: 8

    # ceil function
print('Round the number 8.5 up:', math.ceil(8.5))
# printed: Round the number 8.5 up: 9

    # pow function
print('5 to the power of 10 =', math.pow(5, 10))
# printed: 5 to the power of 10 = 9765625.0

    # sqrt function
print('The square root of 82 is', math.sqrt(82))
# printed: The square root of 82 is 9.055385138137417


    # random module
import random
# module imported

    # random function
print('A random float between 0- 1.0:', random.random())
# printed: A random float between 0- 1.0: 0.6876872187915776

    # sample function
numbers = random.sample(range(1, 49), 7)

print('Your lucky numbers are:', numbers)
# saved a random sample of #'s to a variable and printed:
    # Your lucky numbers are: [3, 22, 26, 10, 30, 14, 40]




# Page 8 - pip Packages

    # NumPy
pip install numpy
#  installed package, then restarted kernel per terminal
    # recommendation

import numpy as np
# package imported


    # array function
x = np.array([1, 2, 3])

print(x)
# ndarray saved to variable, then variable printed: [1 2 3]
    # note: interesting that it prints w/o commas...

x = np.array([[1, 2, 3], [4, 5, 6]])

print(x)
# ndarray updated and printed


    # ndmin function
x = np.array([range(1,6)], ndmin=2)

print(x)
# ndarray updated and printed




# Page 9 - Accessing Files

    # open, name, and mode functions
file = open('example.txt', 'w')
# file opened in write mode

print('File name:', file.name)
print('File Open Mode:', file.mode)
# printed:
    # File name: example.txt
    # File Open Mode: w


    # testing the print functions to see if it's with actual file
        # name
customName = open('myFile.txt', 'w')

print(customName.name)
# printed: myFile.txt - so it is the actual name :)


    # define a function to check status
def status(file):
    """Check file status"""
    if(file.closed != False):
        return 'Closed'
    else:
        return 'Open'
# function created

    # print status
print('File Status:', status(file))
# printed: File Status: Open


    # close function
file.close()

print('File Status:', status(file))
# printed: File Status: Closed





# Page 10 - Reading and Writing Files
    # additional file functions
story = 'Once upon a time there was\n'
story += 'a dog who loved to play ball.\n'
story += 'This dog could run as fast as the wind.\n'

print(story)
# printed:
    # Once upon a time there was
    # a dog who loved to play ball.
    # This dog could run as fast as the wind.


file = open('story.txt', 'w')
file.write(story)
file.close()

file = open('story.txt', 'r')

for line in file:
    print(line, end = '')
file.close()
# printed:
    # Once upon a time there was
    # a dog who loved to play ball.
    # This dog could run as fast as the wind.


    # alternate option for code above
file = open('story.txt', 'r')

contents = file.read()
print(contents)
file.close()
# printed:
    # Once upon a time there was
    # a dog who loved to play ball.
    # This dog could run as fast as the wind.


    # append to file
file = open('story.txt', 'a')
file.write(story)
file.close()

file = open('story.txt', 'r')

for line in file:
    print(line, end = '')
file.close()
# printed:
    # Once upon a time there was
    # a dog who loved to play ball.
    # This dog could run as fast as the wind.
    # Once upon a time there was
    # a dog who loved to play ball.
    # This dog could run as fast as the wind.





# Page 11 - Updating File Strings
    # using with function for more succinct code, for same as above
newText = 'Python was conceived in the late 1990s by Guido van Rossum'

with open('updating.txt', 'w') as file:
    file.write(newText)
    print('\nFile Now Closed?:', file.closed)
print('File Now Closed?:', file.closed)
# printed:
    # File Now Closed?: False
    # File Now Closed?: True


    # using with function for read
with open('updating.txt', 'r+') as file:
    newText = file.read()
    print('\nString:', newText)
    print('\nPosition In File Now:', file.tell())
    position = file.seek(33)
    print('Position In File Now:', file.tell())
# printed:
    # String: Python was conceived in the late 1990s by Guido van
        # Rossum
    #
    # Position In File Now: 58
    # Position In File Now: 33


    # updating file at defined position
with open('updating.txt', 'r+') as file:
    newText = file.read()
    print('\nString:', newText)
    print('\nPosition In File Now:', file.tell())
    position = file.seek(33)
    print('Position In File Now:', file.tell())
    file.write('1980s')
    file.seek(0)
    newText = file.read()
    print('\nString:', newText)
# Printed:
    # String: Python was conceived in the late 1990s by Guido van
        # Rossum
    #
    # Position In File Now: 58
    # Position In File Now: 33
    #
    # String: Python was conceived in the late 1980s by Guido van
        # Rossum
