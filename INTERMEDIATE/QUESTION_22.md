## Question

What is the output of the following code?

```python
def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@decorator
def greet():
    print("Hello")

greet()
```

## Options

**A.**

```text
Hello
Before
After
```

**B.**

```text
Before
Hello
After
```

**C.**

```text
Before
After
Hello
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

The `@decorator` syntax applies the `decorator` function to `greet`.

So:

```python
greet()
```

actually calls the `wrapper()` function.

Inside `wrapper()`:

1. `"Before"` is printed.
2. `func()` calls the original `greet()` function, printing `"Hello"`.
3. `"After"` is printed.

Therefore, the output is:

```text
Before
Hello
After
```

