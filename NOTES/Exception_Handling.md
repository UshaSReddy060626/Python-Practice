# Exception Handling & File I/O

### Topics Covered

* Exception Handling
* `try`
* `except`
* `finally`
* Common exceptions
* File Handling
* Reading files
* Writing files
* Appending to files
* CSV files
* JSON files

---

# 1. Exception Handling

Sometimes a Python program can produce an error while running.

For example:

```python
a = 10
b = 0

print(a / b)
```

This produces:

```text
ZeroDivisionError
```

Instead of allowing the program to crash, we can handle the error using `try-except`.

---

# 2. `try-except`

Basic structure:

```python
try:
    # code that may cause an error
except:
    # code to handle the error
```

Example:

```python
try:
    a = 10
    b = 0
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")
```

Output:

```text
Cannot divide by zero
```

### Simple Rule

```text
try   → Try to run the code
except → Handle the error
```

---

# 3. Common Exceptions

## ValueError

Occurs when the value is not valid for the operation.

```python
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Please enter a valid number")
```

If the user enters:

```text
hello
```

`ValueError` occurs.

---

## ZeroDivisionError

Occurs when dividing by zero.

```python
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

## TypeError

Occurs when an operation is performed on incompatible types.

```python
try:
    result = "10" + 5

except TypeError:
    print("Invalid data types")
```

---

## IndexError

Occurs when accessing an invalid list index.

```python
numbers = [10, 20, 30]

try:
    print(numbers[10])

except IndexError:
    print("Invalid index")
```

---

## KeyError

Occurs when accessing a dictionary key that doesn't exist.

```python
student = {
    "name": "Rahul"
}

try:
    print(student["marks"])

except KeyError:
    print("Key does not exist")
```

---

## FileNotFoundError

Occurs when trying to open a file that doesn't exist.

```python
try:
    file = open("students.txt", "r")

except FileNotFoundError:
    print("File does not exist")
```

---

# 4. Multiple `except`

A program can have multiple possible errors.

```python
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(a / b)

except ValueError:
    print("Please enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

# 5. `finally`

`finally` runs whether an error occurs or not.

```python
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid number")

finally:
    print("Program finished")
```

### Remember

```text
try     → Try the code
except  → Handle the error
finally → Always runs
```

---

# 6. File Handling

Python can work with files to:

* Create files
* Read files
* Write files
* Add new data

The main function is:

```python
open()
```

---

# 7. File Modes

| Mode  | Meaning |
| ----- | ------- |
| `"r"` | Read    |
| `"w"` | Write   |
| `"a"` | Append  |

### `"r"` → Read

Used to read existing file contents.

### `"w"` → Write

Used to write data into a file.

If the file doesn't exist, Python creates it.

⚠️ If the file already contains data, `"w"` can overwrite it.

### `"a"` → Append

Adds new data to the end of the file without removing existing data.

---

# 8. Writing to a File

```python
with open("students.txt", "w") as file:
    file.write("Rahul\n")
    file.write("85\n")
```

The file will contain:

```text
Rahul
85
```

### Why use `with`?

`with open()` automatically closes the file after the work is finished.

---

# 9. Reading a File

```python
with open("students.txt", "r") as file:
    content = file.read()

print(content)
```

---

# 10. Reading Line by Line

```python
with open("students.txt", "r") as file:

    for line in file:
        print(line)
```

This is useful when the file contains many lines.

---

# 11. Appending to a File

```python
with open("students.txt", "a") as file:
    file.write("Rahul\n")
```

If the file already contains:

```text
Usha
85
```

After appending:

```text
Usha
85
Rahul
```

---

# 12. CSV Files

CSV means:

**Comma-Separated Values**

Example:

```text
Name,Marks
Rahul,85
Usha,90
```

CSV files are commonly used for storing tabular data.

---

## Reading CSV

```python
import csv

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)
```

---

## Writing CSV

```python
import csv

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Marks"])
    writer.writerow(["Rahul", 85])
```

---

# 13. JSON

JSON stands for:

**JavaScript Object Notation**

It is commonly used for storing and exchanging structured data.

Example JSON:

```json
{
    "name": "Rahul",
    "marks": 85
}
```

Python can work with JSON using the `json` module.

```python
import json
```

---

# 14. Python → JSON File

Use `json.dump()`.

```python
import json

student = {
    "name": "Rahul",
    "marks": 85
}

with open("student.json", "w") as file:
    json.dump(student, file)
```

---

# 15. JSON File → Python

Use `json.load()`.

```python
import json

with open("student.json", "r") as file:
    student = json.load(file)

print(student)
```

Output:

```text
{'name': 'Rahul', 'marks': 85}
```

---

# 16. Exception Handling + File Handling

We can combine both concepts.

```python
try:

    with open("students.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("The file does not exist.")
```

This prevents the program from crashing if the file is missing.

---

# 17. Example Program

### Student File Program

```python
def save_student(name, marks):

    with open("students.txt", "w") as file:
        file.write("Student Name: " + name + "\n")
        file.write("Student Marks: " + str(marks) + "\n")


try:

    student_name = input("Enter the student name: ")
    student_marks = float(input("Enter the student marks: "))

    save_student(student_name, student_marks)

    with open("students.txt", "r") as file:
        content = file.read()

    print("\nStudent Information:")
    print(content)

except ValueError:
    print("Please enter the marks correctly.")

except FileNotFoundError:
    print("File does not exist.")
```

---

# 🧠 Quick Revision

| Concept             | Meaning                      |
| ------------------- | ---------------------------- |
| `try`               | Code that may cause an error |
| `except`            | Handles the error            |
| `finally`           | Always executes              |
| `ValueError`        | Invalid value                |
| `TypeError`         | Wrong data type              |
| `IndexError`        | Invalid list index           |
| `KeyError`          | Missing dictionary key       |
| `FileNotFoundError` | File doesn't exist           |
| `open()`            | Opens a file                 |
| `"r"`               | Read                         |
| `"w"`               | Write                        |
| `"a"`               | Append                       |
| `.read()`           | Read file content            |
| `.write()`          | Write to file                |
| `csv`               | Work with CSV files          |
| `json`              | Work with JSON data          |
| `json.dump()`       | Python → JSON                |
| `json.load()`       | JSON → Python                |

---

