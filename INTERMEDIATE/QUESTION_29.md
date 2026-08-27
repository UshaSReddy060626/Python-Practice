## Question

What is the output of the following code?

```python
def outer():
    x = 10

    def inner():
        nonlocal x
        x += 5
        return x

    return inner

func = outer()

print(func())
print(func())
```

## Options

**A.**

```text
15
15
```

**B.**

```text
10
15
```

**C.**

```text
15
20
```

**D.**

```text
20
25
```

---

## Answer

**Correct Option:** C

### Explanation

The inner function uses:

```python
nonlocal x
```

This allows `inner()` to modify the variable `x` belonging to the enclosing `outer()` function.

Initially:

```python
x = 10
```

First call:

```python
func()
```

increments `x`:

```text
10 + 5 = 15
```

So it returns:

```text
15
```

The updated value of `x` is remembered by the closure.

Second call increments it again:

```text
15 + 5 = 20
```

Therefore:

```text
15
20
```

