## Question

What is the output of the following code?

```python
x = [1, 2, 3]
y = x

print(x is y)
print(x == y)
```

## Options

**A.**

```text
True
True
```

**B.**

```text
True
False
```

**C.**

```text
False
True
```

**D.**

```text
False
False
```

---

## Answer

**Correct Option:** A

### Explanation

The statement

```python
y = x
```

does not create a new list. Instead, both `x` and `y` refer to the same list object in memory.

- `is` checks whether both variables refer to the same object.
- `==` checks whether the values are equal.

Since both variables point to the same list, both expressions return `True`.

Output:

```text
True
True
```