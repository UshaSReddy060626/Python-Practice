## Question

What is the output of the following code?

```python
data = {"a": 1, "b": 2}

data["c"] = 3

print(len(data))
```
## Options

**A.**

```text
2
```

**B.**

```text
3
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

The dictionary initially contains two key-value pairs:

```python
{"a": 1, "b": 2}
```

Then:

```python
data["c"] = 3
```

adds a new key-value pair.

The dictionary becomes:

```python
{"a": 1, "b": 2, "c": 3}
```

Therefore:

```python
len(data)
```

returns:

```text
3
```

