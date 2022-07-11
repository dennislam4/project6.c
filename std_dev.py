# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 7/11/2022
# Description: A class that indicates a person's name and age and a function that returns the standard deviation
# of a list of Person and their ages.
class Person:
    """Represents a person's name and age."""
    def __init__(self, name, age):
        """Initializes the name and age values of a person."""
        self._name = name
        self._age = age

    def person_age(self):
        """Returns the person's age."""
        return self._age

def std_dev(person_list):
    """Returns the standard deviation of ages within the list of persons."""
    x = 0

    for person in person_list:
         x += person.person_age()
    mean_of_age = x / len(person_list)
    y = 0

    for person in person_list:
         y += (mean_of_age - person.person_age()) ** 2
    return (y / len(person_list)) ** (1 / 2)
