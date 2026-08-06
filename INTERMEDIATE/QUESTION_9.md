## Question

What is the output of the following code?

```python
def display(**details):
    print(details["name"])

display(name="Alice", age=22)
```

## Options

**A.**

```text
Alice
```

**B.**

```text
{'name': 'Alice', 'age': 22}
```

**C.**

```text
22
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** A

### Explanation

The `**kwargs` syntax allows a function to accept any number of keyword arguments.

When the function is called:

```python
display(name="Alice", age=22)
```

the parameter

```python
details
```

becomes

```python
{
    "name": "Alice",
    "age": 22
}
```

Therefore,

```python
details["name"]
```

returns

```text
Alice
```