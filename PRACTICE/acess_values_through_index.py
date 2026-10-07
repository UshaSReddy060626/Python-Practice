"""Ask the user for an index and print the element at that index.
Use try-except to handle an invalid index."""
try:
    numbers = [10, 20, 30, 40, 50]
    user_input=int(input("enter the index you want to access(0-4):"))
    print("your accessed value is:",numbers[user_input])
except ValueError:
    print("enter the correct value.")
except IndexError:
    print("please enter the correct index value.")