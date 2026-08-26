## Question

What is the output of the following code?

```python
numbers = [1, 2, 3]

result = map(lambda x: x ** 2, numbers)

print(list(result))
```

## Options

**A.**

```text
[1, 2, 3]
```

**B.**

```text
[2, 4, 6]
```

**C.**

```text
[1, 4, 9]
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** C

### Explanation

The `map()` function applies a function to every element of an iterable.

Here:

```python
lambda x: x ** 2
```

calculates the square of each number.

Therefore:

```text
1² = 1
2² = 4
3² = 9
```

The `map()` object is converted into a list using:

```python
list(result)
```

So the output is:

```text
[1, 4, 9]
```

