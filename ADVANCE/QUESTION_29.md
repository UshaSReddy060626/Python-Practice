## Question

What is the output of the following code?

```python
import gc

class Demo:
    pass

obj = Demo()

del obj

print(gc.isenabled())
```

## Options

**A.**

```text
True
```

**B.**

```text
False
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

**Correct Option:** A

### Explanation

Python's garbage collector is normally **enabled by default**.

The `gc` module provides functions for interacting with Python's cyclic garbage collector.

Therefore:

```python
gc.isenabled()
```

returns:

```text
True
```

The statement:

```python
del obj
```

removes the variable reference to the object. If no references remain, the object can become eligible for cleanup.

