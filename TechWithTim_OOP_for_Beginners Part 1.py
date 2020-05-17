#Object Oriented Programming in Pyhton:


class Dog:
    '''
  This special method, __init__ allows to instantiate the object right when it is created. so it is called whenever you imstantiate an object- e.g. ''d = bark()

  Whenever we do this, the __init__ method will be called and  will apss any arguments that we put within the barkets, look to the "instantiating of objects" section below:
  '''

    def __init__(self, name, age):
        self.name = name  #What we've done here is created an attribute of the class dog, which is 'name'. What this means is everytime we create a new dog object we will pass a name through the parameter being used, in this case we are focusing on 'name'.
        self.age = age

    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    #def add_one(self, x):
    #   return x + 1

    #def bark(self):
    #   print("bark")


# Instantiating of Objects Section:
##
d = Dog("Jimmy", 14)
d2 = Dog("Lucas", 2)
d3 = Dog("Sarah", 20)

print("\n")
print(d.get_name())
print(d.get_age())

print("\n")
print(d2.get_age())
d2.set_name("Lucaaaask")
print(d2.get_name())

print("\n")
d3.set_age(21)
print(d3.get_age())

#d.bark()
#print(type(d))
#print(d.bark)
