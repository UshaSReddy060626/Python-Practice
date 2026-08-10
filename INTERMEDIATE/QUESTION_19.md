## Question

What is the output of the following code?

```python
numbers = iter([10, 20, 30])

print(next(numbers))
print(next(numbers))
```

## Options

**A.**

```text
10
10
```

**B.**

```text
10
20
```

**C.**

```text
20
30
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

The `iter()` function converts an iterable into an **iterator**.

```python
numbers = iter([10, 20, 30])
```

The `next()` function retrieves the next value from the iterator.

First:

```python
next(numbers)
```

returns:

```text
10
```

The iterator then moves forward.

Second:

```python
next(numbers)
```

returns:

```text
20
```

Therefore, the output is:

```text
10
20
```

