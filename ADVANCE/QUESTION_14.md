## Question

What is the output of the following code?

```python
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print([cls.__name__ for cls in D.__mro__])
```

## Options

**A.**

```text
['D', 'B', 'C', 'A', 'object']
```

**B.**

```text
['D', 'A', 'B', 'C', 'object']
```

**C.**

```text
['A', 'B', 'C', 'D', 'object']
```

**D.**

```text
['D', 'C', 'B', 'A', 'object']
```

---

## Answer

**Correct Option:** A

### Explanation

`D` inherits from both `B` and `C`:

```python
class D(B, C):
```

Python calculates the **Method Resolution Order (MRO)** using the C3 linearization algorithm.

The resulting order is:

```text
D → B → C → A → object
```

Therefore:

```python
D.__mro__
```

contains:

```text
D
B
C
A
object
```

The list comprehension extracts their class names:

```text
['D', 'B', 'C', 'A', 'object']
```

