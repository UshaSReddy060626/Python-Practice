## Question

What is the output of the following code?

```python
class Student:
    def __repr__(self):
        return "Student Object"

student = Student()

print(student)
```

## Options

**A.**

```text
Student Object
```

**B.**

```text
<Student Object>
```

**C.**

```text
Student
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** A

### Explanation

The `__repr__()` method defines the **official or developer-oriented representation** of an object.

When:

```python
print(student)
```

is executed, Python uses the object's string representation. Since `__repr__()` is defined and `__str__()` is not, the representation returned by `__repr__()` is displayed.

Therefore, the output is:

```text
Student Object
```

