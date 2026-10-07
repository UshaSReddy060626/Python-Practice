"""Divide Two Numbers
Take two numbers from the user and divide the first by the second.
Use try-except to handle division by zero."""
try:
    a=float(input("enter the first number:"))
    b=float(input("enter the second number:"))
    c=a/b
    print("Result=",c)
except ZeroDivisionError:
    print("the number cant be divided by zero")
except ValueError:
    print("enter the correct values")
