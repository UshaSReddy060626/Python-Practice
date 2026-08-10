## Question

What happens when `next()` is called after an iterator has no more elements?

```python
numbers = iter([1])

print(next(numbers))
print(next(numbers))
```

## Options

**A.**

```text
1
None
```

**B.**

```text
1
0
```

**C.**

```text
1
StopIteration
```

**D.**

```text
It returns an empty list.
```

---

## Answer

**Correct Option:** C

### Explanation

The iterator contains only one element:

```python
[1]
```

The first call:

```python
next(numbers)
```

returns:

```text
1
```

There are no more elements remaining.

When `next()` is called again, Python raises the:

```text
StopIteration
```

exception.

Therefore, conceptually the output is:

```text
1
StopIteration
```

