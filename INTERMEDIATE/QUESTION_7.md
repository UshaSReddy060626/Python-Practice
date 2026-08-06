## Question

What is the output of the following code?

```python
names = ["Alice", "Bob", "Charlie"]
marks = [85, 90, 95]

result = list(zip(names, marks))

print(result)
```

## Options

**A.**

```text
[("Alice", 85), ("Bob", 90), ("Charlie", 95)]
```

**B.**

```text
["Alice", 85, "Bob", 90, "Charlie", 95]
```

**C.**

```text
{"Alice":85, "Bob":90, "Charlie":95}
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** A

### Explanation

The `zip()` function combines multiple iterables element by element.

```python
zip(names, marks)
```

creates an iterator of tuples.

Converting it to a list gives:

```text
[("Alice", 85), ("Bob", 90), ("Charlie", 95)]
```