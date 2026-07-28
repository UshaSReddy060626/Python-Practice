## Question

What is the output of the following code?

```python
x = "Python"

print(x[1:4])
```

## Options

**A.**

```text
Pyt
```

**B.**

```text
yth
```

**C.**

```text
tho
```

**D.**

```text
Python
```

---

## Answer

**Correct Option:** B

### Explanation

String slicing follows the syntax:

```python
string[start:end]
```

- The `start` index is included.
- The `end` index is excluded.

For the string `"Python"`:

```
P  y  t  h  o  n
0  1  2  3  4  5
```

`x[1:4]` returns the characters at indices `1`, `2`, and `3`.

Output:

```text
yth
```