## Question

What is the output of the following code?

```python
x = [[1, 2], [3, 4]]

y = x.copy()

y[0].append(5)

print(x)
print(y)
```

## Options

**A.**

```text
[[1, 2], [3, 4]]
[[1, 2, 5], [3, 4]]
```

**B.**

```text
[[1, 2, 5], [3, 4]]
[[1, 2, 5], [3, 4]]
```

**C.**

```text
[[1, 2], [3, 4]]
[[1, 2], [3, 4]]
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

The `copy()` method creates a **shallow copy** of the outer list.

Both `x` and `y` still share the same inner lists.

So,

```python
y[0].append(5)
```

modifies the shared inner list.

Output:

```text
[[1, 2, 5], [3, 4]]
[[1, 2, 5], [3, 4]]
```

