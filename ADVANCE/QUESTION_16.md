## Question

What is the output of the following code?

```python
class Student:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


s1 = Student("Alice")
s2 = Student("Alice")

print(s1 == s2)
```

## Options

**A.**

```text
True
```

**B.**

```text
False
```

**C.**

```text
None
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** A

### Explanation

Normally, two separate objects are different objects even if their attributes contain the same values.

Here:

```python
s1 = Student("Alice")
s2 = Student("Alice")
```

creates two different objects.

However, the class defines:

```python
def __eq__(self, other):
    return self.name == other.name
```

The `__eq__()` magic method controls how the `==` operator behaves for these objects.

So:

```python
s1 == s2
```

becomes:

```python
s1.name == s2.name
```

which is:

```text
"Alice" == "Alice"
```

Therefore:

```text
True
```

