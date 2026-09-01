# Question 36 - Intermediate

## Question

What is the output of the following code?

```python
numbers = [1, 2, 3, 4, 5]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)
```

## Options

**A.**

```text
[1, 3, 5]
```

**B.**

```text
[2, 4]
```

**C.**

```text
[0, 2, 4]
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

The `filter()` function selects elements from an iterable based on a condition.

Here:

```python
lambda x: x % 2 == 0
```

checks whether each number is even.

From:

```text
1, 2, 3, 4, 5
```

the even numbers are:

```text
2, 4
```

Therefore:

```python
list(filter(lambda x: x % 2 == 0, numbers))
```

produces:

```text
[2, 4]
```

> **Interview Tip:** `filter()` keeps elements for which the given function returns `True`. In Python 3, `filter()` returns an iterator, so `list()` is commonly used to obtain the results as a list.