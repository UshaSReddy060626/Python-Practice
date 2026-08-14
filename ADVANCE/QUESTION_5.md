## Question

What is the output of the following code?

```python
class A:
    def show(self):
        print("A")


class B(A):
    pass


class C(B):
    def show(self):
        print("C")


obj = C()

print(C.__mro__)
```

Which class does Python search first when `obj.show()` is called?

## Options

**A.**

```text
A
```

**B.**

```text
B
```

**C.**

```text
C
```

**D.**

```text
Object
```

---

## Answer

**Correct Option:** C

### Explanation

`MRO` stands for **Method Resolution Order**.

It defines the order in which Python searches for a method or attribute in an inheritance hierarchy.

Here:

```text
C → B → A → object
```

Since `C` defines its own `show()` method, Python finds it first in class `C`.

Therefore, the correct answer is:

```text
C
```

