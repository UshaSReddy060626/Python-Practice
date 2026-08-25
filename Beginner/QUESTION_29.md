## Question

What is the output of the following code?

```python
x = [1, 2, 3, 4]

print(3 in x)
print(5 not in x)
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

**Correct Option:** A

### Explanation

The `in` operator checks whether an element exists in a sequence.

Since `3` exists in:

```python
[1, 2, 3, 4]
```

this:

```python
3 in x
```

returns:

```text
True
```

The `not in` operator checks whether an element does **not** exist.

Since `5` is not present:

```python
5 not in x
```

returns:

```text
True
```

Therefore:

```text
True
True
```

