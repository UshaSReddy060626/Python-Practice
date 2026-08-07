## Question

What is the output of the following code?

```python
x = 10

def func():
    global x
    x = 20

func()

print(x)
```

## Options

**A.**

```text
10
```

**B.**

```text
20
```

**C.**

```text
30
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

The keyword

```python
global x
```

tells Python to use the global variable instead of creating a local one.

So,

```python
x = 20
```

updates the global variable.

Output:

```text
20
```

