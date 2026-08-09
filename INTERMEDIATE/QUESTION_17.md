## Question

What is the output of the following code?

```python
try:
    number = int("hello")
except ValueError:
    print("Invalid number")
except TypeError:
    print("Wrong type")
```

## Options

**A.**

```text
Invalid number
```

**B.**

```text
Wrong type
```

**C.**

```text
hello
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** A

### Explanation

The `int()` function attempts to convert the string `"hello"` into an integer:

```python
int("hello")
```

This cannot be converted to an integer, so Python raises a:

```text
ValueError
```

The first `except` block handles it:

```python
except ValueError:
    print("Invalid number")
```

Therefore, the output is:

```text
Invalid number
```

The `TypeError` block is not executed because the exception is a `ValueError`.
