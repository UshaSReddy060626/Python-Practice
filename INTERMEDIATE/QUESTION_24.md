## Question

What is the output of the following code?

```python
def multiply(x):
    def inner(y):
        return x * y
    return inner

double = multiply(2)

print(double(5))
```

## Options

**A.**

```text
7
```

**B.**

```text
10
```

**C.**

```text
25
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

The function `multiply()` returns another function:

```python
return inner
```

When:

```python
double = multiply(2)
```

the value `2` is remembered by the inner function.

Then:

```python
double(5)
```

is equivalent to:

```python
2 * 5
```

which gives:

```text
10
```

This behavior is called a **closure**.

