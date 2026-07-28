# Question 5 - Medium

## Question

What is the output of the following code?

```python
x = [1, 2, 3]

print(x * 2)
```

## Options

**A.**

```text
[2, 4, 6]
```

**B.**

```text
[1, 2, 3, 1, 2, 3]
```

**C.**

```text
[1, 4, 9]
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

The `*` operator with a list repeats the list.

```python
[1, 2, 3] * 2
```

creates a new list by repeating the original list twice.

Output:

```text
[1, 2, 3, 1, 2, 3]
```

It does **not** multiply each element by `2`.