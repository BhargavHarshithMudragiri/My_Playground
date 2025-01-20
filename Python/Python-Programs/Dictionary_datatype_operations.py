
my_dict = { 
           "name" : "Bhargav",
           "region" : "India",
           "age" : 30,
           "phone" : "+91-9963874454"
           }
#To view Dictionary Keys
dict_keys = my_dict.keys()
print("Dictionary Keys are : ", dict_keys)

#To view Dictionary values
dict_values = my_dict.values()
print("Dictionary values are: ",dict_values)

#To view all Dictionary keys and values
dict_items = my_dict.items()
print("Dictionary Items are: ",dict_items)

#Accessing a value by key
region = my_dict['region']
print("Region is: ",region)

#Accessing a value by using get
phone_num = my_dict.get('phone')
print("Phone Number is: ",phone_num)

#Accessing a key with default value
salary = my_dict.get('salary','Not Available')
print("Salary is: ",salary)

#Add a new key-value pair
my_dict["occupation"] = 'Engineer'
print("After adding occupation: ",my_dict)

#Removing a key-value pair using pop
popped_value = my_dict.pop('age')
print("popped item is: ", popped_value)
print("After pop: ", my_dict)

