"""Practices code DSO109 from lesson 6."""
# DSO109 - Programming Foundations - Python
    # Lesson 6 - Object Oriented Programming

# Page 3 - Classes
    # Create a class, with comments to describe each section


    # 1. Define the class (renamed to avoid warning below)
class Dog1:
    # 2. The doctstring for the class
    """The summary docstring for the Dog class. This class represents
       a Dog."""


    # 3. The initializer of the class - where class properties are
        # initialized
    def __init__(self, name, age):
        # 4. Class methods, including the initializer, should have
        # their own docstrings
        """Initialize attributes to describe a dog."""

        # 5. Below are the properties of the class, each w/ its own
            # docstring
        self.name = name   #: The name property represents dog's name
        self.age = age     #: The age property represents dog's age

    # 6. Teo methods are defined for the class
    def sit(self):
        """Simulate a dog sitting on command."""
        print(self.name.title() + ' is sitting.')

    def stay(self):
        """Simulate a dog that will stay on command."""
        print(self.name.title()) + ' was told to stay.'
# class created with 2 methods


    # Create a class without comments
class Dog:
    """The summary docstring for the Dog class. This class represents
       a Dog."""

    def __init__(self, name, age):
        """Initialize attributes to describe a dog."""
        self.name = name   #: The name property represents dog's name
        self.age = age     #: The age property represents dog's age

    def sit(self):
        """Simulate a dog sitting on command."""
        print(self.name.title() + ' is sitting.')

    def stay(self):
        """Simulate a dog that will stay on command."""
        print(self.name.title() + ' was told to stay.')
# class created with 2 methods


    # create 2 instances of the class
fido = Dog('Fido', 5)
spot = Dog('Spot', 7)
# 2 instances created

    # print properties for each instance
print('The name of the dog is', fido.name, 'and the age is',
      fido.age)
print('The name of the dog is', spot.name, 'and the age is',
      spot.age)
# instances printed with defined text

    # update fido's age
fido.age = 9
# property updated for defined instance

    # print properties for each instance again, w/ updated age
print('The name of the dog is', fido.name, 'and the age is',
      fido.age)
print('The name of the dog is', spot.name, 'and the age is',
      spot.age)
# instances printed with defined text


    # call the methods, for each instance
fido.sit()
fido.stay()
spot.sit()
spot.stay()
# both methods called for both instances




# Page 5 - Class Properties and Methods
    # Create a class, with comments to describe each section
class Cat:
    """This class represents a cat."""

    # 1. This is a class variable that is shared by ALL instances
    soundMade = 'Meow'

    # 2. The class intialization method
    def __init__(self, name):
        """Initializer of Cat class"""
        self.name = name   #: The name of the Cat instance

    # 3. This method prints out the class variable 'sound_made'
    def saySomething(self):
        """Speak!"""
        print(self.name, 'says', Cat.soundMade)
# class created


    # 4. create 2 Cat instances
mittins = Cat('Mittens')
feather = Cat('Feather')
# 2x instances created

    # 5. call 'saySomething' method on each instance
mittins.saySomething()
feather.saySomething()
# instance property called for each instance – which printed:
    # Mittens says Meow
    # Feather says Meow

    # 6. change the value of the class variable
Cat.soundMade = 'Woof'
# class variable updated

    # 7. call 'say_something' again for each instance after that
        # update
mittins.saySomething()
feather.saySomething()
# instance property called for each instance – which printed:
    # Mittens says Woof
    # Feather says Woof

    # testing to see if calling the class property is the same
        # outside of the class
print(Cat.soundMade)
# success, it is the same – printed: Woof


    # another example
class cat2:
    """This is an example"""

    classVar = 'I am a class variable'

    def __init__(self, instVar):
        """ Initializer for cat2 class"""
        self.instVar = instVar

    def printProps(self):
        """Print"""
        print('My class property value is', cat2.classVar)
        print('My instance property value is', self.instVar)
# class created


myCat = cat2('Whiskers')
myCat.printProps()
# instance created and instance property called – which printed:
    # My class property value is I am a class variable
    # My instance property value is Whiskers

print(cat2.classVar)
print(myCat.instVar)
# class and instance variables both printed:
    # I am a class variable
    # Whiskers


    # Create a class, with comments to describe each section
class Duck:
    """This class represents a duck."""

    # 1. class variable available to all instances
    soundMade = 'quack'

    def __init__(self, name):
        """Duck initializer"""
        self.name = name

    # 2.instance method for saying something
    def say(self, what):
        """The instance says 'what'"""
        print(self.name, 'says', what)

    # 3. class method for speaking the sound all ducks make
    @staticmethod
    def speak():
        """The class says soundMade"""
        print('Ducks say', Duck.soundMade)
# class created

# 4. call class method
Duck.speak()
# printed: Ducks say quack

# 5. creating an instance and calling the instance method
daffy = Duck('daffy')
daffy.say('Hello')
# printed: daffy says Hello




# Page 6 - Robust Class Example
    # Create a class, with comments to describe each section

    # 1. Define student class
class student:
    """This models a student"""

    # 2. class variable - array of student instances
    students = []   #: class variable to hold all students

    # 3. initializer for 2 instance properties
    def __init__(self, name, grade):
        """Initializer of class"""
        self.name = name     #: instance variable for student name
        self.grade = grade   #: instance variable for student name

    # 4. instance method to display info about a student
    def display(self):
        """Instance method to display student info"""
        print('Name:', self.name, ', Grade:', self.grade)

    # 5. class method to add a student instance to class array
    @staticmethod
    def addStudent(student):
        """Class method to add student to class list variable"""
        student.students.append(student)

    # 6. class method to call the display method for all students
    @staticmethod
    def displayStudents():
        """Class method for printing all students"""
        for Student in student.students:
            Student.display()
# class created

# 7. create an instance of class and print info
bill = student('Bill', 'Freshman')
bill.display()
# printed: Name: Bill , Grade: Freshman

# 8. create another instance of class and print info
sally = student('Sally', 'Junior')
sally.display()
# printed: Name: Sally , Grade: Junior

# 9. add both students to array class variable using class method
student.addStudent(bill)
student.addStudent(sally)
# class method called for both instances

# 10. call class method to print info for all instances
print('–––––––')
student.displayStudents()
# printed:
    # –––––––
    # Name: Bill , Grade: Freshman
    # Name: Sally , Grade: Junior




# Page 8 - Person Classes Activity
    # Given the Person class below, create a Greeter class with a
            # single static method named greet. This method should:
        # Accept one parameter named people that is a list of Person
            # objects.
        # Create a list of greetings (strings). There will be one
            # greeting per person. Each should say "Hello FIRST
            # LAST!", where "FIRST" and "LAST" are replaced with the
            # values from the person (firstName and lastName).
        # Return the array of greetings.

    # For instance, if the input to the static greet method of the
            # Greeter class were two people named "Bill Barnes" and
            # "Sally Smith", the result would be an array of two
            # Strings:
        # "Hello Bill Barnes!"
        # "Hello Sally Smith!"

    # The Person class is defined as follows (you do not need to add
        # this to your code):
class Person:
    """This is a person"""

    def __init__(self, firstName, lastName):
        """Initializer"""
        self.firstName = firstName
        self.lastName = lastName



    # Solution (my many attempts below) - I was close with attempt
        # 3, which was what I chose to submit, but missed the step
        # of creating an empty greeting list in the class and
        # appending the greetings to that list, AND I forgot the
        # docstring for the method in all my attmpts
class Greeter:
    """This is a greeter"""

    @staticmethod
    def greet(people):
        """Static method to greet a list of people"""
        greetings = []
        for person in people:
            greeting = ('Hello ' + person.firstName + ' ' +
                        person.lastName + '!')
            greetings.append(greeting)
        return greetings

    # using my drafts to call the solution class method
meMyself = Person('Me', 'Myself')
andI = Person('and', 'I')

people = [meMyself, andI]

print(Greeter.greet(people))
# success, this returned: ['Hello Me Myself!', 'Hello and I!']


    # attempt 1
class Person:
    """This is a person"""

    def __init__(self, firstName, lastName):
        """Initializer"""
        self.firstName = firstName
        self.lastName = lastName


class Greeter:
    """Greet people"""

    @staticmethod
    def greet(people):
        greeting = (('Hello', people[0], '!'),
                    ('Hello', people[1], '!'))
        return greeting


meMyself = Person('Me', 'Myself')
andI = Person('and', 'I')

people = [meMyself, andI]

Greeter.greet(people)
# created class and instances from provided class in a list, then
    # called class method and it returned:
        # (('Hello', <__main__.Person at 0x7fc429760b50>, '!')
        # ('Hello', <__main__.Person at 0x7fc4297604f0>, '!'))


    # above didn't work - attempt 2
class Person:
    """This is a person"""

    def __init__(self, firstName, lastName):
        """Initializer"""
        self.firstName = firstName
        self.lastName = lastName


class Greeter:
    """Greet people"""

    @staticmethod
    def greet(people):
        greeting = 'Hello', Person.firstName, Person.lastName, '!'
        return greeting


people = [Person('Me', 'Myself'), Person('and', 'I')]

Greeter.greet(people)
# AttributeError: type object 'Person' has no attribute 'firstName'
    # as expected, actually, this didn't work b/c the name
    # properties are instance, not class properties


    # above didn't work - attempt 3
class Person:
    """This is a person"""

    def __init__(self, firstName, lastName):
        """Initializer"""
        self.firstName = firstName
        self.lastName = lastName


class Greeter:
    """Greet people"""

    @staticmethod
    def greet(people):
        for person in people:
            greeting = ('Hello', person.firstName, person.lastName,
                        '!')
        return greeting


people = [Person('Me', 'Myself'), Person('and', 'I')]

Greeter.greet(people)
# returned: ('Hello', 'and', 'I', '!')


    # above didn't work - attempt 4
class Person:
    """This is a person"""

    def __init__(self, firstName, lastName):
        """Initializer"""
        self.firstName = firstName
        self.lastName = lastName


class Greeter:
    """Greet people"""

    @staticmethod
    def greet(people):
        for person in people:
            greeting = 'Hello', people.firstName, people.lastName,
            '!'
        return greeting


people = [Person('Me', 'Myself'), Person('and', 'I')]

Greeter.greet(people)
# AttributeError: 'list' object has no attribute 'firstName'


    # above didn't work - attempt 5
class Person:
    """This is a person"""

    def __init__(self, firstName, lastName):
        """Initializer"""
        self.firstName = firstName
        self.lastName = lastName


class Greeter(Person):
    """Greet people"""

    @staticmethod
    def greet(people):
        for person in people:
            greeting = ('Hello', person.firstName, person.lastName,
                        '!')
        return greeting


meMyself = Person('Me', 'Myself')
andI = Person('and', 'I')

people = [meMyself, andI]

Greeter.greet(people)
# Returned: ('Hello', 'and', 'I', '!')


    # above didn't work - attempt 6
class Person:
    """This is a person"""

    def __init__(self, firstName, lastName):
        """Initializer"""
        self.firstName = firstName
        self.lastName = lastName


class Greeter():
    """Greet people"""

    @staticmethod
    def greet(people):
        for person in people:
            greeting = ('Hello', getattr(person, firstName),
                        getattr(person, lastName), '!')
        return greeting


meMyself = Person('Me', 'Myself')
andI = Person('and', 'I')

people = [meMyself, andI]

Greeter.greet(people)
# NameError: name 'firstName' is not defined




# Page 9 - Rectangle Classes Activity
    # Create a class named Rectangle that:
        # Has two properties width and height.
        # Has an initializer to set the two properties.
        # Has a method named area() that has no parameters (other
            # than self) and returns the area of the rectangle (the
            # product of the width and height).
class Rectangle:
    """Input rectangle dimensions to find area"""

    def __init__(self, width, height):
        """Define width and height of rectangle"""
        self.width = width
        self.height = height

    def area(self):
        """Calculate area"""
        return self.width * self.height

twoFour = Rectangle(2, 4)

print(twoFour.area())
# created class, created instance, and called instance method
    # success! printed: 8




# Page 10 - Hands-On
    # From workshop - https://vimeo.com/426091587

# Let's set up classes for a video game. They have different
    # types of characters you can play. Barbarian!

    # Define the barbarian class
class Barbarian:
    """Class for Barbarian video game"""

    def __init__(self, name, weapon, enemiesVanquished):
        """Initializer"""
        self.name = name
        self.weapon = weapon
        self.enemiesVanquished = enemiesVanquished

    def victory(self):
        """"Print statement about barbarian"""
        print(self.name, 'the barbarian has had victory over',
              self.enemiesVanquished, 'enemies with a',
              self.weapon + '!')
# class created


    # create an instance
Conan = Barbarian('Conan', 'sword', '721')
# instance created


    # call the function
Conan.victory()
# printed: Conan the barbarian has had victory over 721 enemies with
    # a sword!


    # add another instance property and function to the barbarian
        # class
class Barbarian:
    """Class for Barbarian video game"""

    def __init__(self, name, canRead, weapon, enemiesVanquished):
        """Initializer"""
        self.name = name
        self.canRead = canRead
        self.weapon = weapon
        self.enemiesVanquished = enemiesVanquished

    def victory(self):
        """"Print statement about barbarian"""
        print(self.name, 'the barbarian has had victory over',
              self.enemiesVanquished, 'enemies with a',
              self.weapon + '!')

    def educated(self):
        """Print exclamation if barbarian can read"""
        if self.canRead == True:
            print('Wow! I can\'t believe', self.name, 'can read!')
# class updated


    # update instance
Conan = Barbarian('Conan', True, 'sword', '721')
# it's official: Conan can read ;)

    # call both functions
Conan.victory()
Conan.educated()
# printed:
    # Conan the barbarian has had victory over 721 enemies with a
        # sword!
    # Wow! I can't believe Conan can read!


    # create another instance
Barbarella = Barbarian('Barbarella', False, 'spear', '100')
# instance created

    # call both functions for new instance
Barbarella.victory()
Barbarella.educated()
# printed:
    # Barbarella the barbarian has had victory over 100 enemies with
        # a spear!
# note: no 'Wow!' statement printed b/c of the False value for the
    # canRead property
