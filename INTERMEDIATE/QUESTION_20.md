## Question

What is the output of the following code?

```python
def numbers():
    yield 1
    yield 2
    yield 3

result = numbers()

print(next(result))
print(next(result))
```

## Options

**A.**

```text
1
1
```

**B.**

```text
1
2
```

**C.**

```text
2
3
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

A function containing the `yield` keyword is a **generator function**.

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

Calling:

```python
result = numbers()
```

does not execute the entire function immediately. It creates a generator object.

The first:

```python
next(result)
```

returns `1`.

The generator pauses at that point.

The second:

```python
next(result)
```

resumes execution and returns `2`.

Therefore, the output is:

```text
1
2
```
