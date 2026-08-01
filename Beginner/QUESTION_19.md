## Question

What is the output of the following code?

```python
x = [10, 20, 30, 40]

print(x[-2])
```

## Options

**A.**

```text
20
```

**B.**

```text
30
```

**C.**

```text
40
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

Negative indexing starts counting from the end of the list.

```
Index:      0   1   2   3
Value:     10  20  30  40

Negative: -4  -3  -2  -1
```

Therefore,

```python
x[-2]
```

returns:

```text
30
```