## Question

What is the output of the following code?

```python
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    print(check_age(-5))
except ValueError as e:
    print(e)
```

## Options

**A.**

```text
-5
```

**B.**

```text
Age cannot be negative
```

**C.**

```text
ValueError
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

The `raise` keyword is used to **manually raise an exception**.

Here:

```python
if age < 0:
    raise ValueError("Age cannot be negative")
```

Since `age` is `-5`, the `ValueError` is raised.

The `except` block catches the exception:

```python
except ValueError as e:
    print(e)
```

The variable `e` contains the error message:

```text
Age cannot be negative
```

Therefore, the output is:

```text
Age cannot be negative
```

