print('Hello World!\n\n\n\n')

#Sets and its methods:

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# .difference: going to find the difference with one set to another-In this case what in 'my_set' is different when looking at 'your_set'. Duplicates will be ignored.
print(my_set.difference(your_set))

print(your_set.difference(my_set))

print('\n\n')

# .discard: going to remove an element from a set if it is a member:-
# print(my_set.discard(5))
# print(my_set)
#print('\n\n\n')


# .difference_update:
##going to remove all elements of another set from this set:-
#print(my_set.difference_update(your_set))
# print(my_set)
#print('\n\n\n')


# .intersection:
## returns the two common things between two sets
# print(my_set.intersection(your_set))
#print('\n\n\n')


# .isdisjoint:
## are the two sets overlapping, true or false will be returned.
# print(my_set.isdisjoint(your_set))
#print('\n\n\n')


# .issubset()
print(my_set.issubset(your_set))
print('\n\n\n')



# .issuperset()
print(your_set.issuperset(my_set))
print('\n\n\n')
#print('\n\n\n')


# .union()
# print(my_set.union(your_set))

# print(my_set | your_set)
#print('\n\n\n')
