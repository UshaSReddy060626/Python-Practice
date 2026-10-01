#program that creates a new list containing only the even numbers greater than 8.
numbers = [12, 5, 8, 21, 10, 3, 16]
print([number for number in numbers if number > 8 and number%2==0])