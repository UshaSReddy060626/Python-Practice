## Question

What is the output of the following code?

```python
class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")
        super().show()


class C(A):
    def show(self):
        print("C")
        super().show()


class D(B, C):
    pass


obj = D()
obj.show()
```

## Options

**A.**

```text
B
A
```

**B.**

```text
B
C
A
```

**C.**

```text
C
B
A
```

**D.**

```text
A
B
C
```

---

## Answer

**Correct Option:** B

### Explanation

Class `D` inherits from both `B` and `C`:

```python
class D(B, C):
```

Python uses **Method Resolution Order (MRO)** to determine the order in which methods are searched.

The MRO is:

```text
D → B → C → A → object
```

So when:

```python
obj.show()
```

is called:

1. `B.show()` runs → prints `B`
2. `super().show()` moves to `C.show()` → prints `C`
3. `C.show()` calls `super().show()` → moves to `A.show()` → prints `A`

Therefore:

```text
B
C
A
```

