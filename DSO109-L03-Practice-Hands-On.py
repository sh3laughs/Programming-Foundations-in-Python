# DSO109 - Programming Foundations - Python
    # Lesson 3 - Lists and Loops

# Page 22 - [Practice] Hands-On

# Part I
    # 1. Create a list of the following first names: Kurt, David,
        # Katherine.
    # 2. The variable name for the above list should be
        # list_of_names.
list_of_names = ['Kurt', 'David', 'Katherine']
# list created


    # 3. Use a for loop to loop through each name in the list and
            # print the following question: Where is _____ today?
        # Each name should replace the blank within the question.
    # 4. The output should look like the following:
        # Where is Kurt today?
        # Where is David today?
        # Where is Katherine today?
for name in list_of_names:
    print('Where is ' + name + ' today?')
# for loop ran and printed results as defined in requirement #4




# Part II
    # 1. Create three separate lists with the following variable
            # names: my_favorite_cars, my_favorite_flowers,
            # my_favorite_animals
        # my_favorite_cars should include 3 different cars
        # my_favorite_flowers should include 4 different flowers
        # my_favorite_animals should include 5 different animals
my_favorite_cars = ['Bentley', 'Tesla', 'Lamborghini']
my_favorite_flowers = ['wildflowers', 'peony', 'honeysuckle',
                       'any flowers someone gives me']
my_favorite_animals = ['Abbey', 'Thunder', 'Minette', 'Tommy',
                       'Tucker']
# 3 lists created


    # 2. Concatenate the above three lists into a single list named
        # my_favorite_things.
my_favorite_things = my_favorite_cars + my_favorite_flowers + my_favorite_animals

print(my_favorite_things)
# list created and printed


    # 3. Use a for loop to iterate over each element of the
            # my_favorite_things combined list. Print out each item
            # with an even length.
        # The output should show only items in the my_favorite_things
            # list that have an even number of letters.
for favoriteThing in my_favorite_things:
    if len(favoriteThing) % 2 == 0:
        print(favoriteThing)
# printed:
    # any flowers someone gives me
    # Tucker
# apparently I tend to prefer odd things, haha ;)



# Part III
    # Finally, add to your program new code that does the following:
    # 1. Create a list named number_range that includes the numbers
        # 1 - 20
    # 2. Loop through the list
    # 3. For every number that is divisible by 3 and 5, print ZipZap
    # 4. For every number that is divisible by 3, print Zip
    # 5. For every number that is divisible by 5, print Zap
    # 6. If the number is not divisible by any of the three, then
        # just print the number.
    # Your output should look like the following:
        # 1
        # 2
        # Zip
        # 4
        # Zap
        # Zip
        # 7
        # 8
        # Zip
        # Zap
        # 11
        # Zip
        # 13
        # 14
        # ZipZap
        # 16
        # 17
        # Zip
        # 19
        # Zap
number_range = list(range(1, 21))
print(number_range)

for number in number_range:
    if number % 3 == 0 and number % 5 == 0:
        print('ZipZap')
    elif number % 3 == 0:
        print('Zip')
    elif number % 5 == 0:
        print('Zap')
    else:
        print(number)
# list saved and printed as in the requirements above
    # Took a few tries, but I got it - woo hoo!
    # first issue to fix was wrong syntax for the range
    # second issue was = instead of ==
    # final issue was multiple if's instead of elif's
