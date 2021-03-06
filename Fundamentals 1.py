import math

#######################
#FUNDMENTAL DATA TYPES
#######################

##The data types:
#- int
#- float
#- bool
#- str
#-list
#- tuple
#- set
#- dict
#- complex

#Operators:

#- ** is to the power of/indices
#- + is to Add
#- / is to divide.
#- () is to use brackets
#- * is to multiply
#- % is to find remainder/modulus
#- - is to subtract

print('Operators:')
print(3**4)
print(55 + 7)
print(44 / 2)
print(((22 - 5) * 2) - 15)
print(9 * 7)
print(66 % 8)
print(1 - 3.14)
print("\n\n")

#Type:

#Getting the data types of an expression (using 'type'):
print('Types:')
print(type(6))
print(type(0))
print(type(2 - 3))
print(type(2 * 4))
print(type(2 / 4))
print(type(6 % 3))
print(type(6**3))
print("\n\n")

#Math Functions:

# round - is to round a number to its nearest integer.

# abs - is to get the absolute value of a number meaning it cannot be negative, ONLY postive.

# sqrt(x) -  is to return the square root of x

# pow(x, y) -  is to return x raised to the power y

#log10(x) -  is to return the base-10 logarithm of x

print('Math Functions:')
print(round(6.6935))
print(round(2.19))
print(abs(-98))
print(abs(8.5))
print(math.sqrt(49))
print(math.sqrt(10))
print(pow(4, 3))
print(pow(16, 2))
print(math.log10(80))
print("\n\n")

#ASCII codes and binary:

# bin() - is

# int(binary code, base 2)

print('Binary and Ascii codes:')
print(bin(5))
print(bin(9))
print(int('0b101', 2))
print(int('0b1001', 2))
print(int('0b1011', 2))
print("\n\n")

#Variables and Constants:
print('Constants and Variables')
# Constants - are variables that NEVER change. These are usually left in capitals.

#Below are some examples of Constants that I made:

PI = 3.1457
print(PI)

ENTERAGE = 21
print(ENTERAGE)

#Variable examples:
a, b, c, d = 1, 3, 5, 9
print(a)
print(b)
print(c)
print(d)
print("\n\n")

#String:

#''' is used for long string/paragraphs of strign text
print('String')
print(type("Hi Hello, number 23! Reply. Now!!!"))
username = 'Supercoder'
password = 'supers'

long_string = '''
\nWOOOOW
 0  0
 ----
 ----
'''
print(long_string)

first_name = 'Mike-El '
last_name = 'Tabi'
full_name = first_name + last_name
print(full_name)

print('Hello Number ' + str(9))
print(str(100))

print(type(int(str(100))))

a = str(100)
b = int(a)
c = type(b)
print(c)

weather = "Its kind of sunny"
print(weather)

weather2 = "It\'s \"kind of\" sunny"
print(weather2)
print("\t python \t program")
print(weather)

name = 'Mike-El'
age = str(23)

print('\n0.\nHi ' + name + '.\nYou are ' + age + 'years old.')

print(f'\n1.\nHiya {name}. How are you?\nYou are {age} years old.Damn')

print('\n2.\nHiya {}. How are you?\nYou are {} years old.Damn'.format('Mike-El','23'))

print('\n3.\nHiya {}. How are you?\nYou are {} years old.Damn'.format(name, age))

print('\n4.\nYoo {new_name}. What you saying?\nYou\'re {new_age} years old.Damn'.format(new_name='Karen', new_age='33'))
print("\n\n")


#String Indexes:

selfish = '012345678'
      #    012345678

      #[Start:Stop]
print(selfish[0:9])
print(selfish[0:6])
print(selfish[0:2])
print('\n')
print(selfish[0:8:2])
print(selfish[1:9:2])
print(selfish[0:9:3])
print('\n')
print(selfish[0:])
print(selfish[7:])
print(selfish[3:])
print('\n')
print(selfish[:2])
print(selfish[:4])
print(selfish[:7])
print('\n')
print(selfish[::])
print('\n')
print(selfish[-1])
print(selfish[-3])
print(selfish[-2])
print('\n')
print(selfish[:-1])
print(selfish[::-1])
print(selfish[::-5])
print(selfish[::-2])
print(selfish[::-4])
print(selfish[::-3])
print('\n\n')



#Built-In Functions and Methods:

print('Built-In Functions and Methods')
print(len('hellloooo'))
print('\n')

randword = 'deasd'
greeting = 'yooiooio'
print(greeting[0:9])
print(greeting[0:5])
print(greeting[0:3])
print('\n')
print(greeting[0:len(greeting)])
print(greeting[0:len(randword)])
print('\n')
quote = 'To be or not to be'
print(quote.upper())
print(quote.capitalize())
print(quote.find('be'))
print('\n')
print(quote.replace('be','flee'))
print('\n')
quote2 = quote.replace('to', 'you')
print(quote2)
