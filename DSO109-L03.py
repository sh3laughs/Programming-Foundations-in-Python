# DSO109 - Programming Foundations - Python
    # Lesson 3 - Lists and Loops

# Page 3 - What is a List?

# Calling split on this string variable (myMessage) in prior lesson
    # resulted in the creation of a list (splitAtSpaces)

myMessage = 'Split these words for me'
splitAtSpaces = myMessage.split()
print(splitAtSpaces)
# variable created with a string, separate variable created with that
    # string split into separate values in a list, then that second
    # variable printed


# From workshop - https://vimeo.com/439142696

# Let's set up classes for a video game. They have different types
    # of characters you can play. Barbarian!

    # Her original code, that should run w/o errors (through line
        # 63)
    # In actuality.. it doesn't run and I couldn't figure out why
        # I fixed a few errors, which was the point of the workshop
        # but got stuck on "AttributeError: 'Barbarian' object has
        # no attribute 'name'" and gave up since we haven't learned
        # classes yet...
    # UPDATE: after learning about classes in lesson 6, I was able
        # to fix the issues in the code so that it now successfully
        # runs :)

# Define the barbarian class
class Barbarian:

    # This is my initialization statement
    def __init__(self, name, can_read, weapon, enemies_vanquished):
        self.name = name
        self.can_read = can_read
        self.weapon = weapon
        self.enemies_vanquished = enemies_vanquished

    # This is a function
    def Victory(self):
        print(self.name + ' the barbarian has had victory over ' +
              self.enemies_vanquished + ' enemies with a ' +
              self.weapon + '!')

    def educated(self):
        if self.can_read == True:
            print('Wow! I can\'t believe ' + self.name +
                  ' can read!')

# Create an instance of that class

Conan = Barbarian('Conan', True, 'sword', '721')
Barbarella = Barbarian('Barbarella', False, 'spear', '100')

print(Conan.name)
print(dir(Conan))

# Call that function

Conan.Victory()
Conan.educated()

Barbarella.Victory()
Barbarella.educated()




# Page 4 - Creating a List

    # Mixed data list
anotherVariable = 'Hello world'
myList = ['String', 3, 7.5, anotherVariable]
# string variable created, then added as one object in list of
    # another new variable - other list objects are a string, a
    # float, and an integer

print(myList)
# variable printed


    # All String List
planets = ['Earth', 'Mars', 'Saturn', 'Venus']
print(planets)
# variable created and printed


    # All Number List
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
# variable created and printed


    # Create a few lists in your lesson_3.py file and print them
fruits = ['love', 'peace', 'patience', 'others ;)']
print(fruits)

nums = ['ice cream', 11, 35]
print(nums)

things = [fruits, nums, 'other stuff', 29]
print(things)
# lists created and printed



# Page 6 - Nested and Empty Lists

    # Nested Lists
ourWorld = ['Earth', ['United States', 'Canada', 'Mexico'],
            [1, 2, 3]]
print(ourWorld)
# list created which includes another list as one of its objects,
    # then printed


    # Empty Lists
myEmptyList = []
# empty list created



# Page 7 - Tuples

myTuple = ('doctor', 'nurse', 'PA')
print(myTuple)
# tuple created and printed


    # Empty Tuples
emptyTuple = ()
# empty tuple created


    # Tuple with One Element
oneItemTuple = ('just me',)
print(oneItemTuple)
# tuple created and printed


    # Mixed Data Type Tuples

        # you've already seen a string tuple
stringTuple = ('this', 'contains', 'string', 'values')
# tuple created


    # you can, of course, create tuples with numbers
numberTuple = (23, 23.5, 9, 144)
# tuple created


    # like lists, you can create tuples with a mix of types
mixedTuple = ('Bob', 33, 'Sally', 29, 'Spike', 8)
# tuple created



# Page 9 - Lists and Tuples Indexing

    # Len to find length
colorsList = ['red', 'green', 'blue', 'yellow']
numColors = len(colorsList)
print(numColors)
# variable created, then a second variable created with the # of
    # objects in that variable, and that second variable printed


    # Accessing Items - Indexing

        # print the third item of the list
print(colorsList[2])
# 3rd item in list - blue - printed

        # print the second item of the tuple
numbersTuple = (22, 33, 44, 55)
print(numbersTuple[1])
# list created, and 2nd item - 33 - printed


    # Accessing the Last Item in a List or Tuple

        # print the last item of the list
print(colorsList[-1])
# last item in list printed

        # print the last item of the tuple
print(numbersTuple[-1])
# last item in list - 55 - printed

        # access the last item with index `-1`
firstFromEnd = colorsList[-1]
# variable created with last item from a list

        # access the next-to-last item with index `-2`
secondFromEnd = colorsList[-2]
# variable created with 2nd to last item from a list

        # access the second from the last item with index `-3`
thirdFromEnd = colorsList[-3]
# variable created with 3rd to last item from a list

print(firstFromEnd)
print(secondFromEnd)
print(thirdFromEnd)
# last 3 created variables printed


    # Accessing Multiple Items Within a Range

        # get the first three items
firstThreeItems = colorsList[0:3]
# list created w/ 1st three items from another list

        # get the middle two items
middleTwoItems = colorsList[1:3]
# list created w/ 2nd and 3rd items from another list

print(firstThreeItems)
print(middleTwoItems)
# last 2 created variables printed




# Page 10 - Modifying Lists

    # Modifying an Item in a List

        # the starting list
contacts = ['Sally', 'Bob', 'Mary', 'Steven']
# list created

        # Bob prefers to go by "Robert"
            # Bob is at index 1 in the list
contacts[1] = 'Robert'
# replaced 2nd object in list - Bob - with new value

print(contacts)
# printed list


colorsList = ['white', 'white', 'white', 'white']
print(colorsList)
# list created and printed

colorsList[0] = 'red'
colorsList[1] = 'green'
colorsList[2] = 'blue'
colorsList[3] = 'yellow'
print(colorsList)
# 1st- 4th objects in list updated, then list printed

colorsList[-1] = 'purple'
print(colorsList)
# last object in list updated, then list printed



# Page 11 - Adding an Item to the End of the List
myString = 'Hello there Bob'
# variable created


    # splits string into list using space as the delimiter/separator
myStringItems = myString.split()
print(myStringItems)
# created a list from a string and saved it as a new variable, then
    # printed that new variable

    # but we forgot Sally!
        # add 'and' and 'Sally' to the list
myStringItems.append('and')
myStringItems.append('Sally')

print(myStringItems)
# added two new objects to the end of the list, then printed list


numbers = [1, 2, 3, 4, 5]
# list created

    # add 6 to the end
numbers.append(6)
# object added to the end of the list

    # add 'seven' to the end
numbers.append('seven')
print(numbers)
# object added to the end of the list and list printed

    # Append three new elements to the end of a list and print your
        # list
numbers.append('elevensies')
numbers.append('skipped a few')
numbers.append('100')
print(numbers)
# 3 new objects added to list, and list printed



    # Inserting an Item Into the List
myList = [1, 2, 4]
# list created

    # Oops! Forgot 3!
myList.insert(2, 3)
print(myList)
# object added as the 3rd option in a list, then the list printed

    # add 'zero' to the beginning of the list
myList.insert(0, 'zero')
# added object as the 1st item in a list

    # insert `four' at index 4
myList.insert(4, 'four')
# added object as the 5th item in a list

print(myList)
# printed list, including newly added objects



# Page 13 - Removing an Item From a List

    # When You Know the Index - del

numbers = [1, 2, 3, 4]
# list created

    # delete item at index 2
del numbers[2]
print(numbers)
# 3rd item - 3 - deleted from list, then updated list printed


    # the position of value 4 has changed
        # its index went from 3 to 2, due to the deletion

    # delete the first item
del numbers[0]
print(numbers)
# 1st item - 1 - deleted from list, then updated list printed

    # delete the last item
del numbers[-1]
print(numbers)
# last item - 4 - deleted from list, then updated list printed


    # When You Don't Know the Index - .remove()
colors = ['red', 'blue', 'yellow', 'green']
colors.remove('yellow')
print(colors)
# list created, object - 'yellow' - removed, and updated list printed


# From workshop - https://vimeo.com/428204013
variableFun = 'Woot!'
myFirstList = [22, 12, 'Happy', variableFun]
print(myFirstList)
# variable created; then a list created which includes some integers,
    # a string, and that variable; then the list printed

nestedList = [['birds', 'nest', 'so'], 'do', 'lists']
print(nestedList)
# list created which includes another list as one of its objects,
    # then printed

emptyListSyndrome = []
print(emptyListSyndrome)
# empty list created and printed

print(len(myFirstList))
# length - 4 - of list printed

print(myFirstList[0])
# 1st item in list - 22 - printed

print(myFirstList[3])
# 4th item in list - Woot! - printed

print(myFirstList[-1])
# last item in list - Woot! - printed

print(myFirstList[0:1])
# first item in list - 22 - printed

print(myFirstList[0:2])
# first 2 items in list - [22, 12] - printed

print(myFirstList[1:3])
# 2nd and 3rd items in list - [12, 'Happy'] - printed

myFirstList[0] = 21
print(myFirstList)
# first 1 item in list updated, and list printed

myFirstList.append('Just added this!')
print(myFirstList)
# new string added to the end of list, and list printed

print(myFirstList[1])
del myFirstList[1]
print(myFirstList)
# 2nd item in list - 12 - printed, then deleted, then updated list
    # printed

myFirstList.remove('Woot!')
print(myFirstList)
# string deleted from list, then updated list printed

onlyNumbers = [1, 5, 9, 12, 2]
print(sorted(onlyNumbers))
print(onlyNumbers)
# list of integers created and printed, first in ascending order,
    # then in indexed order

onlyNumbers.sort()
print(onlyNumbers)
# indexed order updated to be ascending for list, then updated list
    # printed

print(sorted(onlyNumbers, reverse=True))
print(onlyNumbers)
# list of integers created and printed, first in descending order,
    # then in indexed order

onlyNumbers.sort(reverse=True)
print(onlyNumbers)
# indexed order updated to be descending for list, then updated list
    # printed




# Page 15 - Creating a List from a Range of Numbers

    # Storing Range as a List
numbers = list(range(1, 11))
print(numbers)
# 1-10 range created as a list and printed

    # Storing Range as a Variable
theRange = range(1, 11)
print(theRange)
# 1-10 range saved as a variable (not a list!) and variable printed

    # Range with No Start Value
noStartRange = range(5)
numbers = list(noStartRange)
print(numbers)
# 0-4 saved as that range (not a list!), then saved by another name
    # as a list, and that list printed

    # Specify the Increment in the Range
incBy2Range = range(2, 11, 2)
numbers = list(incBy2Range)
print(numbers)
# 2-10 range created in increments of 2, then saved as a list, and
    # list printed

incBy10Rrange = range(0, 101, 10)
numbers = list(incBy10Rrange)
print(numbers)
# 10-100 range created in increments of 10, then saved as a list, and
    # list printed


    # testing to see if a tuple can be converted to a list
tuple1 = (1, 2, 3)
list1 = (list(tuple1))
print(list1)
# it can! tuple created, converted to a list, and list printed


    # RANGE can only create ranges of integers, so I found this page
        # that explains how to create a range with floats, which
        # requires use of numpy package
        # https://pynative.com/python-range-for-float-numbers/
pip install numpy
import numpy as np
print(list(np.arange(0.5, 7, 1.5)))
# package installed and imported, then range printed as a list:
    # [0.5, 2.0, 3.5, 5.0, 6.5]

print(list(np.arange(7)))
# range printed as a list: [0, 1, 2, 3, 4, 5, 6]
    # confirms this function can include integers

print(list(np.arange(7.5)))
# range printed as a list: [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
    # note: b/c parameter is a float, range created as floats,
    # though all numbers are whole

print(list(np.arange(0.5, 7)))
# range printed as a list: [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
    # note: the increment is 1 (as default) since another increment
    # was not defined, though the first item in listed range is 0.5




# Page 16 - Sorting a List
numbers = [2, 6, 3, 9, 1, 10]
strings = ['dog', 'cat', 'bird']
# lists created

    # sort numerically
numbers.sort()
# indexed order of list updated to be in ascending order

    # sort alphabetically
strings.sort()
# indexed order of list updated to be in ascending order

print(numbers)
print(strings)
# lists printed

    # Sort in Descending Order
numbers = [2, 6, 3, 9, 1, 10]
numbers.sort(reverse=True)
print(numbers)
# list updated, then indexed order of list updated to be in
    # descending order, then list printed


    # Non-Permanent Sorting
numbers = [2, 6, 3, 9, 1, 10]
# list updated

print('This is the original set of numbers: ')
print(numbers)
# list printed after defined text

print('This is the sorted set of numbers: ')
print(sorted(numbers))
# list printed after defined text, with list in ascending order,
    # though indexed order not updated

print('This is the re-sorted set of numbers: ')
print(sorted(numbers, reverse=True))
# list printed after defined text, with list in descending order,
    # though indexed order not updated

print('This is the original set of numbers again: ')
print(numbers)
# list printed after defined text




# Page 17 - Iterating Over a Collection

    # For Loop
countries = ['USA', 'Canada', 'England', 'Ireland']
print(countries)
# list created and printed


    # loop through list of countries using `for` loop
for country in countries:
    print(country)
# for loop ran and printed each country from list

    # 1. a list of numbers from 1-5
allNumbers = [1, 2, 3, 4, 5]
# list created

    # 2. an empty list that will store even numbers
evenNumbers = []
# empty list created

    # 3. loop through `allNumbers` and add the even
        # numbers to the `evenNumbers` list
for theNumber in allNumbers:
    # 4. if the number is even, add to `evenNumbers`
    if theNumber % 2 == 0:
        evenNumbers.append(theNumber)
    else:
        print("Ignoring the odd number: ", theNumber)
# for loop ran and added even numbers to a new list and printed odd
    # numbers after defined text

    # 5. print out `evenNumbers`
print(evenNumbers)
# list that was filled by for loop above printed


    # Write three for loops that iterate through a list and prints
        # out each item to the console.
pets = ['Abbey', 'Minette', 'Thunder', 'Various Fish']

for pet in pets:
    print('I <3 pets named ' + pet)
# list created and for loop ran and printed list items after defined
    # text


for pet in pets:
    if pet == 'Abbey' or pet == 'Thunder':
        print('Bark')
    elif pet == 'Minette':
        print('Meow')
    else:
        print('Splash')
# for loop ran and printed defined text based on each pet in list

for pet in pets:
    if pet == 'Abbey' or pet == 'Thunder':
        print('dog')
    elif pet == 'Minette':
        print('cat')
    else:
        print('fish, of course')
# for loop ran and printed animal type for each pet in list
    # note: I tried to use two if's (instead of 2nd as elif) and
    # that didn't work b/c it used the else too much





# Page 19 - While Loop
aNumber = 1
while aNumber <= 5:
    print(aNumber)
    aNumber += 1
# variable created and while loop ran and printed numbers
    # incrementally until it reached 5

    # Iterating over a List with a While Loop
allNumbers = [1, 2, 3, 4, 5]
evenNumbers = []
currentPosition = 0

while currentPosition < len(allNumbers):
    theNumber = allNumbers[currentPosition]
    if theNumber % 2 == 0:
        evenNumbers.append(theNumber)
    else:
        print("Ignoring the odd number: ", theNumber)
    currentPosition += 1

print(evenNumbers)
# variables created and while loop ran and added even numbers from
    # the first variable to the defined variable, and printed odd
    # numbers after the defined text





# Page 20 - Terminating a For Loop
for letter in 'Sally':
    if letter == 'l':
        break
    print('Current letter: ' + letter)

print('The loop is over.')
# for loop ran and printed letters in string after defined text until
    # reaching the defined break point/ value/ letter


    # Terminating a While Loop
aNumber = 7

while aNumber > 0:
    print('Current number value is: ', aNumber)
    aNumber -= 1
    if aNumber == 4:
        break

print('The loop is over.')
# variable created and while loop ran and printed the variable after
    # defined text, then decreased the value of the variable by 1,
    # until the defined value was reached


    # Skipping an Iteration of a Loop
everyone = ['Sally', 'Billy', 'Mary', 'Bob']
lookingFor = 'Mary'

for person in everyone:
    if person != lookingFor:
        continue
    print('Found ' + lookingFor + "'!')
# variables created and for loop ran and skipped values in list until
    # reaching the defined value, then printed the defined value with
    # defined text
