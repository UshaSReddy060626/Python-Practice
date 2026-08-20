## Question

What is the output of the following code?

```python
class Descriptor:
    def __get__(self, instance, owner):
        return "Value accessed"


class Demo:
    value = Descriptor()


print(Demo.value)
```

## Options

**A.**

```text
Value accessed
```

**B.**

```text
Descriptor
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

When a descriptor is accessed through the class:

```python
Demo.value
```

Python calls its `__get__()` method.

In this case:

```python
__get__(self, instance, owner)
```

receives:

- `self` → the descriptor object
- `instance` → `None`, because the access is through the class
- `owner` → `Demo`

The method returns:

```text
Value accessed
```

Therefore:

```text
Value accessed
```

is printed.

