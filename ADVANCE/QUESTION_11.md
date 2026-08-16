## Question

What is the output of the following code?

```python
class Demo:
    def __enter__(self):
        print("Start")
        return "Hello"

    def __exit__(self, exc_type, exc_value, traceback):
        print("End")


with Demo() as value:
    print(value)
```

## Options

**A.**

```text
Start
Hello
End
```

**B.**

```text
Hello
Start
End
```

**C.**

```text
Start
End
Hello
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** A

### Explanation

The value returned by `__enter__()` is assigned to the variable after `as`.

Here:

```python
with Demo() as value:
```

calls:

```python
__enter__()
```

which prints:

```text
Start
```

and returns:

```python
"Hello"
```

Therefore:

```python
value
```

contains:

```text
Hello
```

The `print(value)` statement produces:

```text
Hello
```

Finally, when the `with` block finishes, `__exit__()` runs and prints:

```text
End
```

Therefore, the output is:

```text
Start
Hello
End
```

