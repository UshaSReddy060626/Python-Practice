## Question

What is the output of the following code?

```python
class Demo:
    pass

print(type(Demo))
```

## Options

**A.**

```text
<class 'object'>
```

**B.**

```text
<class 'type'>
```

**C.**

```text
<class 'Demo'>
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

In Python, classes are themselves objects.

The class:

```python
Demo
```

is an instance of the metaclass:

```python
type
```

Therefore:

```python
type(Demo)
```

returns:

```text
<class 'type'>
```

