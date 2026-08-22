## Question

What is the output of the following code?

```python
Person = type(
    "Person",
    (),
    {"name": "Alice"}
)

person = Person()

print(person.name)
```

## Options

**A.**

```text
Person
```

**B.**

```text
Alice
```

**C.**

```text
None
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

The `type()` function can be used to **dynamically create a class**.

The syntax is:

```python
type(class_name, bases, attributes)
```

Here:

```python
type(
    "Person",
    (),
    {"name": "Alice"}
)
```

creates a class named `Person` with an attribute:

```python
name = "Alice"
```

Then:

```python
person = Person()
```

creates an instance of that class.

Therefore:

```python
person.name
```

returns:

```text
Alice
```

