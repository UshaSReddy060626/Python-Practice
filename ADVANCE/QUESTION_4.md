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


obj = B()
obj.show()
```

## Options

**A.**

```text
A
B
```

**B.**

```text
B
A
```

**C.**

```text
B
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

`B` overrides the `show()` method inherited from `A`.

When:

```python
obj.show()
```

is called, Python first executes the `show()` method inside class `B`.

So:

```python
print("B")
```

prints:

```text
B
```

Then:

```python
super().show()
```

calls the `show()` method of the parent class `A`.

Therefore:

```text
B
A
```

