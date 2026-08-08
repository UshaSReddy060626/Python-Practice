## Question

What is the output of the following code?

```python
numbers = [1, 2, 3]

squares = {x: x ** 2 for x in numbers}

print(squares)
```

## Options

**A.**

```text
{1, 2, 3}
```

**B.**

```text
{1: 1, 2: 4, 3: 9}
```

**C.**

```text
[1, 4, 9]
```

**D.**

```text
{1: 2, 2: 4, 3: 6}
```

---

## Answer

**Correct Option:** B

### Explanation

This is a **dictionary comprehension**.

```python
{x: x ** 2 for x in numbers}
```

creates a dictionary where:

- The number becomes the **key**.
- The square of the number becomes the **value**.

Therefore:

```text
1 → 1
2 → 4
3 → 9
```

The output is:

```text
{1: 1, 2: 4, 3: 9}
```

