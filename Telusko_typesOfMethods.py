#Types of Methods:
#We have two types of object: Attributes and methods.
#We have 3 types of methods
##1. Instance Methods
##2. Class Methods
##3. Static Methods

class Student:
  # Here we see class variables. These can be used with class methods.
  school = 'Telusko'

  def __init__(self, s1, s2, s3):
    # Here we see instance variables. These can be used with instance methods.
    self.s1 = s1
    self.s2 = s2
    self.s3 = s3

#This is an instance method. This is because we are passing self.
#When we say self it means it belongs to a particular object.

#We have 2 different types of instance methods: 

#1. (Getters) Acessor Method: If we are only fetching the value of the instance variable/attribute. 

#2. (Setters) Mutator Method: If you want to modify the the value of the instance variable.

# Normal Instance Method, can be considered a Getter Method.
  def average(self):
    return (self.s1 + self.s2 + self.s3)/3

# # Getter Method.
#   def get_m1(self, s1):
#     return self.get_s1

# # Setter Method.
#   def set_m1(self, s1value):
#     self.s1 = s1value

  @classmethod
  def get_school(cls):
    return cls.school

# Since this type of method is not related to an objects or class variables, we keep the brackets blank.
  @staticmethod
  def get_classInfo():
    print("This is Student class whatever... in abc module set.")


s1 = Student(34, 67, 88)
s2 = Student(22, 8, 99)
s3 = Student(78, 123, 52)

print(s1.average())
print(s2.average())
print(s3.average())


print(Student.get_school())
Student.get_classInfo()
