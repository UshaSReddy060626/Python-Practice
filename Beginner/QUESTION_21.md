## Question

What is the output of the following code?

```python
numbers = {1, 2, 2, 3, 3, 4}

print(numbers)
```

## Options

**A.**

```text
{1, 2, 2, 3, 3, 4}
```

**B.**

```text
{1, 2, 3, 4}
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

**Correct Option:** B

### Explanation

A **set** stores only **unique** elements.

When duplicate values are added to a set, they are automatically removed.

```python
numbers = {1, 2, 2, 3, 3, 4}
```

becomes

```text
{1, 2, 3, 4}
```

