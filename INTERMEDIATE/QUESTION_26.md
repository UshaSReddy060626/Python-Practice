## Question

What is the output of the following code?

```python
x = [1, 2, 3]
result = [i * 2 for i in x if i % 2 != 0]

print(result)
```

## Options

**A.**

```text
[2, 4, 6]
```

**B.**

```text
[1, 3]
```

**C.**

```text
[2, 6]
```

**D.**

```text
[1, 2, 3]
```

---

## Answer

**Correct Option:** C

### Explanation

The list comprehension:

```python
[i * 2 for i in x if i % 2 != 0]
```

first checks whether each number is odd.

From:

```text
1, 2, 3
```

the odd numbers are:

```text
1, 3
```

Each of them is multiplied by `2`:

```text
1 * 2 = 2
3 * 2 = 6
```

Therefore:

```text
[2, 6]
```

