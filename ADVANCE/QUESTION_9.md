## Question

What is the output of the following code?

```python
class Account:
    def __init__(self):
        self.__balance = 1000

account = Account()

print(account.__balance)
```

## Options

**A.**

```text
1000
```

**B.**

```text
__balance
```

**C.**

```text
AttributeError
```

**D.**

```text
None
```

---

## Answer

**Correct Option:** C

### Explanation

The double underscore:

```python
self.__balance
```

triggers **name mangling** in Python.

Python internally changes the attribute name to something similar to:

```python
_Account__balance
```

Therefore, directly accessing:

```python
account.__balance
```

does not find the attribute and raises:

```text
AttributeError
```

