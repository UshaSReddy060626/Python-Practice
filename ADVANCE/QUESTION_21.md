## Question

What is the output of the following code?

```python
class Student:
    def __init__(self, name):
        self.name = name


student = Student("Alice")

data = {
    student: "Python"
}

print(data[student])
```

## Options

**A.**

```text
Alice
```

**B.**

```text
Python
```

**C.**

```text
Student
```

**D.**

```text
It raises a TypeError.
```

---

## Answer

**Correct Option:** B

### Explanation

Python objects can be used as dictionary keys when they are **hashable**.

The `Student` class does not define a custom `__eq__()` method, so instances use the default object identity-based equality and hashing behavior.

Therefore:

```python
student
```

can be used as a dictionary key.

The dictionary stores:

```python
student: "Python"
```

So:

```python
data[student]
```

returns:

```text
Python
```

Therefore, the output is:

```text
Python
```

