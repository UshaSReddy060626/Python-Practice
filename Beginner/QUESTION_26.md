## Question

What is the output of the following code?

```python
x = (1, 2, 3)
y = x + (4,)

print(y)
```

## Options

**A.**

```text
(1, 2, 3, 4)
```

**B.**

```text
[1, 2, 3, 4]
```

**C.**

```text
(1, 2, 3, (4,))
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** A

### Explanation

Tuples are immutable, but two tuples can be combined using the `+` operator.

```python
x = (1, 2, 3)
```

and:

```python
(4,)
```

are combined to create a new tuple.

Therefore:

```python
x + (4,)
```

produces:

```text
(1, 2, 3, 4)
```

