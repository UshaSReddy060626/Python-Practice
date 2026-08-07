## Question

What is the output of the following code?

```python
x = 10

def func():
    x = 20
    print(x)

func()
print(x)
```

## Options

**A.**

```text
20
20
```

**B.**

```text
10
10
```

**C.**

```text
20
10
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** C

### Explanation

The variable `x` inside the function is a **local variable**.

```python
x = 20
```

exists only inside `func()`.

The global variable

```python
x = 10
```

remains unchanged.

Output:

```text
20
10
```
