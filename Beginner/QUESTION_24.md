## Question

What is the output of the following code?

```python
x = [1, 2, 3]

print(x.append(4))
```

## Options

**A.**

```text
[1, 2, 3, 4]
```

**B.**

```text
None
```

**C.**

```text
4
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

The `append()` method modifies the original list **in place** and returns `None`.

After execution,

```python
x
```

becomes

```text
[1, 2, 3, 4]
```

However,

```python
print(x.append(4))
```

prints the return value of `append()`, which is:

```text
None
```

