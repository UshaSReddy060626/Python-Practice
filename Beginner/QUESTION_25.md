## Question

What is the output of the following code?

```python
x = [1, 2, 3]

y = x

x = [4, 5, 6]

print(y)
```

## Options

**A.**

```text
[4, 5, 6]
```

**B.**

```text
[1, 2, 3]
```

**C.**

```text
[]
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

Initially,

```python
y = x
```

makes both variables refer to the same list.

Later,

```python
x = [4, 5, 6]
```

does **not modify** the original list.

Instead, it makes `x` refer to a **new list object**.

The variable `y` still points to the original list.

Therefore,

```python
print(y)
```

outputs:

```text
[1, 2, 3]
```

