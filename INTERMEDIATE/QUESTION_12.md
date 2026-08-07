## Question

What is the output of the following code?

```python
square = lambda x: x * x

print(square(5))
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
25
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** C

### Explanation

A `lambda` function is an anonymous function.

```python
square = lambda x: x * x
```

is equivalent to

```python
def square(x):
    return x * x
```

Calling

```python
square(5)
```

returns

```text
25
```

