## Question

What is the output of the following code?

```python
import weakref

class Demo:
    pass

obj = Demo()

ref = weakref.ref(obj)

print(ref() is obj)

del obj

print(ref())
```

## Options

**A.**

```text
True
None
```

**B.**

```text
False
None
```

**C.**

```text
True
<Demo object>
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** A

### Explanation

A **weak reference** does not keep an object alive.

This creates a weak reference:

```python
ref = weakref.ref(obj)
```

Initially, `obj` still exists, so:

```python
ref() is obj
```

returns:

```text
True
```

Then:

```python
del obj
```

removes the strong reference to the object.

Since the weak reference does not keep the object alive, the object can be garbage collected.

Calling:

```python
ref()
```

after the object is gone returns:

```text
None
```

Therefore, the output is:

```text
True
None
```

