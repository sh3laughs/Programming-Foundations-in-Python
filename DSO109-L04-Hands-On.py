# DSO109 - Programming Foundations - Python
    # Lesson 4 - Dictionaries

# Page 14 - Hands-On

# Part 1
    # 1. Create two dictionaries to represent information about two
            # pets. Each dictionary should contain the following
            # information (different for each pet):
        # Pet's Name (This should be the name of your dictionary)
        # Type of Pet
        # Color
        # Nickname
        # Owner's Name
Abbey = {
    'Type': 'dog',
    'Color': 'black',
    'Nickname': 'sniffvestigative journalist',
    'Owner': 'Hannah'
}
print('Abbey:', Abbey)

Minette = {
    'Type': 'cat',
    'Color': 'seal point tortoise',
    'Nickname': 'Minette-ah',
    'Owner': 'Hannah'
}
print('Minette:', Minette)
# 2 dictionaries created and printed, with dictionary names


    # 2. Iterate over each dictionary, printing each key-value pair
            # on one line. The output should be similar to the
            # below:
        # Type: Cat
        # Color: White and Orange
        # Nickname: Birchy
        # Owner: Kurt
        # Type: Cat
        # Color: Tortoise Shell
        # Nickname: Palnut
        # Owner: Olivia
for k, v in Abbey.items():
    print(k + ': ' + v)
for k, v in Minette.items():
    print(k + ': ' + v)
# for loops ran on each dictionary and printed key value pairs as
    # defined in requirements



# Part 2
    # 1. Add three new dictionaries to your program.
        # Each dictionary should represent a city around the world.
Paris = {
    'Country': 'France',
    'Language': 'French',
    'FavFood': 'steak frites'
}
print('Paris:', Paris)

Carlsbad = {
    'Country': 'USA',
    'Language': 'English',
    'FavFood': 'carnitas burrito'
}
print('Carlsbad:', Carlsbad)

Kelowna = {
    'Country': 'Canada',
    'Language': 'English',
    'FavFood': 'poutine'
}
print('Kelowna:', Kelowna)
# 3 dictionaries created and printed, with dictionary names


    # 2. Add the below dictionaries to your main.py file:
        # england = {'Capital': 'London'}
        # france = {'Capital': 'Paris'}
        # belgium = {'Capital': 'Brussels'}
england = {'Capital': 'London'}
print('england:', england)

france = {'Capital': 'Paris'}
print('france: ', france)

belgium = {'Capital': 'Brussels'}
print('belgium:', belgium)
# 3 provided dictionaries created and printed, with dictionary names


    # 3. Given the above dictionaries, add the following information
            # to each dictionary:
        # Population
        # The population of England is 53.01 million
        # The population of France is 66.9 million
        # The population of Belgium is 11.35 million
        # Interesting Fact
        # Top Language Spoken by Locals
england['Population'] = '53.01 million'
england['Factoid'] = 'I lived here for 3 months, as a nanny'
england['Language'] = 'English'
print('england:', england)

france['Population'] = '66.9 million'
france['Factoid'] = 'I lived here for 2 months, as a student'
france['Language'] = 'French'
print('france: ', france)

belgium['Population'] = '11.35 million'
belgium['Factoid'] = 'My Mom lived here for 2 months - in a castle!'
belgium['Language'] = 'French, Dutch, German'
print('belgium:', belgium)
# dictionaries udpated to include 3 additional key:value pairs each
    # then each printed with their names


    # 4. Once you have added the necessary information into the
        # dictionaries, loop through each one and print out all key-
        # value pairs.
for k, v in england.items():
    print(k + ' of England: ' + v)
for k, v in france.items():
    print(k + ' of France: ' + v)
for k, v in belgium.items():
    print(k + ' of Belgium: ' + v)
# for loops ran on each dictionary and printed key value pairs, with
    # dictionary names as part of key labels to differentiate them



# Part 3
    # 1. Add a dictionary to your program that replicates a user's
            # pizza order. Name this dictionary pizza_order and it
            # should contain the following:
        # Customer's Name
        # What size pizza they have ordered
        # What type of crust
        # What toppings they would like.
            # Toppings should include at least three separate
                # toppings
pizza_order = {
    'name': 'Andrew',
    'size': 'small',
    'crust': 'thin-crust',
    'toppings': 'extra cheese, sausage, bacon'
}
print(pizza_order)
# dictionary created and printed


    # 2. Next, print out the customer's order:
        # Thank them for their order using their name
        # Print out what they're ordering
        # Print out the list of toppings (minimum 3)
    # 3. Your output should looks similar to the following:
            # Thank you for your order, Andrew
            # You have ordered a small, thin-crust pizza with the
                # following toppings:
            # extra cheese, sausage, bacon
        # Use the print() and get() functions
print('Thank you for your order,', pizza_order.get('name'),
      '\nYou have ordered a', pizza_order.get('size') + ',',
      pizza_order.get('crust'),
      'pizza with the following toppings:', '\n' +
      pizza_order.get('toppings'))
# order printed as defined in requirements
