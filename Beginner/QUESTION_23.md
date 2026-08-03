## Question

What is the output of the following code?

```python
x = [1, 2, 3]

print(x[::-1])
```

## Options

**A.**

```text
[3, 2, 1]
```

**B.**

```text
[1, 2, 3]
```

**C.**

```text
[2, 3]
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** A

### Explanation

The slicing syntax is:

```python
sequence[start:end:step]
```

When the step is `-1`, Python traverses the sequence from the end to the beginning.

```python
x[::-1]
```

returns a reversed copy of the list.

Output:

```text
[3, 2, 1]
```

