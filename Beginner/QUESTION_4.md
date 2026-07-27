## Question

What is the output of the following code?

```python
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

print(add_item(1))
print(add_item(2))
```

## Options

**A.**

```text
[1]
[2]
```

**B.**

```text
[1]
[1, 2]
```

**C.**

```text
[1, 2]
[1, 2]
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

In Python, default arguments are evaluated **only once**, when the function is defined—not each time it is called.

Here, the default list `my_list=[]` is created only once and reused for every call to the function.

- First call:

```python
add_item(1)
```

Output:

```text
[1]
```

- Second call:

```python
add_item(2)
```

The same list is reused, so `2` is appended to the existing list.

Output:

```text
[1, 2]
```

A safer approach is:

```python
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list
```