"""Practices code from DSO109 lesson 5."""
# DSO109 - Programming Foundations - Python
    # Lesson 5 - Functions

# Page 1 - Functions - From workshop


    # create function
def notThatOld(age):
    newAge = age - 5
    print(newAge)
# new function created
    # HINT: age is a local variable


    # call newly created function
notThatOld(55)
# new function called and results printed


    # create function
def notThatOld2(age):
    return age - 5
# new function created
    # HINT: age is a local variable


    # call newly created function
print(notThatOld2(55))
# new function called and results printed - same results as with first
    # function, but in a different way (return in function and print
    # used when calling it)


    # create function
def notThatOld3(age, increment):
    newAge = age - increment
    print(newAge)
# new function created
    # HINT: age and increment are local variables


    # call newly created function
notThatOld3(55, 5)
# new function called and results printed - same results as with other
    # functions, but in a different way (value for making age younger
    # is variable and defined when calling the function)


    # create a global function
newAge = ''


def notThatOld4(age, increment):
    global newAge
    newAge = age - increment
    print(newAge)


    # call new function
notThatOld3(55, 5)
print(newAge)
# new function called and results printed - same results as with other
    # functions, but in a different way (value for making age younger
    # is variable and defined when calling the function)

    # create function
lambdaOld = lambda x, y: x - y
# new function created
    # HINT: x and y are local variables

    # call newly created function
print(lambdaOld(55, 5))
# new function called and results printed - same results as with other
    # functions, but in a different way (using lambda function)


    # create function using map function to iterate
ages = [32, 57, 39, 75]
increments = [4, 20, 2, 10]
# lists created

mapIt = map(lambdaOld, ages, increments)
listIt = list(mapIt)
# variable created using map function which ran the new lists as the
    # arguments in the parameters for the defined lambda function
    # (created just before/ above), then a new list created using the
    # output of that map function running

print(listIt)
# newly created list printed, as final step in using map function


    # create function using filter function to iterate
overTheHill = lambda x: x > 50

filterIt = filter(overTheHill, ages)

listIt2 = list(filterIt)

print(listIt2)
# lambda function created, then filtered (only return True results),
    # then those results added to a new list, and that list printed




# Page 3 - Functions
def greeting():
    """This function prints a greeting"""
    print('Hello!')


greeting()
# function created and called




# Page 4 - Parameters and Arguments

    # create function and run it
def increment(value):
    """This function increments a value"""
    print('Old value =', value)
    value += 1
    print('New value =', value)


increment(10)
# function created and called


    # create function and run it
def myFunction(howMany, ofWhat, itTastes):
    """Print quantity and taste"""
    print(howMany, ofWhat, itTastes)


myFunction(10, 'oranges', 'yummy')
# function created and called


    # update function to include an additonal parameter and run it
def increment(value, stepSize):
    """This function increments a value"""
    print('Old value =', value)
    value += stepSize
    print('New value =', value)


increment(10, 5)
# function updated and called


    # update function to make the additonal parameter optoinal and
        # run it
def increment(value, stepSize=1):
    """This function increments a value"""
    print('Old value =', value)
    value += stepSize
    print('New value =', value)


increment(10, 5)
increment(10)
# function updated and called w/ and w/o optional parameter




# Page 5 - Function Return Values

    # update function to return results instead of printing them
def increment(value, stepSize=1):
    """This function increments a value"""
    return value + stepSize


newValue = increment(5, 3)
print('The new value is', newValue)
# function updated, called, and results printed with defined text


    # create a new function, call it, and print the results
def sum(x, y):
    """This function sums the inputs"""
    return x + y


result = sum(10, 15)
print('The sum of 10 and 15 is', result)
# function created, called, and results printed


    # create function, save its results to a tuple, and print it
def getSettings():
    """This function returns two dictionaries as a tuple"""
    dict1 = {'name': 'Bob', 'color': 'blue'}
    dict2 = {'name': 'Sally', 'color': 'red'}
    return (dict1, dict2)


tuple = getSettings()
print(tuple)
# created function, saved its results to a tuple, and printed it


    # test returning default "None" results
print(greeting())




# Page 6 - Local Variables and Scope

    # global and local variables with same name
user = 'Andrew Jones'
# global variable created


def myFunction2(first, last):
    """This function concatenates users' first and last names"""
    user = first + ' ' + last
    return user
# function created with a local variable the same name as the
    # previously created global variable


print(user)
# global variable printed

print(myFunction2('John', 'Smith'))
# function called and results printed


    # create a function that uses the global variable
def theUser():
    """Return the value of a global user variable"""
    return user


print(theUser())
# function created, called, and results printed


    # create a function using a global variable
y = 25


def myFunction3():
    """This function is literally just for practice"""
    global y
    print('y is', y)
    y = 5
    print('the new value of global y is', y)


myFunction3()
print('y is now', y)
# (global) variable creaed, function created with that variable,
    # function called, variable printed with defined text





# Page 7 - Average Function Activity

    # Create a function named get_average that:
        # Has three numeric parameters: x, y, and z.
        # Returns the average of the three parameters. Remember, the
            # average is the sum of all items divided by the count.
def get_average(x, y, z):
    return (x + y + z) / 3


print(get_average(1, 2, 3))
# function created, called, and results printed




# Page 8 - Count Function Activity

    # Create a function named get_count that:
        # Has two parameters:
            # data_list: a list of numeric values.
            # update_count: an optional parameter with a default
                # value of False.
        # If update_count is True, this function should set the
            # global count variable to the count of the input list
            # data_list.
        # Returns the number of items of the data_list parameter.
count = 0
listy = [1, 2, 3, 4, 5]

def get_count(data_list, update_count=False):
    global count
    if update_count == True:
        count = len(data_list)
    return len(data_list)


print(get_count(listy))
print(count)

print(get_count(listy, True))
print(count)
# variable, list, and function created, then function called and
    # results printed, testing both scenarios


    # solution from page
def get_count(data_list, update_count=False):
    if update_count:
        global count
        count = len(data_list)
    return len(data_list)


print(get_count(listy))
print(count)

print(get_count(listy, True))
print(count)
# same results as mine ;)




# Page 9 - Lambdas

    # install package(s)
pip install python-language-server
pip install 'python-language-server[yapf]'

    # create lambda function and assign to variable
myLambda = lambda x, y: x + y

print(myLambda(4, 5))
# lambda function created, called, and results printed


    # create lambda function and assign to variable
a = lambda x: x > 10

print(a(20))
# lambda function created, called, and results printed




# Page 10 - Map and Filter

    # map function

    # 1. the list of numbers
numbers = [1, 2, 3, 4, 5]

    # 2. the lambda function to square a number
square = lambda x: x * x

    # 3. use `map` to apply the squaring lambda function to every
        # item in the list of `numbers` as its argument
map_results = map(square, numbers)

# 4. `map` returns a special type of data, but it can be converted
    # to a list using the `list` function
results = list(map_results)

# 5. print the results
print(results)
# list created, function created, function called and results saved
    # as a list, then list printed


    # create a lambda function as a map argument

    # declare two lists of integers
list_a = [1, 2, 3, 4, 5]
list_b = [11, 12, 13, 14, 15]

    # call `map` with a lambda function that sums two numbers
        # the first number comes from `list_a`, the second comes
        # from `list_b`
map_results = map(lambda val_a, val_b: val_a + val_b, list_a, list_b)

    # print results (converting map result to list within print
        # statement)
print(list(map_results))



    # filter function
# 1. the list of numbers
numbers = [1, 2, 3, 4, 5]

# 2. the lambda function to return True only if the value is even
is_even = lambda x: x % 2 == 0

# 3. call `filter` using the `is_even` lambda function and the list
    # `numbers` as its argument
filter_results = filter(is_even, numbers)

# 4. `filter` returns a special type of data like `map`, but it can
    # be converte to a list using the `list` function
results = list(filter_results)

# 5. print the results
print(results)


    # testing to see if I can create a lambda function as a filter
        # argument, like I could with map
results2 = filter(lambda x: x % 2 == 0, numbers)

print(list(results2))
# success - can create this way as well




# Page 11 - Lambda Activity

    # Create a lambda function that has one parameter for a list of
        # numbers. The lambda should compute the average of all of
        # the numbers in the list. Assign the lambda to the variable
        # named fn_average.
    # Remember, to compute the average, you divide the sum by the
        # count. You can use the built-in Python functions sum and
        # len to compute the sum and get the length of a list,
        # respectively. You've already seen the len function (e.g.
        # len(my_list)).
    # Using the numbers list of lists, call the map function to
        # compute the averages. The call to the map function should
        # be using the numbers and fn_average variables as
        # arguments.

    # SUCCESSFUL option (prior attempts below - had forgotten to use
        # list function!)
    # adding map directly to variable
numbers = [[1, 2, 3], [4, 5, 6]]

fn_average = lambda num: sum(num) / len(num)

averages = list(map(fn_average, numbers))

print(averages)
# printed: [2.0, 5.0] - woo hoo!
    # alternate option for last two lines:
        # averages = list(map(fn_average, numbers))
        # print(averages)


    # 3 prior attempts
    # 1. treating each nested list as a separate list
        # note: this goes against requirements of having a single
        # parameter in lambda function
numbers = [[1, 2, 3], [4, 5, 6]]

fn_average = lambda num1, num2: (sum(num1, num2) / (len(num1)) +
                                 len(num2))

averages = map(fn_average, numbers[0], numbers[1])

print(averages)
# printed: <map object at 0x7f87a961adc0>


    # 2. using a for loop
numbers = [[1, 2, 3], [4, 5, 6]]

fn_average = lambda num: sum(num) / len(num)

averages = []

for item in numbers:
    averages.append(map(fn_average, item))

print(averages)
# printed: [<map object at 0x7f87e8e2abe0>,
    # <map object at 0x7f87e8e2aeb0>]


    # 3. removing map, just to ensure my lambda function works
numbers = [[1, 2, 3], [4, 5, 6]]

fn_average = lambda num: sum(num) / len(num)

averages = []

for item in numbers:
    averages.append(fn_average(item))

print(averages)
# printed: [2.0, 5.0]




# Page 12 - Product Activity

    # Given the two lists list_a and list_b, use the map function to
        # compute the product of the numbers of the lists. Store the
        # results of the call to map in a variable named products.
    # The product is the result of multiplying numbers. For instance,
        # if the input list were:
            # [1, 2, 3]
            # [2, 3, 4]
        # The result would be:
            # [2, 6, 12]
list_a = [4, 6, 8]
list_b = [3, 3, 1]

prod = lambda first, second: first * second

products = list(map(prod, list_a, list_b))

print(products)
# success!
    # alternate option for last two lines:
        # products = list(map(prod, list_a, list_b))
        # print(products)
