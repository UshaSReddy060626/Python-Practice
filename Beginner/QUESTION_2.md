## Question

What is the output of the following code?

```python
name = "Python"

print(name[-1])
```

## Options

**A.**

```text
P
```

**B.**

```text
n
```

**C.**

```text
o
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

Negative indexing starts from the end of a string. The index `-1` always refers to the last character.

```
P  y  t  h  o  n
0  1  2  3  4  5
              -1
```

Therefore,

```python
print(name[-1])
```

prints

```text
n
```