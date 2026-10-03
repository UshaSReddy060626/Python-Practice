# Python Fundamentals

## 1. Syntax

Syntax is the set of rules that defines how Python programs must be written so that the interpreter can understand and execute them.

---

## 2. Indentation

Indentation in Python is the whitespace used to define blocks of code.

Unlike languages that commonly use braces `{}`, Python uses indentation to represent code blocks.

```python
if age >= 18:
    print("You are eligible")
```

---

## 3. Comments

A comment is non-executable text used to explain or document code.

In Python, a single-line comment starts with `#`.

```python
# This is a comment
print("Hello")
```

---

# Variables

A variable is a name used to reference an object or value in memory.

Python variables are **dynamically typed**, meaning their type is determined at runtime and a variable can refer to objects of different types at different times.

```python
x = 10
x = "Hello"
```

## Variable Naming Rules

A variable:

- Can contain letters
- Can contain numbers
- Can contain `_`
- Cannot start with a number
- Cannot contain spaces
- Cannot use Python keywords

### Examples

```python
name = "Usha"
age2 = 20
student_name = "Usha"
```

Invalid examples:

```python
2age = 20
student name = "Usha"
```

---

# Data Types

A data type tells us **what kind of value an object represents**.

| Data Type | Example |
|---|---|
| `int` | `10` |
| `float` | `10.5` |
| `complex` | `2 + 3j` |
| `str` | `"Hello"` |
| `bool` | `True` |
| `list` | `[1, 2, 3]` |
| `tuple` | `(1, 2, 3)` |
| `set` | `{1, 2, 3}` |
| `dict` | `{"name": "Usha"}` |
| `NoneType` | `None` |

---

# Type Casting

Type casting means **converting a value from one data type to another**.

## Common Conversions

- String → Integer
- Integer → Float
- Integer → String
- String → Float

### Examples

```python
x = int("10")
y = float(10)
z = str(10)
a = float("10.5")
```

Common type conversion functions include:

- `int()`
- `float()`
- `str()`
- `bool()`

---

# Operators

Operators perform operations on values.

## Arithmetic Operators

Arithmetic operators are used to perform mathematical operations.

| Operator | Meaning | Example |
|---|---|---|
| `+` | Addition | `10 + 5` |
| `-` | Subtraction | `10 - 5` |
| `*` | Multiplication | `10 * 5` |
| `/` | Division | `10 / 5` |
| `//` | Floor Division | `10 // 3` |
| `%` | Modulus | `10 % 3` |
| `**` | Exponentiation | `10 ** 2` |

---

## Comparison Operators

Comparison operators compare two values and return a Boolean result.

| Operator | Meaning |
|---|---|
| `==` | Equal |
| `!=` | Not equal |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

Example:

```python
x = 10
y = 5

print(x > y)
print(x == y)
```

---

## Logical Operators

### `and`

Both conditions must be true.

```python
age = 20
has_id = True

print(age >= 18 and has_id)
```

### `or`

At least one condition must be true.

```python
age = 20
has_permission = False

print(age >= 18 or has_permission)
```

### `not`

Reverses the Boolean result.

```python
is_logged_in = True

print(not is_logged_in)
```

---

## Assignment Operators

Assignment operators are used to assign and update values.

```python
x += 5
x -= 5
x *= 5
x /= 5
x //= 5
x %= 5
x **= 2
```

---

## Membership Operators

Membership operators are used to check whether something exists inside a sequence or container.

The main membership operators are:

- `in`
- `not in`

They are commonly used with strings and lists.

```python
name = "Python"

print("P" in name)
print("z" not in name)
```

```python
numbers = [1, 2, 3, 4]

print(3 in numbers)
```

---

## Identity Operators

Identity operators check whether two references point to the **same object**, not simply whether their values are equal.

The identity operators are:

- `is`
- `is not`

### Important Difference

```text
==  → compares values
is  → checks object identity
```

---

# Input

`input()` reads user input from the standard input and always returns the entered value as a string unless explicitly converted.

```python
name = input("Enter your name: ")
print(name)
```

For numerical input:

```python
age = int(input("Enter your age: "))
```

---

# f-Strings

An f-string is a formatted string literal that allows expressions to be embedded inside a string using `{}`.

```python
name = "Usha"
age = 20

print(f"My name is {name} and I am {age} years old.")
```

---

# Strings

A string is a sequence of characters.

Python indexing starts at `0`.

```python
text = "Python"

print(text[0])
print(text[1])
```

Output:

```text
P
y
```

## String Slicing

The syntax for string slicing is:

```text
string[start:stop:step]
```

The `stop` index is excluded.

Example:

```python
text = "Python"

print(text[0:3])
```

Output:

```text
Pyt
```

---

# String Methods

## `lower()`

Converts a string to lowercase.

```python
text = "HELLO"
print(text.lower())
```

## `upper()`

Converts a string to uppercase.

```python
text = "hello"
print(text.upper())
```

## `strip()`

Removes leading and trailing whitespace.

```python
text = "  Hello  "
print(text.strip())
```

## `replace()`

Replaces one part of a string with another.

```python
text = "I like Java"
print(text.replace("Java", "Python"))
```

## `split()`

Converts a string into a list.

```python
text = "Python is easy"
words = text.split()

print(words)
```

## `join()`

Combines strings.

```python
words = ["Python", "is", "easy"]

sentence = " ".join(words)

print(sentence)
```

## `len()`

Returns the number of elements or characters.

```python
text = "Python"

print(len(text))
```

---

# String Immutability

You cannot directly change an individual character in a string.

The following produces an error:

```python
text = "Python"
text[0] = "J"
```

Strings in Python are **immutable sequences**, meaning their individual characters cannot be modified after the string object has been created.

Operations that appear to modify a string actually create a new string.

```python
text = "Python"
text = "J" + text[1:]

print(text)
```

---

# Lists

A list stores multiple values.

Lists can contain different types of values.

```python
items = [10, "Python", 3.5, True]
```

Lists are:

- Ordered
- Mutable
- Allow duplicates
- Able to contain different data types

---

# List Indexing

Lists use indexing to access individual elements.

```python
numbers = [10, 20, 30, 40]

print(numbers[0])
print(numbers[2])
```

---

# Changing a List

Unlike strings, lists are **mutable**.

Individual elements can be changed.

```python
numbers = [10, 20, 30]

numbers[0] = 100

print(numbers)
```

---

# List Methods

## `append()`

Adds one item at the end.

```python
numbers = [1, 2, 3]

numbers.append(4)

print(numbers)
```

## `insert()`

Adds an item at a specific position.

```python
numbers = [1, 2, 3]

numbers.insert(1, 10)

print(numbers)
```

## `remove()`

Removes a value.

```python
numbers = [1, 2, 3]

numbers.remove(2)

print(numbers)
```

## `pop()`

Removes and returns an element.

It removes the last element by default.

```python
numbers = [1, 2, 3]

value = numbers.pop()

print(value)
print(numbers)
```

## `sort()`

Sorts the elements of a list.

```python
numbers = [3, 1, 2]

numbers.sort()

print(numbers)
```

## `reverse()`

Reverses the order of elements.

```python
numbers = [1, 2, 3]

numbers.reverse()

print(numbers)
```

## `count()`

Counts how many times a value appears.

```python
numbers = [1, 2, 2, 3]

print(numbers.count(2))
```

## `index()`

Returns the index of the first occurrence of a value.

```python
numbers = [10, 20, 30]

print(numbers.index(20))
```

---

# List Slicing

List slicing works similarly to string slicing.

```text
list[start:stop:step]
```

Example:

```python
numbers = [1, 2, 3, 4, 5]

print(numbers[1:4])
```

Output:

```text
[2, 3, 4]
```

---

# Tuples

A tuple is similar to a list but is **immutable**.

```python
numbers = (1, 2, 3)
```

A tuple is an **ordered, immutable sequence** in Python.

Once created, its elements cannot be modified, added, or removed.

---

# List vs Tuple

| Feature | List | Tuple |
|---|---|---|
| Syntax | `[]` | `()` |
| Ordered | Yes | Yes |
| Mutable | Yes | No |
| Duplicates | Yes | Yes |
| Indexing | Yes | Yes |
| Slicing | Yes | Yes |

## Why Use Tuples?

Tuples are useful when data should not change.

Example:

```python
coordinates = (10, 20)
```

---

# Slicing

Slicing is used to extract a portion of a sequence.

The syntax is:

```text
sequence[start:stop:step]
```

The `stop` index is excluded.

This concept applies to:

- Strings
- Lists
- Tuples

Examples:

```python
text = "Python"
print(text[0:3])
```

```python
numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])
```

```python
numbers = (1, 2, 3, 4, 5)
print(numbers[1:4])
```

---

# Comprehensions

A list comprehension is a concise way of creating a list by applying an expression to each element of an iterable, optionally using a condition to filter elements.

## Syntax

```python
[expression for item in iterable]
```

Example:

```python
numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)
```

With a condition:

```python
numbers = [1, 2, 3, 4, 5]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)
```

---

# Packing

Packing means putting multiple values into one variable.

```python
numbers = 1, 2, 3

print(numbers)
```

The values are packed into a tuple.

---

# Unpacking

Unpacking means taking values out of an iterable and assigning them to multiple variables.

```python
numbers = (1, 2, 3)

first, second, third = numbers

print(first)
print(second)
print(third)
```

---

# Extended Unpacking

Extended unpacking allows `*` to collect multiple remaining values.

```python
numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers

print(first)
print(middle)
print(last)
```

Output:

```text
1
[2, 3, 4]
5
```

---

# Summary

## Syntax & Indentation

Python syntax defines the rules for writing valid Python programs. Python uses indentation to define blocks of code instead of relying primarily on curly braces.

## Variables

A variable is a name that references an object in Python. Python is dynamically typed, so variable types are determined at runtime.

## Data Types

Python provides built-in data types such as integers, floating-point numbers, strings, booleans, lists, tuples, sets, dictionaries, and `NoneType`.

## Type Casting

Type casting is the conversion of a value from one data type to another using functions such as `int()`, `float()`, `str()`, and `bool()`.

## Operators

Operators are symbols or keywords used to perform operations on values. Python provides arithmetic, comparison, logical, assignment, identity, and membership operators, among others.

## Input

`input()` reads user input from the standard input and always returns the entered value as a string unless explicitly converted.

## Strings

A string is an ordered, immutable sequence of Unicode characters.

## Lists

A list is an ordered, mutable collection that can contain duplicate elements and values of different types.

## Tuples

A tuple is an ordered, immutable sequence that can contain multiple elements.

## Slicing

Slicing is used to extract a portion of a sequence using the syntax:

```text
sequence[start:stop:step]
```

The `stop` index is exclusive.

## List Comprehension

A list comprehension provides a concise way to create a list by applying an expression to elements of an iterable, optionally with a filtering condition.

## Packing

Packing combines multiple values into a single tuple or collection.

## Unpacking

Unpacking assigns the individual elements of an iterable to multiple variables.
