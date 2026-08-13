## Question

What is the output of the following code?

```python
def outer():
    x = 10

    def inner():
        return x + 5

    return inner

func = outer()

print(func())
```

## Options

**A.**

```text
5
```

**B.**

```text
10
```

**C.**

```text
15
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** C

### Explanation

The function `inner()` uses the variable `x` from the enclosing function `outer()`.

```python
def inner():
    return x + 5
```

Even after `outer()` has finished executing, the returned `inner` function remembers the value of `x`.

This is called a **closure**.

Here:

```python
x = 10
```

so:

```python
x + 5
```

becomes:

```text
15
```

Therefore, the output is:

```text
15
```

