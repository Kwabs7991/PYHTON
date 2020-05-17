#Object Oriented Programming in Python:
##Looking at Static methods and attributes:-

class Math:

  @staticmethod
  def add5(x):
    return x + 5

  @staticmethod
  def add10(x):
    return x + 10

  @staticmethod
  def pr():
    print("run")
  
print(Math.add10(15))
print(Math.add5(15))
Math.pr()

##From what I understand:

### instance methods require the class to be instantiated.
###Classmethods can access other class attributes
###Static Methods are self contained and cannot access other attribute or access other methods within that class.
