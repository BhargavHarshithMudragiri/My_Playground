
my_list=[1,2,3,4,5,6,1,2,8,9]
print("This is my list", my_list)

my_list.append(10)
print("After Append", my_list)

my_list.extend([11,12,13])
print("After Extend", my_list)

my_list.insert(0,0)
print("After inserting new value at index 0", my_list)

#Removes the first occurance of value 0
my_list.remove(0)
print("After removing the first occurance of 0", my_list) 

#Removes the last item in the list
popped_element= my_list.pop()
print("Poped Element is: ", popped_element)
print("After pop", my_list)

#Getting the index of the value 5
index_of_5 = my_list.index(5)
print("Index value of item 5 is: ", index_of_5)

#Getting count of a value 2 in the list
count_value = my_list.count(2)
print("Number of occurances of value 2 is: ", count_value)

#Sorting the list
my_list.sort()
print("After sorting: ", my_list)

#Reverse the list
my_list.reverse()
print("After Reverse: ", my_list)

#Copying the list to another list
Copied_list = my_list.copy()
print("After copy: ", Copied_list)

#List properties and functions

print("Length of the list: ",len(my_list))
print("Length of the copied list: ",len(Copied_list))
print("Maximum Element in the list: ", max(my_list))
print("Minimun Element in the list: ", min(my_list))
print("Sum of the elements in the list: ", sum(my_list))

#Clearing the list
my_list.clear()
print("After clearing list: ", my_list)

