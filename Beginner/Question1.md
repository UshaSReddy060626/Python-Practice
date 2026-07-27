## Question

What is the output of the following code?

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
print(b)
```

## Options

**A.**

```text
[1, 2, 3]
[1, 2, 3, 4]
```

**B.**

```text
[1, 2, 3, 4]
[1, 2, 3, 4]
```

**C.**

```text
[1, 2, 3]
[1, 2, 3]
```

**D.**

```
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

`b = a` does not create a new list. Both `a` and `b` point to the same list object in memory. When `b.append(4)` is executed, the original list is modified, so both variables display the updated list.