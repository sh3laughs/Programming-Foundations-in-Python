"""Practices code from DSO109 lesson 5."""
# DSO109 - Programming Foundations - Python
    # Lesson 5 - Functions

# Page 13 - [Practice] Hands-On

# Part I
    # 1. Create three functions that each accept three parameters.
        # The first function should be named sum_function and should
            # return the sum of all numbers (add them all together)
        # The second function should be named product_function and
            # should return the product of all numbers (multiply them
            # all together)
        # The third function should be named average_function and
            # should return the average of all numbers
        # HINT: The average is the sum divided by the number of
            # items.
def sum_function(data1, data2, data3):
    """Sum 3 parameters."""
    return data1 + data2 + data3


def product_function(data1, data2, data3):
    """Find product of 3 parameters."""
    return data1 * data2 * data3


def average_function(data1, data2, data3):
    """Find average of 3 parameters."""
    return (data1 + data2 + data3) / 3
# 3x functions created
    # note: couldn't use the built-in sum() function within the 1st
    # or last of these functions b/c it only accepts 2 arguments


    # 2. Print out the result of calling each function. For example:
            # print(sum_function(1, 2, 3))
        # Should print:
            # 6
print(sum_function(1, 2, 3))

print(product_function(1, 2, 3))

print(average_function(1, 2, 3))
# functions called and results printed



# Part II
    # 1. Create three lambda functions that do the same thing as the
            # functions in step 1. Assign each lambda function the
            # following variables:
        # add_numbers
        # multiply_numbers
        # average_numbers
add_numbers = lambda data1, data2, data3: (data1 + data2 + data3)

multiply_numbers = lambda data1, data2, data3: data1 * data2 * data3

average_numbers = lambda data1, data2, data3: (
    data1 + data2 + data3) / 3
# 3x lambda functions created


    # 2. Print and call the above functions
print(add_numbers(1, 2, 3))

print(multiply_numbers(1, 2, 3))

print(average_numbers(1, 2, 3))
# functions called and results printed



# Part III
    # 1. Creating three separate lists named the following: list_one,
        # list_two, list_three
list_one = []
list_two = []
list_three = []
# 3x empty lists created


    # 2. Add the following numbers in to their respective lists:
        # numbers 4, 6, 88, and 24 should go within list_one
        # numbers 17, 34, 9, and 5 should go within list_two
        # numbers 63, 20, 98, and 4 should go within list_three
list_one = [4, 6, 88, 24]
list_two = [17, 34, 9, 5]
list_three = [63, 20, 98, 4]

print(list_one)
print(list_two)
print(list_three)
# lists updated with provided values, then printed



    # 3. Create one lambda function named average_maker that takes in
        # three numbers and finds the average.
average_maker = lambda data1, data2, data3: (
    data1 + data2 + data3) / 3
# lambda function created


    # 4. Use map to compute the average of each set of values at each
            # index. This will produce a new list of the four average
            # calculations.
        # The variable name for this calculation should be
            # map_results
        # You will be using each of the lists within the map
            # function.
map_results = map(average_maker, list_one, list_two, list_three)
# used map to call function, and saved results to new variable


    # 5. Print out the end result of using map.
        # Hint! You will need to use list()
print(list(map_results))
# printed new variable as a list
    # note: I initially used the list function in step 4, then
    # updated to use it here instead, per the Hint! on this step


    # 6. The final output should be as shown below:
        # [28.0, 20.0, 65.0, 11.0]
# success!
