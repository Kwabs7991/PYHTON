def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

#Ternary Operators:-
##A ternary Operator is also jknown as a conditional expression.
##It is a condition that evaluates to something based on the condtion being true or not.

#Condition_ifitisTrue if condition else condition_ifitisFalse

##So it doesnt start at the start of the line. In fgact it starts at the if , so 'if condition' is true then we go left to the 'Condition_ifitisTrue', and if it is false then we go right to 'condition_ifitisFalse'.

isFriend = True

can_Message = "Message allowed" if isFriend else "Not allowed ot message."

print(can_Message)


#Short Circuiting:
is_Friend = True
is_User = True

if is_Friend or is_User:
  print('Best Fiends')
print('\n\n\n\n')



#Logical Operators

## > 'This' is Greater than 'That'
## < 'This' is Less Than 'That'
## =  Assigninig variable
## == Equals to
## >= Greater than or Equal to
## <= Less than or equal to
## != Not equal to
## not Opposite, e.g: print(not(1 == 1))


#Exercise for Logical Operators:

is_Magician = True
is_expert = False

#check if magician AND expert: "You are a MASTER magician."

#check if magician AND not expert: "Dont Worry, Youre Getting there."

#check if NOT a magician: "You are in need of magic powers."

if is_Magician and is_expert:
  print('You are a MASTER magician.')
elif is_Magician and not(is_expert):
  print('Dont Worry, You\'re Getting there.')
elif not(is_Magician):
  print('You are in need of magic powers.')
print('\n\n\n\n')


#is .vs. ==

# '==' checka for the equality in values
# 'is', however, checks the location of memeory anbd checks the compared is in the same location of memory.

print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])
#
print('\n\n')

#use == or != to compare str, bytes, and int literals

print([] is []) 
# Whenever you create a new list it createsa list in a new location in memory.


print(True is True)
print('\n\n')

for item in 'Zero to Mastery':
  print(item)
print('\n\n')

for item in {1,2,3,4,5}:
  print(item)
print('\n\n')


for item in (1,2,3,4,5):
  print(item)
print('\n\n')


for item in (1,2,3,4,5):
  for x in ['a', 'b', 'c']:
    print(item,x)


#An Iterable, can be a; list, dictionary, tuple, set, it is a collection of items. this is because they can iterated.
#Iterate - we go through a one-by-one check each item in the collection.

user={
  'name': 'duncan',
  'Surn': 'Alicia',
  'age' : 35,
  'can_swim' : True
}

#prints keys of dictionary
print('\n\n')
for item in user:
  print(item)
print('\n\n')

#prints key-value pair of dictionary
for item in user.items():
  print(item)
print('\n\n')
#or we can use the below instead:

for k, v in user.items():
  print(k, v)
print('\n\n')


for item in user.values():
  print(item)
print('\n\n')
