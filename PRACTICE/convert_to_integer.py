"""Convert to Integer
Ask the user to enter a number and convert it to an integer using int().
Use try-except to handle invalid input such as "hello"."""
try:
    user_input=input("enter a number:")
    print(int(user_input))
except ValueError:
    print("enter the correct value")
