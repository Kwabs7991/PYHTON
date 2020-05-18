#Topic: Range
##Range creates a special kind of object that we can iterate over.

#e.g.1
print(range(100))
print('\n\n\n\n')
#e.g.2
ran = range(0,50)
for numbre in ran:
  print(numbre)
print('\n\n\n\n')

  #e.g.3
for _ in range(0, 10, 2):
  print(_)
print('\n\n\n\n')

  #e.g.4
for _ in range(100, 10, -10):
  print(_)
print('\n\n\n\n')

  #e.g.3
  ##Here we loop two times, and then im going; to create a range of 10, so an iterable object of 10 items, and then convert that into a list.
for _ in range(2):
  print(list(range(10)))
print('\n\n\n\n')

#e.g.3
ranger = list(range(10, 0, -2))
for k in ranger:
  print('{}: {}'.format(k, ranger ))
print('\n\n\n\n')
print('\n\n\n\n')
print('\n\n\n\n')

#Enumeration
##Enumerate takes an editable object and gives you an index counter and the item of that index.For example:

#e.g.1
## i is the index of which the character is located
for i,char in enumerate('Surely, Surely'):
  print(i, char)
print('\n\n\n')

#e.g.2
for x,char in enumerate([1,2,3]):
  print(x, char)
print('\n\n\n')

#e.g.3
for x,char in enumerate(list(range(100))):
  if char == 50:
    print(f'index of 50 is {x}')
  else:
    continue
print('\n\n\n')
