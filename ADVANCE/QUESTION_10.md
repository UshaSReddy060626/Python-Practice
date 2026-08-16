## Question

What is the output of the following code?

```python
class Demo:
    def __enter__(self):
        print("Enter")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exit")


with Demo():
    print("Inside")
```

## Options

**A.**

```text
Inside
Enter
Exit
```

**B.**

```text
Enter
Inside
Exit
```

**C.**

```text
Enter
Exit
Inside
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

The `with` statement creates a **context manager**.

When execution enters the `with` block, Python automatically calls:

```python
__enter__()
```

So:

```text
Enter
```

is printed first.

Then the code inside the block runs:

```python
print("Inside")
```

giving:

```text
Inside
```

When the `with` block finishes, Python automatically calls:

```python
__exit__()
```

which prints:

```text
Exit
```

Therefore, the output is:

```text
Enter
Inside
Exit
```

