## Question

What is the output of the following code?

```python
class Meta(type):
    def __new__(cls, name, bases, attrs):
        print("Creating class")
        return super().__new__(cls, name, bases, attrs)


class Demo(metaclass=Meta):
    pass


print("Done")
```

## Options

**A.**

```text
Done
Creating class
```

**B.**

```text
Creating class
Done
```

**C.**

```text
Done
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

`Meta` is a **metaclass** because it inherits from:

```python
type
```

When Python creates the class:

```python
class Demo(metaclass=Meta):
```

it uses `Meta` to construct `Demo`.

The `__new__()` method executes during class creation:

```python
print("Creating class")
```

So this is printed first.

Only after the `Demo` class has been created does Python continue to:

```python
print("Done")
```

Therefore, the output is:

```text
Creating class
Done
```

