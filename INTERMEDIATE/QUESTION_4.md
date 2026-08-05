## Question

What is the output of the following code?

```python
def square(x):
    return x * x

numbers = [1, 2, 3]

result = map(square, numbers)

print(list(result))
```

## Options

**A.**

```text
[1, 2, 3]
```

**B.**

```text
[1, 4, 9]
```

**C.**

```text
map object
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

The `map()` function applies a function to every element in an iterable.

```python
result = map(square, numbers)
```

creates a map object.

When converted to a list:

```python
list(result)
```

each element is squared.

Output:

```text
[1, 4, 9]
```
