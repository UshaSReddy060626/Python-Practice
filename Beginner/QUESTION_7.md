## Question

What is the output of the following code?

```python
x = [1, 2, 3]

print(x == [1, 2, 3])
print(x is [1, 2, 3])
```

## Options

**A.**

```text
True
True
```

**B.**

```text
True
False
```

**C.**

```text
False
True
```

**D.**

```text
False
False
```

---

## Answer

**Correct Option:** B

### Explanation

The `==` operator compares the **values** of two objects.

```python
x == [1, 2, 3]
```

returns:

```text
True
```

because both lists contain the same elements.

The `is` operator checks whether two variables refer to the **same object in memory**.

```python
x is [1, 2, 3]
```

returns:

```text
False
```

because `[1, 2, 3]` creates a new list object.

Therefore, the output is:

```text
True
False
```