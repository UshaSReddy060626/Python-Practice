## Question

What is the output of the following code?

```python
x = (1, 2, 3)

x[0] = 100

print(x)
```

## Options

**A.**

```text
(100, 2, 3)
```

**B.**

```text
(1, 2, 3)
```

**C.**

```text
TypeError
```

**D.**

```text
IndexError
```

---

## Answer

**Correct Option:** C

### Explanation

Tuples are **immutable**, meaning their elements cannot be changed after creation.

The statement

```python
x[0] = 100
```

tries to modify the first element of the tuple, which is not allowed.

Python raises a:

```text
TypeError
```

because tuple item assignment is not supported.