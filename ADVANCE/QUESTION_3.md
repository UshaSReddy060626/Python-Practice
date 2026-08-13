## Question

What is the output of the following code?

```python
def generate_numbers():
    for i in range(3):
        yield i

numbers = generate_numbers()

print(next(numbers))
print(next(numbers))
print(next(numbers))
```

## Options

**A.**

```text
0
0
0
```

**B.**

```text
0
1
2
```

**C.**

```text
1
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

The function contains the `yield` keyword, so it becomes a **generator function**.

```python
def generate_numbers():
    for i in range(3):
        yield i
```

Calling:

```python
numbers = generate_numbers()
```

creates a generator object.

Each call to `next()` resumes the generator from where it previously stopped.

First:

```python
next(numbers)
```

returns:

```text
0
```

Second:

```python
next(numbers)
```

resumes from where it stopped and returns:

```text
1
```

Third:

```python
next(numbers)
```

returns:

```text
2
```

Therefore, the output is:

```text
0
1
2
```

