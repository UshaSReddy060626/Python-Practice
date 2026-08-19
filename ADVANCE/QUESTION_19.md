## Question

What is the output of the following code?

```python
class Student:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


s1 = Student("Alice")
s2 = Student("Alice")

students = {s1, s2}

print(len(students))
```

## Options

**A.**

```text
0
```

**B.**

```text
1
```

**C.**

```text
2
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

The class defines both:

```python
__eq__()
```

and:

```python
__hash__()
```

Two objects are considered equal because:

```python
s1.name == s2.name
```

which is:

```text
"Alice" == "Alice"
```

Both objects also have the same hash because:

```python
hash(self.name)
```

is based on the same string.

A set keeps only one object when two objects are equal and have the same hash.

Therefore:

```python
len(students)
```

returns:

```text
1
```

