## Question

What is the output of the following code?

```python
names = ["Alice", "Bob", "Charlie"]

for index, name in enumerate(names):
    print(index, name)
```

## Options

**A.**

```text
Alice
Bob
Charlie
```

**B.**

```text
0 Alice
1 Bob
2 Charlie
```

**C.**

```text
1 Alice
2 Bob
3 Charlie
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

The `enumerate()` function returns both the index and the value while iterating.

```python
enumerate(names)
```

produces:

```python
(0, "Alice")
(1, "Bob")
(2, "Charlie")
```

Therefore, the loop prints:

```text
0 Alice
1 Bob
2 Charlie
```

