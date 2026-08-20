## Question

What is the output of the following code?

```python
class Descriptor:
    def __get__(self, instance, owner):
        return 100


class Demo:
    value = Descriptor()


obj = Demo()

print(obj.value)
```

## Options

**A.**

```text
Descriptor
```

**B.**

```text
100
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

`Descriptor` defines the special method:

```python
__get__()
```

This allows it to control what happens when the attribute is accessed.

Here:

```python
value = Descriptor()
```

means `value` is a descriptor attached to the `Demo` class.

When:

```python
obj.value
```

is accessed, Python calls:

```python
Descriptor.__get__()
```

which returns:

```text
100
```

Therefore, the output is:

```text
100
```

