# DSO109 - Programming Foundations - Python
	# Lesson 2 - Performing Operations in Python

# Page 20 - Hands-On

# Part 1 - Create a program that will concatenate string 
    # variables together to form your birthday.

    # 1. Create three variables named day, month and year
day = '29'
month = 'April'
year = '1981'
# variables created

    # 2. Concatenate each of these variables to create your 
            # full birthday.
        # Hint! You cannot concatenate strings and integers, 
            # so all variables will need to be strings
month + ' ' + day + ', ' + year
# variables concatenated, wih spaces and comma to be legible
 
    # 3. Assign the concatenation to a fourth variable named 
        # my_birthday.
my_birthday = month + ' ' + day + ', ' + year
# new variable saved, concatenating prior variables

    # 4. Finally, print the variable my_birthday to see if you 
            # have the format identical to the one in the example 
            # below:
        # For example, if your birthday is on November 11th of 
            # 1991, then the format/output should be November 11, 
            # 1991
        # Tip! To add spaces between each word as you concatenate 
            # them, use double quotes with a space in between them 
            # like so: " ".
print(my_birthday)


# Part 2
    # 1. Concatenate the variables first, second, third, and 
        # fourth and set this concatenation to the variable 
        # final:
first = 'happy'
second = 'birthday'
third = 'to'
fourth = 'you'

final = first + ' ' + second + ' ' + third + ' ' + fourth
print(final)
# variables saved, then concatenated and saved into a new
    # final variable, then final variable printed

    # 2. Print the final variable, but all words should be 
        # uppercase.
print(final.upper())
# final variable printed in UPPERCASE

    # 3. Run this code in the VSCode terminal.
        # The output should be HAPPY BIRTHDAY TO YOU.
print(final.upper())
# final variable printed in UPPERCASE (again)
    # note: I'm not sure how this is different from step 2...
        # unless that step was about typing the code and this
        # step about running it? That seems weird...

# Part 3 - Finally, add code to your program that determines 
    # if the given age allows the attendee to see the movie, 
    # printing out a specific message based on the age. There 
    # should be four possible outputs:
        # If under the age of 10, print Not permitted
        # If under the age of 15, print Permitted with a 
            # parent
        # If under the age of 18, print Permitted with anyone 
            # over 18
        # If 18 or over, print Permitted to attend alone
    # Tip! You may need more than one elif statement to capture 
        # each condition, and the sequence matters.

# Below is some code to get you started:
age = 15

if age == 10:
    print('Not permitted')
elif age < 15:
    print('Permitted with a parent')
elif age < 18:
    print('Permitted with anyone over 18')
else:
    print('Permitted to attend alone')
# variable saved and 2nd elif condition met - person is younger
    # than 18 (and older than 14) so that operation performed
    # (string printed: 'Permitted with anyone over 18')