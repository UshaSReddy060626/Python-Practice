#square no using comprehensions
sq=[i**2 for i in range(1,51)]
print(sq)

#square of no's greater than 5
numbers = [2, 5, 6, 8, 10]
result=[number**2 for number in numbers if (number > 5)]
print(result)