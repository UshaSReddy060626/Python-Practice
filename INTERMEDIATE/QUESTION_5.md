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
[1, 2, 3, 4, 5]
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

The `filter()` function keeps only the elements for which the function returns `True`.

```python
lambda x: x % 2 == 0
```

checks whether a number is even.

Therefore,

```python
filter(...)
```

returns only:

```text
[2, 4]
```
