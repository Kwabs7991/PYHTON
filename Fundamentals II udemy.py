
for i in range(5):
  print('A number:', i)

  #45. Common List Patterns

new_basket = ['a', 'x','k','c','d','e','f']

new_basket.sort()
new_basket.reverse()
print('\n')

print(new_basket)
print('\n')

print(len(new_basket))
print('\n')

for i in range(11):
  print('Kaitlin!')
print('\n')

new_basket.sort()
new_basket.reverse()
print(new_basket[::-1]) #All items in the array are reversed, again
print(new_basket)
print('\n\n')




##a[::-1]    # all items in the array, reversed.

##a[1::-1]   # the first two items, reversed.

##a[:-3:-1]  # the last two items, reversed.

##a[:]   # makes a copy of the list.

##a[-3::-1]  # everything except the last two items, reversed

print(list(range(1,100)))
print('\n\n')
print(list(range(100)))
print('\n\n')


#List Unpacking

a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]

print(a)
print(b)
print(c)

print(other)

print(d)


#None


weapons = None
print(weapons)
print('\n\n\n')


# Dictionary - in other languages its known as a hashtable or maps.

# A dictionary is an unordered key value pairing. As long as we know the key, then we can just use that.


dictionary = {

  'a':1,
  'b':2,
  'c':3,
  'd':4
}

print(f'\nDictionary:\n{dictionary}')
print(dictionary['b'])

#The data can be anything we want like a string, or list, or a boolean value, etc.
print('\n\n')
dictionary2 = {

  'e' : [1,2,3,4,5,6,7],'f' : 'Heyoooo',
  'g' : False,
  'h' : True,
  'i': 1+2+3
}

print(dictionary2['f'])
print(dictionary2['g'])
print(dictionary2['e'])
print(dictionary2['i'])
print(dictionary2['i'])

print('\n\n')

new_list = [
{
  'e' : [1,2,3,4],
  'f' : 'Heyoooo',
  'h' : True,
  'i': 1+2+3+6
},
{
  'x' : [5,6,7],
  'h' : 'Hiyaaa',
  'k' : False,
  'i': 1+2+4+8
}
]

#What is this saying:
##what this is printing out is:
### Look at the first item i the list array, then the 'a' key, and then the thrid  index in its array.
print(new_list[0]['e'][3])

print(new_list[1]['i'])
print('\n\n\n')

#More dictionery Methods

##What this goes over is, grab thge 'age' from the user dictionary, if age does not exist in the 'ppls' dictionary, use 55 in place as it returns, but if it does exist then use the value for 'age'.

ppls ={
  'basketo': [1,2,3],
  'greet': 'hello',
  'age' : 22
}

print(ppls.get('age',55))
print('\n\n')

#Even More Dictionery stuff:


usery = {
  'baske': [3,5,9],
  'greeting' : 'hello',
  'age' : 22
}

print('baske' in usery)
print('\n\n')
print('gender' in usery)
print('\n\n')

#To check the keys and values:

print(usery.keys())
print('\n')
print(usery.values())
print('\n')
print(usery.items())
print('\n\n')
print('baske' in usery.keys())
print('size' in usery.keys())

print(1 in usery.values())
print('hello' in usery.values())

print(usery.pop('age'))
print(usery)

##This removes a random key-value pair in the dictionary
print(usery.popitem())
print(usery)
print('\n\n\n')
#Update: updates a key value. If you decide to update a key item that does not exist, like 'death' it will update the dictionary by adding 'death' and its value to the dictionary.

print(usery.update({'baske' : 55}))
print(usery)

print('\n\n')

print(usery.update({'death' : 88}))
print(usery)
