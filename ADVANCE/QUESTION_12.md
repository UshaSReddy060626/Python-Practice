## Question

What is the output of the following code?

```python
class Demo:
    def __enter__(self):
        print("Enter")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exit")
        return True


with Demo():
    print("Inside")
    raise ValueError("Something went wrong")

print("Done")
```

## Options

**A.**

```text
Enter
Inside
Exit
Done
```

**B.**

```text
Enter
Inside
ValueError
```

**C.**

```text
Enter
Exit
Done
```

**D.**

```text
It raises an error before printing Exit.
```

---

## Answer

**Correct Option:** A

### Explanation

The `with` statement first calls:

```python
__enter__()
```

so:

```text
Enter
```

is printed.

Then the block executes:

```python
print("Inside")
```

so:

```text
Inside
```

is printed.

Next:

```python
raise ValueError("Something went wrong")
```

raises an exception.

However, before the exception leaves the `with` block, Python calls:

```python
__exit__()
```

So:

```text
Exit
```

is printed.

The important part is:

```python
return True
```

inside `__exit__()`.

Returning `True` tells Python that the exception has been **handled**, so it does not propagate further.

Therefore, execution continues with:

```python
print("Done")
```

Output:

```text
Enter
Inside
Exit
Done
```

