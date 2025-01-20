#Integer Examples
x = 10
y= -5
z=100

#Float Examples
a = 10.5
b = -5.5
c = 3e4  #Exponential value equivalent to 3*10^4

#Complex Number Examples
d= 2+3j
e= 1-6j

#Print Value of X & Y
print(f"Value of x is {x}")
print(f"Value of y is {y}")

#Arithmetic Operations
print(f"x + y is: {x+y}")
print(f"x - y is: {x-y}")
print(f"x * y is: {x*y}")
print(f"x / y is: {x/y}")
print(f"x % y is: {x%y}")

#TypeCasting variables
f = float(x)
print(f"Float of integer {x} is: {f}")

g = int(a)
print(f"Integer of float {a} is: {g}")

h = complex(b,c)
print(f"Create complex number: h = {h}")