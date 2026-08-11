## Question

What is the output of the following code?

```python
def greet():
    return "Hello"

def execute(func):
    return func()

print(execute(greet))
```

## Options

**A.**

```text
greet
```

**B.**

```text
Hello
```

**C.**

```text
None
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

In Python, functions can be passed as arguments to other functions.

Here:

```python
execute(greet)
```

passes the `greet` function to `execute`.

Inside `execute()`:

```python
return func()
```

calls the function.

Since `greet()` returns:

```text
Hello
```

the final output is:

```text
Hello
```

