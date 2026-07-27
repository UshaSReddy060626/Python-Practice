## Question

What is the output of the following code?

```python
a = [10, 20, 30]
b = a[:]

b.append(40)

print(a)
print(b)
```

## Options

**A.**

```text
[10, 20, 30, 40]
[10, 20, 30, 40]
```

**B.**

```text
[10, 20, 30]
[10, 20, 30, 40]
```

**C.**

```text
[10, 20, 30]
[10, 20, 30]
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

The statement

```python
b = a[:]
```

creates a **shallow copy** of the list.

Since `a` and `b` are now two different list objects, modifying `b` does not affect `a`.

When `b.append(40)` is executed, only `b` changes.

Output:

```text
[10, 20, 30]
[10, 20, 30, 40]
```