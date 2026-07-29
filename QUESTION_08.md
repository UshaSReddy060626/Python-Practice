## Question

What is the output of the following code?

```python
numbers = [1, 2, 3]

print(numbers.pop())
print(numbers)
```

## Options

**A.**

```text
1
[2, 3]
```

**B.**

```text
3
[1, 2]
```

**C.**

```text
3
[1, 2, 3]
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

The `pop()` method removes and returns the **last element** of the list by default.

Initially:

```python
numbers = [1, 2, 3]
```

After:

```python
numbers.pop()
```

- Returned value: `3`
- Updated list: `[1, 2]`

Therefore, the output is:

```text
3
[1, 2]
```