## Question

What is the output of the following code?

```python
def add(*numbers):
    return sum(numbers)

print(add(10, 20, 30))
```

## Options

**A.**

```text
30
```

**B.**

```text
60
```

**C.**

```text
(10, 20, 30)
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

The `*args` syntax allows a function to accept any number of positional arguments.

```python
def add(*numbers):
```

stores all positional arguments in a tuple.

```python
numbers
```

becomes

```python
(10, 20, 30)
```

The `sum()` function returns:

```text
60
```