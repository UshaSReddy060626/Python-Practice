## Question

What is the output of the following code?

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)


a = Number(10)
b = Number(20)

result = a + b

print(result.value)
```

## Options

**A.**

```text
10
```

**B.**

```text
20
```

**C.**

```text
30
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** C

### Explanation

The `__add__()` magic method controls the behavior of the `+` operator for objects.

When Python sees:

```python
a + b
```

it internally calls:

```python
a.__add__(b)
```

The method performs:

```python
self.value + other.value
```

which is:

```python
10 + 20
```

So a new `Number` object containing:

```text
30
```

is returned.

Therefore:

```python
print(result.value)
```

outputs:

```text
30
```

