## Question

What is the output of the following code?

```python
text = "Python is awesome"

print(text.split())
```

## Options

**A.**

```text
["Python", "is", "awesome"]
```

**B.**

```text
"Python is awesome"
```

**C.**

```text
("Python", "is", "awesome")
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** A

### Explanation

The `split()` method divides a string into a list of substrings.

By default, it splits the string wherever it finds whitespace.

```python
text.split()
```

returns

```text
["Python", "is", "awesome"]
```

