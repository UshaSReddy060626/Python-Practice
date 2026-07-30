## Question

What is the output of the following code?

```python
text = "Python"

print(text.upper())
print(text)
```

## Options

**A.**

```text
PYTHON
PYTHON
```

**B.**

```text
Python
PYTHON
```

**C.**

```text
PYTHON
Python
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** C

### Explanation

Strings in Python are **immutable**.

The `upper()` method returns a **new string** with all characters converted to uppercase. It does not modify the original string.

```python
text.upper()
```

returns

```text
PYTHON
```

but `text` itself remains unchanged.

Therefore, the output is:

```text
PYTHON
Python
```