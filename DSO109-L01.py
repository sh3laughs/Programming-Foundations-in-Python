# NOTE: HANDS-ON STARTS AT LINE 353

# DSO109 - Programming Foundations - Python
	# Lesson 1 - Introduction to Python

# Page 1 - Introduction to Python
# From workshop

    #variables
# Good Variable Names
my_first_variable = "yes"
# saved variable

MyFirstVariable = "Fun Times"
# saved variable

# Bad Variable Names
# my first variable
# output: cannot save variable, so I commented it out

# my.first.variable
# output: cannot save variable, so I commented it out

# Variables are case sensitive
# myFirstVariable not the same as MyFirstVariable
# output: cannot save variable, so I commented it out

# print function
print(MyFirstVariable)
# MyFirstVariable printed

# update variable and re-print
MyFirstVariable = "I'm an awesome data science student"
print(MyFirstVariable)
# variable updated and printed

# saving one variable into another variable and re-printing
MyFirstVariable = my_first_variable
print(MyFirstVariable)
# variable updated and printed


    # strings
StringExample = 'This will work'
print(StringExample)
# variable saved and printed

StringExample2 = "This will work"
print(StringExample2)
# variable saved and printed

StringExample3 = '''This 
                    will
    work'''
print(StringExample3)
# variable saved and printed
# note: triple quotes (using single or double quote punctuation)
    # respect line breaks and tabs 

# StringExample4 = 'This won't work'
# print(StringExample4)
# output: can't use apostrophes within single quotes (commented out)

StringExample4 = "This won't work"
print(StringExample4)
# variable saved and printed

# StringExample5 = "She said, "This will not work.""
# print(StringExample5)
# output: can't use double quotes within double quotes (commented out)

StringExample5 = 'She said, "This will not work."'
print(StringExample5)
# variable saved and printed (hurray!)

    #escape characters for strings
# \t - tab
# \n - new line

AddingIndents = '\t Indenting is fun'
print(AddingIndents)
#v ariable saved and printed, indented (lol at rhyme)

AddingNewLines = 'What if I \n had this on two lines'
print(AddingNewLines)
# variable saved and printed on 2 lines
# note: because there's a space after \n, the 2nd line began with 
    # a space


    #Working with Numbers
DoingMathWithIntegers = 2 + 2
print(DoingMathWithIntegers)
#variable saved and solution to equation - 4 - printed

DoingMathWithFloats = 2.1 + 2.1
print(DoingMathWithFloats)
# variable saved and solution to equation - 4.2 - printed


    # Boolean Values (true / false)
Asleep = True
print(Asleep)

PassClass = False
print(PassClass)


    # from q&a
test = 'won\'t'
print(test)
# apostrophes (single quotes) can be used withing single quotes, if 
    # a backslash immediately preceeds it

test = 'This won\'t work'
print(test)
# apostrophes (single quotes) can be used withing single quotes, if 
    # a backslash immediately preceeds it

test2= "She said, \"This will not work.\""
print(test2)
# double quotes can be used within double quotes, if a backslash 
    # immediately preceeds it



# Page 6 - print()
print('Hello World')
# Hello World printed

# print 'Hello World'
# output: can't print without parenthesis (commented out)

print(22)
# 22 printed

print(-1.35)
# -1.35 printed

print(2+2)
# solution to equation - 4 - printed

print(2*3*4)
# solution to equation - 24 - printed

print(4/3)
# solution to equation - 1.33 - printed



# Page 8 - Naming Variables
message = 'Hello World'
# variable saved with string

my_number = 29
# variable saved with integer

my_message = message
# variable saved with another variable (variable-ception)

message = 'Hello'
# variable saved with string
    # variable name is pretty clear

age_to_drive = 16
# variable saved with integer
    # variable name is very clear

AgeToDrive = 16
# variable saved with integer
    # variable name is very clear

person_age = 20
# variable saved with integer
    # variable name is clear

# person age = 20
# variable cannot be saved (space) so it's commented out

engine_piston_1_working = True
# variable saved with boolean 
    # variable name is very clear

# 2nd_engine_piston_working = False
# output: variable cannot be saved (starts with #) so it's 
    # commented out

# class = 5
# output: variable cannot be saved (reserved word) so it's 
    # commented out

person_age = 20
#variable re-saved with (same) integer

Person_Age = 20
# variable saved with integer
# this is new and separate from the one above, per different
    # cases



# Page 9 - Using Variables in VS Code

my_message = 'Hello World'
print(my_message)
# variable saved and printed

    # variable practice
my_message = "Hello World"
print(my_message)

animal_type = 'cat'
print(animal_type)

human_age = 34
print(human_age)

weather = 'bright and sunny'
print(weather)
# variables saved and printed
# note: this is a mess, but clean in 
    # "interactive window" option – I prefer to
    # print incrementally, but did this way per lesson... 
    # though in screenshot in lesson, it's clean (like in
    # interactive window for me), and I'm not sure why there
    # is a difference


# Page 10 - Changing Variables
my_message = 'Hello World'
print(my_message)

my_message = "Hello World, how are you?"
print(my_message)
# variable re-saved and printed, then updated 
    # and re-printed

this_message = my_message
print(this_message)
# variable saved and - Hello World, how are you? - printed


# Page 11 - Data Types - Strings

    # A very basic definition of a string would be just a 
    # series of characters wrapped in quotes
string1 = "This is a string with double quotes"
print(string1)
# variable saved and printed

string2 = 'This is also a string, but it utilizes single quotes'
print(string2)
# variable saved and printed

string3 = """This is a multi-line
string that
spreads over 4
different lines"""
print(string3)
# variable saved and printed

    # Use single quotes when you need to quote someone.
string4 = 'I told John, "you will really enjoy coding!"'
print(string4)
#variable saved and printed

    # Use double quotes when you need to use an apostrophe.
string5 = "Using Python's straightforward syntax makes coding a lot easier."
print(string5)
# variable saved and printed


# Page 12 - Escape Sequences

    # a tab character (\t) is used to push the text over to 
    # the right
my_message = '\tI should be shifted to the right'
print(my_message)
#variable (re)saved and printed, indented

    # the newline character (\n) is used to force the text to 
    # the next line
my_message = "I am on one line\nbut I'm on the next line"
print(my_message)
#variable (re)saved and printed, on 2 lines

    # You can include double quotes (") within text that is 
    # enclosed by single quotes (') and vice versa. 
    # However, you can also use double quotes within text 
    # that is enclosed within double quotes if you use the 
    # escape character (the same goes for single quotes)
my_text = "She said \"Hello!\""
print(my_text)
# variable (re)saved and printed

my_message = 'What\'s your name?'
print(my_message)
# variable (re)saved and printed


# Page 13 - Numbers

    # An integer is a whole number that can be positive or 
    # negative
add_two_numbers = 2 + 2
print(add_two_numbers)
# variable saved and solution to equation - 4 - printed

multiply_two_numbers = 33 * 54
print(multiply_two_numbers)
# variable saved and solution to equation - 1782 - printed

multiply_three_numbers = 33 * 54 * 89
print(multiply_three_numbers)
# variable saved and solution to equation - 158598 - printed

    # A float is a real number with a "floating point" - i.e. a 
    # decimal
add_two_float_numbers = 0.1 + 0.4
print(add_two_float_numbers)
# variable saved and solution to equation - 0.5 - printed

multiply_two_float_numbers = 3 * 0.1
print(multiply_two_float_numbers)
# variable saved and solution to equation - 0.30000000000000004 
    # - printed


# Page 14 - Boolean Data Type

    # A boolean may only be one of two values: either True or 
    # False
user_update_payment_info = False
edit_content = True
# variables saved


# Page 15 - Comments

    # Comments are notes that you can add to code that do not get 
    # interpreted / compiled

# This is a comment
my_message = 'Hello World'
print(my_message)
# variable (re)saved and printed

    # This is commented out
# my_message = 'Hello World'
# print(my_message)


# Page 17 - [Practice] Hands On

# 1. Within the main.py file, create three variables that are 
    # set to the following questions:
        # What is your name?
        # How old are you?
        # How many months is that?
    # Hint! Make sure to write these as strings.
nameQ = 'What is your name?'
ageQ = 'How old are you?'
monthsQ = 'How many months is that?'
# variables saved

# 2. Next, create three more variables that are set to the 
    # following answers to the above questions:
        # My name is "Billy".
        # 30
        # 360
nameA = 'My name is "Billy".'
ageA = 30
monthsA = 360
# variables saved

# 3. Use the print function to print each of the variables. 
    # The output should looks like below:
        # What is your name?
        # My name is "Billy".
        # How old are you?
        # 30
        # How many months is that?
        # 360
    # Make sure Billy is surrounded by quotes in the output
print(nameQ)
print(nameA)
print(ageQ)
print(ageA)
print(monthsQ)
print(monthsA)
# variables printed

# 4. Next, comment out the appropriate variables and print 
    # functions so the output now looks like below:
        # What is your name?
        # My name is "Billy".
        # How old are you?
        # 30
nameQ = 'What is your name?'
ageQ = 'How old are you?'
# monthsQ = 'How many months is that?'
nameA = 'My name is "Billy".'
ageA = 30
# monthsA = 360
print(nameQ)
print(nameA)
print(ageQ)
print(ageA)
# print(monthsQ)
# print(monthsA)
# output: variables (re)saved and printed out, other than the
    # ones that were commented out

# 5. Finally, create three new variables: my_string, my_integer, 
        # and my_float.
    # Each variable should be set to the appropriate data type 
        # based on the name of the variable name. The actual 
        # values you use is not important. What is important is 
        # that you match up the right type of data with the right 
        # variable.
    # Print out each variable on separate lines.
my_string = 'Two two point two'
my_integer = 2
my_float = 2.2

print(my_string)
print(my_integer)
print(my_float)
# variables saved and printed