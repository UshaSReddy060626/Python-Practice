## Question

What is the output of the following code?

```python
class Parent:
    def __init__(self):
        self.value = 10


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.value += 5


obj = Child()

print(obj.value)
```

## Options

**A.**

```text
5
```

**B.**

```text
10
```

**C.**

```text
15
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** C

### Explanation

The `Child` class overrides the parent's `__init__()` method.

Inside it:

```python
super().__init__()
```

calls the parent's constructor:

```python
def __init__(self):
    self.value = 10
```

So initially:

```python
self.value = 10
```

Then the child executes:

```python
self.value += 5
```

which becomes:

```python
10 + 5
```

Therefore:

```text
15
```

is printed.

