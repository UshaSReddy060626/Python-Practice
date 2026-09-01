# Question 35 - Intermediate

## Question

What is the output of the following code?

```python
a = [1, 2, 3]
b = [4, 5, 6]

result = zip(a, b)

print(list(result))
```

## Options

**A.**

```text
[(1, 4), (2, 5), (3, 6)]
```

**B.**

```text
[[1, 4], [2, 5], [3, 6]]
```

**C.**

```text
[(1, 2, 3), (4, 5, 6)]
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** A

### Explanation

The `zip()` function combines corresponding elements from multiple iterables.

Here:

```python
a = [1, 2, 3]
b = [4, 5, 6]
```

The corresponding elements are paired:

```text
1 → 4
2 → 5
3 → 6
```

So:

```python
list(zip(a, b))
```

produces:

```text
[(1, 4), (2, 5), (3, 6)]
```

Each pair is represented as a tuple.

> **Interview Tip:** `zip()` stops when the shortest iterable is exhausted. It is commonly used when processing multiple sequences element by element.