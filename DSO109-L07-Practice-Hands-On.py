"""Practices code DSO109 from lesson 7."""
# DSO109 - Programming Foundations - Python
    # Lesson 7 - Standard Library

# Page 12 - Python's Standard Library Practice Hands-On

# Part I
    # 1. Create a program that imports the datetime module from the
        # Python standard library and creates a variable that is set
        # to today's date.
    # 2. Print out the full date.
    # 3. Separately, print out only the time: hour and minute.

    # You did not cover the datetime module in the lesson, so you can
        # read up on it at the link below. Looking up information is
        # something that you will need to do rather regularly as a
        # programmer, so it's good practice.

    # Documentation for the datetime module:
# https://docs.python.org/3/library/datetime.html#module-datetime

    # The expected output is below (the actual date and time below
            # will be different for you):
        # Today is: 2018-07-09 08:59:08.385290
        # Time: 08:59:08.385437
        # The time will be in 24/hr format. This is acceptable.

    # Tip! You will need to use the .now() attribute.
import datetime
# module imported

dateToday = datetime.datetime.now()
# variable created

print('Today is:', dateToday)
# printed: Today is: 2022-11-05 02:47:00.054103

print('Time:', datetime.datetime.now().time())
# printed: Time: 02:50:37.065607




# Part II
    # 1. Create the following new string variable that is constructed
            # over four lines: "Tiny little secrets Get buried in the
            # dirt, And if they were dug up, Someone would probably
            # get hurt."
    # The variable name for the above string should be poem_string
    # The new lines should happen where you see capital letters
    # Hint! Use the new line character
poem_string = 'Tiny little secrets'
poem_string += '\nGet buried in the dirt,'
poem_string += '\nAnd if they were dug up,'
poem_string += '\nSomeone would probably get hurt.'

print(poem_string)
# variable created, updated (in the method we learned in the lesson,
    # though it could have actually just been created as a single
    # string to start..), and printed


    # 2. Create and open a new file object named poem.txt in write
            # mode.
        # This variable name should be poem_file
poem_file = open('poem.txt', 'w')


def status(poem_file):
    """Confirm open / closed status for text file"""
    if(poem_file.closed == True):
        print('File Status: Closed')
    else:
        print('File Status: Open')

status(poem_file)
# text file created and opened in write mode, as confirmed via
    # function created to confirm


    # 3. Write the above string to the poem.txt file.
poem_file.write(poem_string)
# string written to text file

    # 4. Close the poem.txt file.
poem_file.close()

status(poem_file)
# text file closed

    # 5. Re-open the poem.txt file in read mode.
        # This variable name should be poem_file
poem_file = open('poem.txt', 'r')

status(poem_file)
# text file opened in read mode, and confirmed opened


    # 6. Read the contents of the file and print to the console.
print(poem_file.read())
# text file read and printed (printed the same as in step 1)

    # 7. Close the file once again.
poem_file.close()

status(poem_file)
# text file closed, and confirmed closed
