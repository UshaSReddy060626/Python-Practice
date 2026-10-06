# Python — Sets, Dictionaries, Conditionals, Loops, Functions & Modules

## 1. Sets

A **set** is a collection of unique values.

```python
numbers = {1, 2, 3, 4, 5}
```

Duplicates are automatically removed:

```python
numbers = {1, 2, 2, 3, 3}

print(numbers)
```

Output:

```text
{1, 2, 3}
```

### Create an Empty Set

```python
numbers = set()
```

> `{}` creates an empty dictionary, not an empty set.

### Add and Remove

```python
numbers.add(10)
numbers.remove(2)
numbers.discard(5)
```

### Set Operations

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
```

#### Union

All elements from both sets.

```python
print(a | b)
```

#### Intersection

Common elements.

```python
print(a & b)
```

#### Difference

Elements in `a` but not in `b`.

```python
print(a - b)
```

#### Symmetric Difference

Elements that are not common.

```python
print(a ^ b)
```

### Membership

```python
if 3 in a:
    print("Found")
```

---

# 2. Dictionaries

A **dictionary** stores data as **key-value pairs**.

```python
student = {
    "name": "Aaru",
    "age": 20,
    "marks": 85
}
```

Here:

* `name` → key
* `Aaru` → value

### Access Values

```python
print(student["name"])
print(student["marks"])
```

### Using `get()`

```python
print(student.get("name"))
```

`get()` is safer when the key may not exist.

### Add a New Item

```python
student["city"] = "Bengaluru"
```

### Update a Value

```python
student["marks"] = 95
```

### Delete

```python
student.pop("age")
```

### Important Dictionary Methods

```python
student.keys()
student.values()
student.items()
```

### Loop Through Dictionary

```python
for key, value in student.items():
    print(key, value)
```

---

# 3. Conditional Statements

Conditions are used to make decisions.

## `if`

```python
age = 20

if age >= 18:
    print("Adult")
```

## `if-else`

```python
marks = 40

if marks >= 50:
    print("Pass")
else:
    print("Fail")
```

## `if-elif-else`

```python
marks = 85

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")
```

### Multiple Conditions

```python
age = 20
marks = 80

if age >= 18 and marks >= 50:
    print("Eligible")
```

Common operators:

```text
and
or
not
```

---

# 4. For Loop

A `for` loop is used to repeat something for each item.

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

### Loop Through a List

```python
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)
```

### Nested Loop

A loop inside another loop.

```python
for i in range(1, 4):

    for j in range(1, 4):
        print(i, j)
```

Nested loops are useful for things like **multiplication tables**.

---

# 5. While Loop

A `while` loop repeats while a condition is true.

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

Output:

```text
1
2
3
4
5
```

### Important

Always make sure the condition eventually becomes `False`.

Otherwise, you can create an **infinite loop**.

---

# 6. Loop Control

## `break`

Stops the loop completely.

```python
for i in range(1, 10):

    if i == 5:
        break

    print(i)
```

Output:

```text
1
2
3
4
```

### Remember

`break` = **Stop the loop**

---

## `continue`

Skips the current iteration.

```python
for i in range(1, 6):

    if i == 3:
        continue

    print(i)
```

Output:

```text
1
2
4
5
```

### Remember

`continue` = **Skip this round**

---

## `pass`

Does nothing.

It is mainly used as a placeholder.

```python
for i in range(5):

    if i == 3:
        pass

    print(i)
```

### Remember

```text
break    → stop
continue → skip
pass     → do nothing
```

---

# 7. Functions

A function is a **reusable block of code**.

```python
def greet():
    print("Hello")
```

Call the function:

```python
greet()
```

### Function With Parameters

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```text
30
```

### `return`

`return` sends a value back from the function.

```python
def square(n):
    return n * n

answer = square(5)

print(answer)
```

Output:

```text
25
```

---

# 8. `*args`

`*args` allows a function to accept multiple positional arguments.

```python
def total(*numbers):
    return sum(numbers)

print(total(10, 20))
print(total(10, 20, 30))
```

`*args` stores the values as a **tuple**.

```python
def show(*numbers):
    print(numbers)

show(10, 20, 30)
```

Output:

```text
(10, 20, 30)
```

### Remember

```text
*args → tuple
```

---

# 9. `**kwargs`

`**kwargs` allows a function to accept multiple keyword arguments.

```python
def student(**details):
    print(details)

student(name="Usha", age=20, marks=90)
```

Output:

```text
{'name': 'Usha', 'age': 20, 'marks': 90}
```

`**kwargs` stores the values as a **dictionary**.

### Remember

```text
**kwargs → dictionary
```

---

# 10. Local and Global Variables

## Local Variable

Created inside a function.

```python
def test():
    x = 10
    print(x)

test()
```

`x` is a local variable.

---

## Global Variable

Created outside the function.

```python
a = 10
b = 20

def add():
    print(a + b)

add()
```

`a` and `b` are global variables.

### Simple Rule

```text
Inside function  → Local
Outside function → Global
```

Avoid using too many global variables in large programs.

---

# 11. Lambda Functions

A lambda is a small **one-line function**.

Normal function:

```python
def square(x):
    return x * x
```

Lambda:

```python
square = lambda x: x * x

print(square(5))
```

Output:

```text
25
```

### Another Example

```python
add = lambda a, b: a + b

print(add(10, 20))
```

Output:

```text
30
```

Lambda is useful for small operations, especially with functions like `sorted()`.

---

# 12. Modules

A **module** is a Python file containing reusable code.

For example:

```python
import math

print(math.sqrt(25))
```

Output:

```text
5.0
```

### Import Specific Function

```python
from math import sqrt

print(sqrt(25))
```

### Using an Alias

```python
import math as m

print(m.sqrt(25))
```

Common examples:

```python
import numpy as np
import pandas as pd
```

---

# 13. Creating Your Own Module

Create a file:

```text
calculator.py
```

Inside it:

```python
def add(a, b):
    return a + b
```

Then another Python file can use it:

```python
import calculator

print(calculator.add(10, 20))
```

This helps us create **reusable code**.

---

# ⭐ Quick Revision

| Topic      | Meaning                         |
| ---------- | ------------------------------- |
| Set        | Stores unique values            |
| Dictionary | Stores key-value pairs          |
| `if`       | Makes a decision                |
| `for`      | Repeats through items           |
| `while`    | Repeats while condition is true |
| `break`    | Stops loop                      |
| `continue` | Skips current iteration         |
| `pass`     | Does nothing                    |
| Function   | Reusable block of code          |
| `*args`    | Multiple positional arguments   |
| `**kwargs` | Multiple keyword arguments      |
| Local      | Variable inside function        |
| Global     | Variable outside function       |
| Lambda     | Small one-line function         |
| Module     | Reusable Python file            |

## ⭐ Most Important Things to Remember

```text
Set        → unique values
Dictionary → key : value
for        → iterate
while      → repeat while condition is true
break      → stop
continue   → skip
pass       → do nothing

*args      → tuple
**kwargs   → dictionary

Local      → inside function
Global     → outside function

lambda     → small one-line function
module     → reusable Python file
```
