#sets: can be changed but dont allow for duplicates.
'''
my_set = {1, 2, 3, 4, 5} #uses curly brackets.
print(my_set)

my_set.add(6) #if you want to add a value to the set.
print(my_set)

my_set.remove(3) #if you want to remove a value from the set.
print(my_set)

''' #three dots used to coment work out of debugger.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

#Union: adds both sets and removes duplicate data.

union_set = set1.union(set2)
print(union_set)

#Intersection: finds common elements between to sets.

inter_set = set1.intersection(set2)
print(inter_set)

#Difference: find elements that are present in one but not the other.

diff_set = set1.difference(set2)
print(diff_set)

