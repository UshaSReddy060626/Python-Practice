## Question

What is the output of the following code?

```python
x = [1, 2]
y = x.copy()

y.append(3)

print(x)
print(y)
```

## Options

**A.**

```text
[1, 2, 3]
[1, 2, 3]
```

**B.**

```text
[1, 2]
[1, 2, 3]
```

**C.**

```text
[1, 2]
[1, 2]
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

The `copy()` method creates a **shallow copy** of the list.

```python
y = x.copy()
```

Now `x` and `y` are two different list objects.

Appending `3` to `y` does not affect `x`.

Output:

```text
[1, 2]
[1, 2, 3]
```