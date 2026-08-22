## Question

What is the output of the following code?

```python
import sys

x = []

y = x

print(sys.getrefcount(x))
```

## Options

**A.**

```text
1
```

**B.**

```text
2
```

**C.**

```text
3
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** C

### Explanation

`sys.getrefcount()` returns the number of references to an object.

Here:

```python
x = []
y = x
```

Both `x` and `y` refer to the same list.

When `x` is passed to:

```python
sys.getrefcount(x)
```

the function call itself creates an additional temporary reference.

So there are typically:

```text
x
y
getrefcount argument
```

which gives:

```text
3
```

