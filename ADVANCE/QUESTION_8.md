## Question

What is the output of the following code?

```python
class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

student = Student(90)

print(student.marks)
```

## Options

**A.**

```text
_marks
```

**B.**

```text
90
```

**C.**

```text
@property
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

The `@property` decorator allows a method to be accessed like an attribute.

Normally, we would call:

```python
student.marks()
```

But because `marks` is defined using:

```python
@property
```

we can access it as:

```python
student.marks
```

The property method returns:

```python
self._marks
```

which is:

```text
90
```

Therefore, the output is:

```text
90
```

