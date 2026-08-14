## Question

What is the output of the following code?

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"


person = Person("Alice")

print(person)
```

## Options

**A.**

```text
Alice
```

**B.**

```text
Person: Alice
```

**C.**

```text
<Person object>
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

The `__str__()` method is a **magic (dunder) method** that defines the human-readable string representation of an object.

When:

```python
print(person)
```

is executed, Python internally uses:

```python
person.__str__()
```

The method returns:

```text
Person: Alice
```

Therefore, the output is:

```text
Person: Alice
```

