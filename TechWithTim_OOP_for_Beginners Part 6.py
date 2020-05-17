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
    Person.number_of_people_()
    Person.add_person()

    '''
    Definition of a class: A class is a code template for creating objects, similar to a blueprint for a program if you will.

    Class Methods:

    So class Methods use 'cls' instead of 'self', also they use a decorator above the actual method/function.
    This decorator is written as '@classmethod'. 

    If the created method is an instance method then the reserved word, self ha to be used, but if the method is a class methodthen the keyword cls must be used.

    So if we look at the classmethod 'number_of_people', it will not be acting on behalf of 1 isinstance.
    What is is instead meant to do is be called on the class itself so it can deal with, for example, the no. of ppl 
    associated with this class 'Person'.
    '''
  
  @classmethod
  def number_of_people_(cls):
    return cls.number_of_people

  @classmethod
  def add_person(cls):
    cls.number_of_people += 1

p1 = Person("Michael jr.")
p2 = Person("Avon")
p3 = Person("Ezekiel")
p4 = Person("Tobias")
print(Person.number_of_people_())


##From what I understand:
### instance methods require the class to be instantiated.
###Classmethods can access other class attributes
###Static Methods are self contained and cannot access other attribute or access other methods within that class.
