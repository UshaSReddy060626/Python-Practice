## Question

What is the output of the following code?

```python
class Product:
    def __init__(self, price):
        self.price = price

    def __lt__(self, other):
        return self.price < other.price


p1 = Product(100)
p2 = Product(200)

print(p1 < p2)
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
100
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** A

### Explanation

The `__lt__()` magic method defines the behavior of the `<` operator.

When Python evaluates:

```python
p1 < p2
```

it internally calls:

```python
p1.__lt__(p2)
```

The method compares:

```python
self.price < other.price
```

which becomes:

```python
100 < 200
```

This is `True`.

Therefore, the output is:

```text
True
```

