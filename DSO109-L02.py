# DSO109 - Programming Foundations - Python
	# Lesson 2 - Performing Operations in Python

# Page 3 - Concatenating Strings

    # concatenation means to combine
    # When concatenating strings, you use the + operator
from email import message
from operator import truediv
from time import monotonic

from parser import isexpr


myMessage = 'Hello'
myOtherMessage = 'how are you?'
# variables saved

    # concatenate the above variables with a comma in between
myFinalMessage = myMessage + ', ' + myOtherMessage
print(myFinalMessage)
# variable saved and printed


day = 1
year = 2017
month = 'August'

todayIs = month + ' ' + day + ', ' + year
print(todayIs)
# frist 3 variables saved, but last one can't be b/c day and year
    # are integers, not strings


day = '1'
year = '2017'
month = 'August'

todayIs = month + ' ' + day + ', ' + year
print(todayIs)
# variables saved and printed


# Page 4 - Converting Data to Strings

    # using str() function
day = 1
year = 2017
month = 'August'

todayIs = month + ' ' + str(day) + ', ' + str(year)
print(todayIs)
# variables (re)saved and printed
    # note: this time it worked to concatenate numbers b/c 
    # they were converted to strings

    # using str.format() function
todayIs = str.format('The date is {} {}, {}', month, day, year)
print(todayIs)
# variable (re)saved and printed

    # Variable Order Matters
todayIs = str.format('The date is {} {}, {}', year, month, day)
print(todayIs)
# variable (re)saved and printed - though it doesn't make sense



# Page 5 - String Operations

    # using lower() function
myMessage = 'THESE ARE ALL CAPS'
print(myMessage.lower())
# variable (re)saved and printed in lowercase

    # using upper() function
myMessage = 'these are all lowercase'
print(myMessage.upper())
# variable (re)saved and printed in uppercase



# Page 6 - Replacing Text
    # using replace() function
experience = 'this game is fun'
betterExperience = experience.replace('fun', 'awesome')

print(experience)
print(betterExperience)
# variables saved and printed - including word replacement

message = 'I like cats, because cats are friendly'
newMessage = message.replace('cats', 'dogs')

print(newMessage)
# variables saved and printed - including word replacement



# Page 7 - Splitting Text
    # using split() function
    # defaults (space as separator, no limit)
myMessage = 'Split these words for me'
splitAtSpaces = myMessage.split()

print(splitAtSpaces)
# variables saved and printed - with string data split at spaces

    # using comma as separator
myMessage = 'apples, oranges, bananas'
splitAtCommas = myMessage.split(',')

print(splitAtCommas)
# variables saved and printed - with string data split at commas
    # note: because there are spaces after the commas, those 
    # spaces were included in split data

    # using maxsplit paramater
fruit = 'strawberries,raspberries,watermelon,tangerines'
splitInto3 = fruit.split(',', maxsplit= 2)

print(splitInto3)
# variables saved and printed – with string data split at commas
    # and only split twice (3 total parts) 
    # note: b/c the last two fruits weren't split, probably better
        # to still have a space between them
    


# Page 8 - Arithmetic Operators

    # addition
result1 = 2 + 2 + 3
print(result1)
# variables saved and solution - 7 - printed

    # subtraction
result2 = 22.2 - 3 - 11
print(result2)
# variables saved and solution - 8.2 - printed

    # multiplication
result3 = 2 * 3 * 1.1
print(result3)
# variables saved and solution - 6.6000000000000005 - printed

    # division
result4 = 10 / 4
print(result4)
# variables saved and solution - 2.5 - printed

    # modulo (remainder)
result5 = 10 % 4
print(result5)
# variables saved and solution - 2 - printed

    # floor division
result6 = 10 // 4
print(result6)
# variables saved and solution - 2 - printed

    # exponent
result7 = 2 ** 3
print(result7)
# variables saved and solution - 8 - printed

    # expressions within parentheses are evaluated first
result = (5 * 2) + (4 * 2)
print(result)
# variable saved and solution - 18 - printed

# do you understand how the final result, below, is computed?
result = 2 ** 3 * (5 - (3 - 2)) / 4 + 9 // 4
print(result)
# variable updated and solution - 10.0 - printed
    # calculated in this order
        # 3-2 = 1
        # 5 - 1 = 4
        # 2 ** 3 = 8
        # 8 * 4 = 32
        # 32 / 4 = 8
        # 9 // 4 = 2
        # 8 + 2 = 10



# Page 9 - Assignment Operators

a = 15
b = 5
c = 0

c = a + b
print("1. C =", c)
# variables saved, c variable updated and solution -  1. C = 20
    # - printed

c += a
print("2. C =", c)
# variable updated and solution - 2. C = 35 - printed

c *= a
print("3. C =", c)
# variable updated and solution - 3. C = 525 - printed

c /= a
print("4. C =", c)
# variable updated and solution - 4. C = 35.0 - printed

c %= a
print("5. C =", c)
# variable updated and solution - 5. C = 5.0 - printed

c //= b
print("6. C =", c)
# variable updated and solution - 6. C = 1.0 - printed

c = 2
c **= a
print("7. C =", c)
# variable updated and solution - 7. C = 32768 - printed



# Page 10 - Comparison Operators

    # comparing numbers
my_burger_price = 15

is_fifteen_dollars = my_burger_price == 15
print(is_fifteen_dollars)
# variables saved and comparison - True - printed, my burger 
    # price is $15

is_not_twenty_dollars = my_burger_price != 20
print(is_not_twenty_dollars)
# variable saved and comparison - True - printed, my burger 
    # price isn't $20

is_affordable = my_burger_price <= 10
print(is_affordable)
# variable saved and comparison - False - printed, my burger 
    # price is not affordable, b/c it's more than $10

is_pricey = my_burger_price >= 15
print(is_pricey)
# variable saved and comparison - True - printed, my burger 
    # price is pricey b/c it's $15


your_burger_price = 20

my_burger_costs_more = my_burger_price > your_burger_price
print(my_burger_costs_more)
# variable saved and comparison - False - printed, my burger 
    # that's $15 doesn't cost more than yours that is $20

my_burger_costs_less = my_burger_price < your_burger_price
print(my_burger_costs_less)
# variable saved and comparison - True - printed, my burger 
    # that's $15 costs less than yours that is $20


    # comparing strings
my_name = "Sally"
your_name = "Billy"
some_name = "Sally"

print(my_name == your_name)
# variables saved and comparsion - False – printed, we don't 
    # have the same name

print(my_name != your_name)
# comparison - True – printed, we don't have the same name

print(some_name == my_name)
# comparison - True – printed, someone and I have the same name

print("---")
# --- printed

my_name = "Joe"   # uppercase j
some_name = "joe" # lowercase j

print(my_name == some_name)
# variables saved and comparsion - False – printed, we don't 
    # have the same name (according to Python, at least...)

print(my_name.upper() == some_name.upper())
# comparison - True – printed, even Python agrees we have the
    # same name when they're in the same case



# Page 11 - Logical Operators - and

# details of the person who wants to watch the movie
person_age = 17
person_money = 25

# the requirements to watch the movie
age_restriction = 18
movie_price = 10

# conditions
is_old_enough = person_age >= age_restriction
has_enough_money = person_money >= movie_price

# two conditions combined using 'and'
can_watch_movie = is_old_enough and has_enough_money
print(can_watch_movie)
# variables saved and logic - False - printed, even though 
    # this person has enough money to watch this movies, 
    # they're not old enough


# multiple conditions
result = (10 > 3) and (3 < 9) and ("this" != "that")
print(result)
# variable (re)saved and logic - True - printed, 10 is
    # greater than 3, 3 is less than 9, and "this" isn't
    # the same as "that"



# Page 12 - Logical Operators - or
amount_of_money = 10
is_a_friend = True

can_hangout_with_me = amount_of_money >= 25 or is_a_friend
print(can_hangout_with_me)
# variables saved and (unconvententional) logic - True - 
    # printed, this person can hang out with be b/c they are
    # my friend, in spite of the fact that they have less
    # than $25



# Page 13 - Logical Operators - not
person_age = 12
is_old_enough = person_age >= 18

must_leave = not is_old_enough
print(must_leave)
# variables saved and logic - True - printed, this person must
    # leave because they are not old enough to stay

settings_sound_on = True
turn_sound_off = not settings_sound_on
print(turn_sound_off)
# variables saved and logic - False - printed, the sound doesn't
    # need to be turned off (b/c, illogically, it's on... weird
    # example ;)


my_age = 17
my_money = 7
is_friend = True
has_food = False

can_watch_movie = (
    not has_food 
    and ((my_age >= 18 and my_money >= 15) 
    or (is_friend and my_money >= 5)))

print(can_watch_movie)
# variables saved and logic - True - printed, though I think 
        # there's a mistake... what this is saying is that I can
        # watch a movie if I HAVE food (this is the mistake, the 
        # lesson text said the condition should be that I do NOT
        # have food – will ask about this on a code review...)
        # AND I am 18 or older and have at least $15, or I'm a 
        # friend and have at least $5
    # So this is true b/c I have food, am a friend, and have $7 
        # (even though I'm under 18 and have less than $15)


    # from quiz: question 4
print(10 % 3)
# solution - 1 - printed

    # from quiz: question 6
print(9 // 2)
# solution - 4 - printed



# Page 17 - if, elif, and else

    # if
    # A person can watch a movie if they have $10
personMoney = 12
if personMoney >= 10:
    print('This person can watch the movie')
# variable saved and operation performed (string printed), 
    # b/c condition was met (person has over $10)

personMoney = 8
if personMoney >= 10:
    print('This person can watch the movie')
# variable updated but no operation performed (string not 
    # printed), b/c condition wasn't met (person has less 
    # than $10)


    # else
personMoney = 8
if personMoney >= 10:
    print('This person can watch the movie')
else:
    print('Sorry, but you don\'t have enough money')
# variable (re)saved and else operation performed (string 
    # printed), b/c condition wasn't met (person has less 
    # than $10)


    # elif
    # If your age is 18 or higher, you can watch R-rated movies. 
    # If your age is 13 or higher, you can watch PG13-rated 
        # movies. 
    # If your age is less than 13, you can only watch G-rated 
        # movies.
personAge = 18

if personAge >= 18:
    print('I can watch an R-rated movie')
elif personAge >= 13:
    print('I can watch a PG13-rated movie')
else:
    print('I can watch a G-rated movie')
# variable saved and if operation performed (string printed) b/c
    # the if condition was met (person is 18 y/o)

if personAge >= 13:
    print('I can watch a PG13-rated movie')
elif personAge >= 18:
    print('I can watch an R-rated movie')
else:
    print('I can watch a G-rated movie')
# b/c the order was updated, and if condition was met (person
    # is over 13 y/o), the if operation was performed (string 
    # printed), which makes less sense in this context, though 
    # it is technically true... moral of this story: order
    # matters

personAge = 5

if personAge >= 18:
    print('I can watch an R-rated movie')
elif personAge >= 13:
    print('I can watch a PG13-rated movie')
else:
    print('I can watch a G-rated movie')
# variable updated and else operation performed (string printed), 
    # per person being under 13 y/o (neither if nor elif 
    # conditions were met)




# Page 18 - Advanced Decision Making

    # first if/elif/else block
personAge = 16

if personAge >= 18:
    print('I can watch an R-rated movie')
elif personAge >= 13:
    print('I can watch a PG13-rated movie')
else:
    print('I can watch a G-rated movie')
# variable updated and elif condition met (person is over
    # 13 y/o), so its operation was performed (string 
    # printed)

    # second if/else block
if personAge >=16:
    print('I can drive!')
else:
    print('I need to walk')
# if condition was met (person is 16 y/o) so its operation
    # was performed (string printed)


    # combining decision making
personAge = 18

if personAge >= 18:
    print('I can watch an R-rated movie')
    print('I can drive!')
elif personAge >= 13:
    print('I can watch a PG13-rated movie')
    print('I can drive!')
else:
    print('I need my mommy')
# variable updated and if operations perfomed (2 strings
    # printed) b/c if condition was met (persion is 18 y/o)


    # combining logical operands and decision making
personAge = 15
hasCar = False
momCanDrive = True
outcome = ''

if personAge >= 18 and hasCar:
    outcome = 'I can go and see an R-rated movie'
elif personAge >= 13 and momCanDrive:
    outcome = 'Mom can take me to see a PG13-rated movie'
else:
    outcome = 'I\m stuck at home today'

print(outcome)
# personAge variable updated, other variables saved, and 
    # elif condition met (person is over 13 y/o and their
    # Mom can drive), so elif operation performed (outcome 
    # variable updated) and outcome variable printed


    # What do you think would be the output if the age is 
        # changed to 18?
personAge = 18

if personAge >= 18 and hasCar:
    outcome = 'I can go and see an R-rated movie'
elif personAge >= 13 and momCanDrive:
    outcome = 'Mom can take me to see a PG13-rated movie'
else:
    outcome = 'I\m stuck at home today'

print(outcome)
# personAge variable updated and elif condition met (person
    # is over 13 y/o and their Mom can drive) so its 
    # operation performed (outcome variable updated) and 
    # outcome variable printed – even though this person is
    # 18, b/c Mom's driving they only get to see a PG13-rated
    # movie



    # From workshop: https://vimeo.com/426836051

# if you can ride a roller coaster or not, based on height
height = 62
rideLimit = 60
pregnant = False
canRide = ''

if height >= rideLimit and pregnant == False:
    canRide = 'Enjoy the ride!'
elif height < rideLimit:
    canRide = 'Try the kiddy coaster'
else:
    canRide = 'Not today'

print(canRide)
# variables saved and if condition met (person is tall enough
    # and isn't pregnant) so its operation performed (canRide
    # variable updated) and canRide variable printed


height = 48

if height >= rideLimit and pregnant == False:
    canRide = 'Enjoy the ride!'
elif height < rideLimit:
    canRide = 'Try the kiddy coaster'
else:
    canRide = 'Not today'

print(canRide)
# height variable updated and elif condition met (person is
    # too short) so its operation performed (canRide
    # variable updated) and canRide variable printed


    # for loops
animals = ['frog', 'frog', 'toad', 'frog']

for i in animals:
    if i == 'frog':
        print('ribbit')
    else:
        print('You got warts!')
# variable saved and operation performed for each item in 
    # the array, based on whether or not the item met the
    # if condition


numbers = [2, 12, 14, 23, 7]

for i in numbers:
    if i < 4:
        print('Try again')
    elif i >= 5:
        print('It\'s your lucky day!')
# variable saved and operation performed for each item in 
    # the array, based on whether or not the item met the
    # if condition


    # while loops
lightbulb = True
ideaCount = 0

while lightbulb == True:
    ideaCount = ideaCount + 1
    if ideaCount < 3:
        print(('Keep on thinking.') +
        (' Edison didn\'t invent the lightbulb right away'))
    if ideaCount >= 3:
        print('Good job!')
    if ideaCount == 5:
        break
print('You are done thinking for the day')
# variables saved and while loop ran to perform operations
    # until defined condition met