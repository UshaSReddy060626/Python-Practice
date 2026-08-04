## Question

What is the output of the following code?

```python
def func(a=[]):
    a.append(1)
    return a

print(func())
print(func())
```

## Options

**A.**

```text
[1]
[1]
```

**B.**

```text
[1]
[1, 1]
```

**C.**

```text
[1, 1]
[1, 1]
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

Default arguments are evaluated only once when the function is defined.

The same list is reused every time the function is called.

First call:

```text
[1]
```

Second call:

```text
[1, 1]
```

A better implementation is:

```python
def func(a=None):
    if a is None:
        a = []
    a.append(1)
    return a
```

