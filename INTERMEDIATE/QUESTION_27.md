## Question

What is the output of the following code?

```python
def calculate(a, b):
    return a + b, a * b

result = calculate(3, 4)

print(result)
print(type(result))
```

## Options

**A.**

```text
7
<class 'int'>
```

**B.**

```text
(7, 12)
<class 'tuple'>
```

**C.**

```text
[7, 12]
<class 'list'>
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

The function returns two values:

```python
return a + b, a * b
```

Python automatically packs multiple returned values into a tuple.

For:

```python
calculate(3, 4)
```

the values are:

```text
3 + 4 = 7
3 * 4 = 12
```

Therefore:

```python
result
```

contains:

```text
(7, 12)
```

and its type is:

```text
<class 'tuple'>
```

