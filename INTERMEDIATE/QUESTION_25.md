## Question

What is the output of the following code?

```python
def add(x, y=10):
    return x + y

print(add(5))
print(add(5, 20))
```

## Options

**A.**

```text
15
25
```

**B.**

```text
5
25
```

**C.**

```text
15
15
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** A

### Explanation

The function has a **default argument**:

```python
def add(x, y=10):
```

If a value for `y` is not provided, Python automatically uses `10`.

So:

```python
add(5)
```

becomes:

```python
5 + 10
```

which gives:

```text
15
```

For:

```python
add(5, 20)
```

the provided value `20` replaces the default value `10`.

So:

```python
5 + 20
```

gives:

```text
25
```

Therefore, the output is:

```text
15
25
```
