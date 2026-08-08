## Question

What is the output of the following code?

```python
numbers = [1, 2, 3, 4, 5]

result = [x * 2 for x in numbers if x % 2 == 0]

print(result)
```

## Options

**A.**

```text
[2, 4, 6, 8, 10]
```

**B.**

```text
[2, 4]
```

**C.**

```text
[1, 3, 5]
```

**D.**

```text
[4, 8]
```

---

## Answer

**Correct Option:** B

### Explanation

This is a **list comprehension** with a condition.

```python
[x * 2 for x in numbers if x % 2 == 0]
```

First, the condition selects only the even numbers:

```text
2, 4
```

Then each selected number is multiplied by `2`:

```text
2 × 2 = 4
4 × 2 = 8
```

Wait — this means the actual output is:

```text
[4, 8]
```

Therefore, the correct answer is **D**.

