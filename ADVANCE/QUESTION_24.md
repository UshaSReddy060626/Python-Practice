## Question

What is the output of the following code?

```python
class Descriptor:
    def __get__(self, instance, owner):
        return instance._value

    def __set__(self, instance, value):
        instance._value = value * 2


class Demo:
    value = Descriptor()


obj = Demo()

obj.value = 10

print(obj.value)
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
100
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

The descriptor defines both:

```python
__get__()
```

and:

```python
__set__()
```

When this statement runs:

```python
obj.value = 10
```

Python calls:

```python
__set__(obj, 10)
```

Inside `__set__()`:

```python
instance._value = value * 2
```

So:

```python
obj._value = 20
```

Later:

```python
print(obj.value)
```

calls:

```python
__get__()
```

which returns:

```python
instance._value
```

Therefore, the output is:

```text
20
```

