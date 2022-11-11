# DSO109 - Programming Foundations - Python
    # Lesson 4 - Dictionaries

# Page 3 - Creating a Dictionary
dictionary = {}
# empty dictionary created

    # dictionary is created to represent an employee
employee = {'name': 'Andrew', 'age': 29, 'position': 'Engineer'}
# dictionary created

    # What about an address?
address = {'city': 'Scottsdale', 'state': 'AZ', 'zip': '85258'}
# dictionary created


    # dict() Function
new_dict = dict(name = 'john', age = 19, hometown = 'Phoenix')
print(new_dict)
# dictionary created and printed

dictionary = dict([(1, 'John'), (2, 'Andrew')])
print(dictionary)
# dictionary created and printed


    # write three dictionaries of your own
dictionary1 = {
    'key 1': 'value1',
    'key2': 'value2',
    'keyN': 'valueN'
}
print(dictionary1)

dictionary2 = {
    1: 'one',
    2: 'two',
    3: 'three',
    'n': 'n!'
}
print(dictionary2)

dictionary3 = dict(cool = 11, random = 'yes')
print(dictionary3)
# 3 dictionaries created, and each printed
    # note: learned that keys need to be a single word when created
    # w/ the dict function, though they can be multiple words when
    # created with {} method


    # Best Practice Dictionary Formatting - separate line per
        # key:value pair
contact = {
    'first_name': 'Henry',
    'last_name': 'Poldark',
    'phone_number': '(123)-456-7890',
    'street': 'N 90th St',
    'city': 'Scottsdale',
    'state': 'Arizona',
    'zip_code': '85258'
}
print(contact)
# dictionary created and printed




# Page 5 - Accessing Dictionary Data
person = {'name': 'Andrew',
          'age': 29,
          'city': 'Scottsdale',
          'state': 'AZ'
          }

print(person['name'])
print(person['age'])
# dictionary created and values printed for 2 keys

print((person['age']), (person['name']))
# tested different options, and this is the way I could find to
    # print multiple values together


    # keys function
student = {'name': 'Andrew', 'program': 'Software Development',
           'id': 110272}
theKeys = student.keys()

print(theKeys)
# dictionary created, variable created with a list of all its keys
    # (with dict_keys title and enclosed in both parenthesis and
    # brackets), and that variable printed


    # values function
values = student.values()

print(values)
# variable created with a list of all the dictionary's values
    # (with dict_values title and enclosed in both parenthesis and
    # brackets), and that variable printed


    # items function
print(student.items())
# variable created with a list of all the dictionary's key:value
    # pairs (with dict_items title and enclosed in both parenthesis
    # and brackets), and that variable printed


    # get function
contact = {'name': 'Andrew',
           'occupation': 'Software Engineer'
           }

print('Name: ', contact.get('name'))
print('Occupation: ', contact.get('occupation'))
print('Salary: ', contact.get('salary'))
print('Address: ' + contact.get('address', 'I live in a box'))
# dictionary created, then its keys printed, as well as some keys
    # that don't exist in it – salary returned "None" b/c no
    # default value was defined and address returned "I live in a
    # box" b/c that was the defined default value



# Page 6 - Modifying a Dictionary
    # adding new key
address['street'] = 'N 90th St'

print(address)
# new key:value pair added to dictionary, and dictionary printed

    # updating a value
address['state'] = 'Arizona'

print(address)
# value updated for defined key, and dictionary printed


    # delete a key:value pair
contact = {
    'first_name': 'Andrew',
    'last_name': 'Stefanik',
    'phone_number': '(123)-456-7890',
    'street': 'N 90th St',
    'city': 'Scottsdale',
    'state': 'Arizona',
    'zip_code': '85258'
}

del contact['phone_number']

print(contact)
# dictionary updated, key:value pair deleted, and dictionary
    # printed


del contact
# dictionary deleted


    # testing to see if del function can delete any variable type
listy = [1, 2, 3]
tupley = (1, 2, listy)

del listy
del tupley
# success, both the list and the tuple were deleted



# Page 8 - Dictionary Iteration
user = {
    'name': 'Andrew',
    'email': 'andrew@email.com',
    'username': 'andrewUser'
}

for key, value in user.items():
    print('Key =', key, '\tValue =', value)
# dictionary created and for loop ran and printed each key and
    # value with defined text


    # iterating over keys
for key in user.keys():
    print('Key =', key, '\tValue =', user[key])

for key in user:
    print('Key =', key, '\tValue =', user[key])
# two for loops ran and each had same results when printing keys
    # and values with defined text - though second version left
    # .keys() function


    # iterating over values
for value in user.values():
    print('Value =', value)
# for loop ran and printed each value in dictionary after defined
    # text


    # testing the fact that we were taught things are conctatenated
        # with + and now we're using commas ...
listy = [1, 2, 3]
tupley = (1, 2, 3)

print('I like lists like', listy, 'and tuples like', tupley)
print(1, 2, 'and', 'three')
# turns out things can be concatenated with commas, and when they
    # are a space is automatically added after the object before
    # the comma




# Page 11 - Nested Dictionaries

    # list of dictionaries
contact_0 = {
    'name': 'Andrew',
    'phone': '(123)-222-2325'
}
contact_1 = {
    'name': 'Mike',
    'phone': '(113)-452-9825'
}
contact_2 = {
    'name': 'David',
    'phone': '(323)-933-2054'
}

addressBook = [contact_0, contact_1, contact_2]

for contact in addressBook:
    print(contact)
# 3 dictionaries created, then saved together as a list, then each
    # printed via a for loop on that list


    # dictionary-ception
contact = {
    'name': 'Andrew',
    'phone': '(123)-222-2325'
}

address = {
    'street': '123 Tuple St',
    'city': 'Scottsdale',
    'state': 'AZ'}

contact['address'] = address

print(contact)
# 2 dictionaries created, then the 2nd one nested in the 1st one,
    # and that updated one printed




# Page 12 -
people = {
    'person1': {
        'name': 'Sally Sue',
        'city': 'Phoenix'
    },
    'person2': {
        'name': 'Billy Bob',
        'city': 'Scottsdale'
    },
    'person3': {
        'name': 'Rover',
        'city': 'Zappa'
    }
}

greetings = []

for person in people.values():
    greeting = 'Hello ' + person['name'] + ' from ' + person['city']
    greetings.append(greeting)

print(greetings)
# 1. nested dictionary created
# 2. empty list created
# 3. for loop ran to create a greeting for each person in dictionary,
    # and save those greetings to the list from #2
# list from #2 printed




# Page 14 - Hands-On

    # from workshop
favCandy = {
    'name': 'nerds',
    'sweetness': 5,
    'sour': 7,
    'eatenToday': False
}

print(favCandy)
# dictionary created and printed


    # print info using dictionary functions

print(favCandy.keys())
# keys from dictionary printed

print(favCandy.values())
# values from dictionary printed

print(favCandy.items())
# key:value pairs from dictionary printed

print(favCandy.get('name'))
# value for defined key printed

print('Her name is Meredith. Her favorite candy is:',
      favCandy.get('name'))
# defined text and values printed


    # iterate on dictionary
for key, value in favCandy.items():
    print('Key =', key, 'Value =', value)
# defined text, keys, and values printed


    # create a list of dictionaries
candy1 = {
    'name': 'Mars Bars',
    'price': 2.99
}
candy2 = {
    'name': 'Mallow Cups',
    'price': 3.99
}
candy3 = {
    'name': 'M&M\'s',
    'price': 1.99
}

chocolateMCandies = [candy1, candy2, candy3]

for candy in chocolateMCandies:
    print(candy)
# 3 dictionaries created, then combined into a list, a for loop ran
    # and printed each dictionary in the list


    # delete dictionary
del favCandy
print(favCandy)
# dictionary deleted, as confirmed by printing
