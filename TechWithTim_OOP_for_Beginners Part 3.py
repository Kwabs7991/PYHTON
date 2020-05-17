#Object Oriented Programming in Python:
##Looking at Inheritence:-


### Pet class = PARENT CLASS
class Pet:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show(self):
    print(f"I am {self.name} and I am {self.age} years old.")

  def speak(self):
    print("Ummm I dont know what to say.")


### Cat class = CHILD/DERIVATIVE CLASS
class Cat(Pet):
  '''
  so here we are still calling the attributes from the parent class 'Pet',
  and stating a new attribute 'color', to be used only in the Cat class. 
  Here when we do an inheritence like this, we still need to initalise them, i.e. __init__, 
  to make sure the object was set u properly. Then instead of using self.age, self.name, we simply use super(), since we are referring to the super class Pet, in a child/derivative class Cat.
  '''
  def __init__(self, name, age, color):
    super().__init__(age, name) # You do not need to pass self when using super(). 
    self.color = color

  def speak(self):
    print("Meow")
  
  def show(self):
   print(f"I am {self.name} and I am {self.age} years old and I am {self.color}.")


### Dog class = CHILD/DERIVATIVE CLASS
####Inherits methods from Class Pet as well as using its own.
class Dog(Pet):
  def speak(self):
    print("Woof")



### Fish class = CHILD/DERIVATIVE CLASS
####Inherits methods from Class Pet as well as using its own.
class Fish(Pet):
  pass

p = Pet("Tim", 19)
p.show()
p.speak()

print("\n")
cat = Cat("Snuggles", 19, "Blue")
cat.show()
cat.speak()

print("\n")
dog = Dog("Simon", 19)
dog.show() 
dog.speak()

print("\n")
fish = Fish("Cap", 19)
fish.show() 
fish.speak()
