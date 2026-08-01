## Question

What is the output of the following code?

```python
numbers = [1, 2, 3]

numbers.extend([4, 5])

print(numbers)
```

## Options

**A.**

```text
[1, 2, 3, [4, 5]]
```

**B.**

```text
[1, 2, 3, 4, 5]
```

**C.**

```text
[[1, 2, 3], 4, 5]
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

The `extend()` method adds each element of the iterable to the existing list.

```python
numbers.extend([4, 5])
```

is equivalent to:

```python
numbers.append(4)
numbers.append(5)
```

The updated list becomes:

```text
[1, 2, 3, 4, 5]
```

