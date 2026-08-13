## Question

What is the output of the following code?

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result

    return wrapper


@decorator
def add(a, b):
    return a + b


print(add(2, 3))
```

## Options

**A.**

```text
5
Before
After
```

**B.**

```text
Before
After
5
```

**C.**

```text
Before
5
After
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** C

### Explanation

The `@decorator` syntax replaces the original `add` function with the `wrapper` function.

When:

```python
add(2, 3)
```

is called, the `wrapper()` function executes.

First:

```python
print("Before")
```

prints:

```text
Before
```

Then:

```python
result = func(*args, **kwargs)
```

calls the original `add()` function:

```python
add(2, 3)
```

which returns:

```text
5
```

However, `5` is not printed immediately. It is stored in:

```python
result
```

Then:

```python
print("After")
```

prints:

```text
After
```

Finally:

```python
return result
```

returns `5` to:

```python
print(add(2, 3))
```

which prints:

```text
5
```

Therefore, the output is:

```text
Before
After
5
```

