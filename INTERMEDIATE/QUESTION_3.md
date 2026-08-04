## Question

What is the output of the following code?

```python
a = "Python"

b = a.replace("P", "J")

print(a)
print(b)
```

## Options

**A.**

```text
Jython
Jython
```

**B.**

```text
Python
Jython
```

**C.**

```text
Python
Python
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

Strings are **immutable** in Python.

The `replace()` method returns a **new string** instead of modifying the original one.

```python
a = "Python"
b = a.replace("P", "J")
```

The variable `a` remains unchanged.

Output:

```text
Python
Jython
```

