## Question

What is the output of the following code?

```python
student = {
    "name": "Alice",
    "age": 22
}

print(student.get("city"))
```

## Options

**A.**

```text
city
```

**B.**

```text
None
```

**C.**

```text
KeyError
```

**D.**

```text
{}
```

---

## Answer

**Correct Option:** B

### Explanation

The `get()` method is used to retrieve the value associated with a key in a dictionary.

If the key does not exist, `get()` returns `None` instead of raising an error.

```python
student.get("city")
```

Since `"city"` is not present in the dictionary, the output is:

```text
None
```

