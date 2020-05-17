#Object Oriented Programming in Python:
##Looking at Static and Class methods and attributes:-
# Minute stopped = ... into the video.

#Class Attributes are Attributes that are specifc to the class not to an instance where an object of that class.
class Person:
  number_of_people = 0 
  ##This attribute/variable above is a class attribute. 
  ###The reason it is a class attribute and not a regular attribute is because we do not need to use self before it.
  ###So because it is not defined within any method, have access to an instance of the class, it is then defined for the entire ###class. Meaning it will not change for any instance of the class. not matter what values the insatnce use. so number_of_people = ###0, will always equal 0.

  def __init__(self, name):
    self.name = name
    Person.number_of_people += 1

p1 = Person("Michael")
print(p1.number_of_people)
print("\n")

p2 = Person("Avon")
print(p1.number_of_people)
print("\n")

p3 = Person("Avon")
print(p1.number_of_people)
print("\n")

p4 = Person("Avon")
print(p1.number_of_people)
print("\n")
