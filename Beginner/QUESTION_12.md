## Question

What is the output of the following code?

```python
numbers = [10, 20, 30]

numbers.insert(1, 15)

print(numbers)
```

## Options

**A.**

```text
[15, 10, 20, 30]
```

**B.**

```text
[10, 15, 20, 30]
```

**C.**

```text
[10, 20, 15, 30]
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

The `insert(index, value)` method inserts an element at the specified index.

```python
numbers.insert(1, 15)
```

places `15` at index `1`.

Original list:

```python
[10, 20, 30]
```

Updated list:

```python
[10, 15, 20, 30]
```