## Question

What is the output of the following code?

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

## Options

**A.**

```text
0
```

**B.**

```text
10
```

**C.**

```text
Cannot divide by zero
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** C

### Explanation

The expression:

```python
10 / 0
```

causes a `ZeroDivisionError`.

The `except` block catches this specific exception:

```python
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Therefore, instead of the program stopping with an unhandled error, it prints:

```text
Cannot divide by zero
```
