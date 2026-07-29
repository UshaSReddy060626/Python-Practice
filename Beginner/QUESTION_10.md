## Question

What is the output of the following code?

```python
x = [1, 2, 3]

print(2 in x)
print(5 in x)
```

## Options

**A.**

```text
True
False
```

**B.**

```text
False
True
```

**C.**

```text
True
True
```

**D.**

```text
False
False
```

---

## Answer

**Correct Option:** A

### Explanation

The `in` operator checks whether a value exists in a sequence such as a list, tuple, or string.

For the list:

```python
x = [1, 2, 3]
```

- `2 in x` returns `True` because `2` is present.
- `5 in x` returns `False` because `5` is not present.

Therefore, the output is:

```text
True
False
```