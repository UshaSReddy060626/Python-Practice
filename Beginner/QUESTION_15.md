## Question

What is the output of the following code?

```python
nums = [5, 2, 8, 1]

nums.sort()

print(nums)
```

## Options

**A.**

```text
[5, 2, 8, 1]
```

**B.**

```text
[8, 5, 2, 1]
```

**C.**

```text
[1, 2, 5, 8]
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** C

### Explanation

The `sort()` method sorts the list **in ascending order** by default.

Original list:

```python
[5, 2, 8, 1]
```

After sorting:

```python
[1, 2, 5, 8]
```

Unlike `sorted()`, the `sort()` method modifies the original list.