# Define the Person class
class Person:
    """
    A class to represent a person with a first name, last name, and age.
    """
    def __init__(self, firstname, lastname, age):
        """
        The constructor for the Person class.
        Initializes the firstname, lastname, and age attributes.
        """
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        """
        Prints a greeting message containing the person's name and age.
        """
        print(f"Hello, my name is {self.firstname} {self.lastname} and I'm {self.age} years old")

# --- Example Usage ---
# Create a new Person object
person1 = Person("Oleksandra", "Andrushchenko", 42)

# Call the talk() method on the person1 object
person1.talk()

# You can create other instances too
person2 = Person("Ivan", "Ivanenko", 30)
person2.talk()