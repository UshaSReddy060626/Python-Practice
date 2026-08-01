## Question

What is the output of the following code?

```python
a = [1, 2]
b = [3, 4]

print(a + b)
```

## Options

**A.**

```text
[4, 6]
```

**B.**

```text
[[1, 2], [3, 4]]
```

**C.**

```text
[1, 2, 3, 4]
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** C

### Explanation

The `+` operator concatenates lists.

```python
a + b
```

creates a **new list** containing all elements of both lists.

Output:

```text
[1, 2, 3, 4]
```

The original lists remain unchanged.
