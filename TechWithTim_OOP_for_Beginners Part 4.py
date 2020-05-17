#Object Oriented Programming in Python:
##Looking at Static and Class methods and attributes:-
# Minute stopped = 41:34 into the video.

#Class Attributes are Attributes that are specifc to the class not to an instance where an object of that class.
class Person:
  number_of_people = 0 
  ##This attribute/variable above is a class attribute. 
  ###The reason it is a class attribute and not a regular attribute is because we do not need to use self before it.
  ###So because it is not defined within any method, have access to an instance of the class, it is then defined for the entire ###class. Meaning it will not change for any instance of the class. not matter what values the insatnce use. so number_of_people = ###0, will always equal 0.

  def __init__(self, name):
    self.name = name

p1 = Person("Michael")
p2 = Person("Avon")

##To access the Class attribute, we can simply using the name of the class, dot, and then the class attribute Name.
##Look to example below to see what happens when you change the class attribute as you go down the code. Currently number_of_people is 0.
print(Person.number_of_people)
print(p1.number_of_people)

Person.number_of_people = 12
print(p2.number_of_people)
Person.number_of_people = 5
print(p2.number_of_people)
Person.number_of_people = 300
print(p1.number_of_people)
Person.number_of_people = 79
print(Person.number_of_people)
