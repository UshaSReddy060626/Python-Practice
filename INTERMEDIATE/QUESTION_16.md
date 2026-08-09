## Question

What is the output of the following code?

```python
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error")
finally:
    print("Done")
```

## Options

**A.**

```text
5.0
Done
```

**B.**

```text
Done
```

**C.**

```text
Error
Done
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

The `try` block executes successfully:

```python
x = 10 / 2
```

The result is stored in `x`, but it is **not printed**.

Since no `ZeroDivisionError` occurs, the `except` block is skipped.

The `finally` block executes regardless of whether an exception occurs.

Therefore, the output is:

```text
Done
```

