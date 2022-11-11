"""Hands-on for DSO109 for Lesson 6."""
# DSO109 - Programming Foundations - Python
    # Lesson 6 - Object Oriented Programming

# Page 10 - Hands-On

# Part I
    # 1. Create a class named Stadium
    # 2. Use the init method to include the following three
                # properties:
            # name
            # city_state
            # capacity
        # Hint! What is the property that is included in every
            # method? Don't forget that one!
    # 3. Initialize each property/attribute within the init method
    # 4. Include a docString for the class and method
    # 5. Create another method within the Stadium class named
        # describe_stadium
    # 6. The describe_stadium method should utilize each method from
        # the Stadium class which will then print a description of
        # the arena (see step 10 for an example of a description)
class Stadium:
    """Stadium info"""

    def __init__(self, name, city_state, capacity):
        """Initializer"""
        self.name = name
        self.city_state = city_state
        self.capacity = capacity

    def describe_stadium(self):
        """Print stadium info"""
        print('The', self.name, 'is located in', self.city_state,
              'and holds', self.capacity, 'fans.')
# class created based on requirements 1-6


    # 7. Create a new instance of the Stadium class named stadium1
    # 8. The stadium1 instance should provide values for each of the
        # three properties of the Stadium class
stadium1 = Stadium('Mercedes Benz Arena', 'Atlanta, GA', '70,000')
# instance created


    # 9. Finally, stadium1 should call the describe_stadium method.
    # 10. The output should be similar to the following:
        # The Mercedes Benz Arena is located in Atlanta, GA and
        # holds 70,000 fans.
stadium1.describe_stadium()
# success! printed:
    # The Mercedes Benz Arena is located in Atlanta, GA and holds
        # 70,000 fans.




# Part II
    # 1. Add two more methods to the Stadium class:
        # sport_played - This method should accept one argument that
            # specifies the sport that is played
        # seats_available - This method should accept one argument
            # that specifies how many seats are available
    # 2. Each of the above method should print out a sentence using
        # the argument provided (see step 4 for output)
class Stadium:
    """Stadium info"""

    def __init__(self, name, city_state, capacity):
        """Initializer"""
        self.name = name
        self.city_state = city_state
        self.capacity = capacity

    def describe_stadium(self):
        """Print stadium info"""
        print('The', self.name, 'is located in', self.city_state,
              'and holds', self.capacity, 'fans.')

    def sport_played(self, sport):
        """Define and print stadium's main sport"""
        print(
            'The following sport is mainly played in this stadium:',
            sport)

    def seats_available(self, seats):
        """Define and print # of seats"""
        print('There are', seats,
              'seats still available for tonight\'s game.')
# class updated


    # 3. Using the stadium1 instance, call each of the new methods,
        # providing the relevant arguments. As an example, if the
        # following code to use the class were added:
    # 4. After running this program in your terminal, the output
            # should be similar to the following:
        # The Mercedes Benz Arena is in Atlanta, GA and holds 70000
            # fans.
        # The following sport is mainly played in this stadium:
            # Football
        # There are 15000 seats still available for tonight's game.
stadium1.describe_stadium()
stadium1.sport_played('Football')
stadium1.seats_available('15000')
# success! printed:
    # The Mercedes Benz Arena is located in Atlanta, GA and holds
        # 70,000 fans.
    # The following sport is mainly played in this stadium: Football
    # There are 15000 seats still available for tonight's game.
# note: what's weird is that this wouldn't run, and I couldn't find
    # any issues... so eventually I quit the program (Spyder) and
    # re-opened it, and then it ran successfully...
