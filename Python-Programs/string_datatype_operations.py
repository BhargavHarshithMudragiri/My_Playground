my_string  = "Hello world! I am Bhargav harshith. Happy learning"
print(f"This is my string: {my_string}")

#Length of the string
print(f"Length Of The String is: {len(my_string)}")

#UpperCase of the string
print(f"Upper Case of the string is: {my_string.upper()}")

#Lowercase of the string
print(f"Lower case of the string is: {my_string.lower()}")

#Count occurances of a substring in the given string
Substring = "Bhargav"
print(f"Number of occurances of '{Substring}' are: {my_string.count(Substring)}")

#To check if string starts with hello
print(f"Is String starts with Hello ?: {my_string.startswith('Hello')}")

#To check if string ends with learning
print(f"Ends with Learning ?: {my_string.endswith('learning')}")

#To convert string into title
print(f"Title is: {my_string.title()}")

#To find the index value of substring Harshith
print(f"Index value of Harshith is: {my_string.find('harshith')}")

#To Replace a substring in the original string with another substring
print(f"Replaced String is: {my_string.replace('Bhargav','Rebel')}")
print(f"Original String is: {my_string}")

#To Split given string into list based on a delimiter
ListOfWords = my_string.split()
print(f"Split into words: {ListOfWords}")

#To check if all charecters are alpha numeric
alphanumeric_string = "bhargavharshith2695"
print(f"Is it alphanumeric string ?: {alphanumeric_string.isalnum()}")

