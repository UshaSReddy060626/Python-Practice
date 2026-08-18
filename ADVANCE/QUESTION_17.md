## Question

What is the output of the following code?

```python
class Team:
    def __init__(self, players):
        self.players = players

    def __len__(self):
        return len(self.players)


team = Team(["Alice", "Bob", "Charlie"])

print(len(team))
```

## Options

**A.**

```text
0
```

**B.**

```text
3
```

**C.**

```text
["Alice", "Bob", "Charlie"]
```

**D.**

```text
It raises an error.
```

---

## Answer

**Correct Option:** B

### Explanation

The `__len__()` magic method defines what happens when `len()` is called on an object.

Here:

```python
def __len__(self):
    return len(self.players)
```

The team contains three players:

```python
["Alice", "Bob", "Charlie"]
```

Therefore:

```python
len(team)
```

internally calls:

```python
team.__len__()
```

which returns:

```text
3
```

