

my_set = {1,2,3,4,5}
print("Set values are: ", my_set)

my_set.add(6)
print("After Add: ", my_set)

my_set.remove(6)
print("After Remove: ", my_set)

Popped_Element = my_set.pop()
print("Popped Item: ", Popped_Element)
print("After  Pop: ", my_set)

my_set.clear()
print("After clear: ",my_set)

set_1 = {1,2,3}
set_2 = {3,4,5}

union_set = set_1.union(set_2)
print("After Union Operation: ", union_set)

intersection_set = set_1.intersection(set_2)
print("After Intersection: ",intersection_set)

diff_set = set_1.difference(set_2)
print("After Difference: ", diff_set)
