#To write simple conditional expression called If

num = float(input("Enter the number of your choice: "))
if num > 0:
    print("Number is POSITIVE")
elif num < 0:
    print("Number is NEGATIVE")
else:
    print("Number is ZERO")