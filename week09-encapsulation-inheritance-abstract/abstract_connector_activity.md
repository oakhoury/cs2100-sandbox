# Activity: Make `Connector` abstract

**Time:** about 30 minutes. **Work in pairs.**

**Goal:** Change `Connector` so that a connector that forgets to implement `load()` is caught as soon as it is created, not later inside the pipeline.

You will only edit **one file**: `connectors/base.py`.

> Run every command from the **project root** (the folder that contains `connectors/` and `data/`).

---

## Step 1. See the problem

Run these two commands:

```
python -m demos.inheritance_demo
pytest
```

Look at **part 3** of the demo. The `ForgetfulConnector` class never overrides `load()`.

1. At what point does the error appear: when the object is **created**, or when `load()` is **called**?
2. Where in the code is the error raised?

Your answers:

- 1. ______________________________________________
- 2. ______________________________________________

---

## Step 2. Predict

Before you change anything, write down your answer in your own words:

> If `Connector` were abstract, **when** would `ForgetfulConnector` fail, and what **kind of error** would you expect?

Your prediction: ______________________________________________

---

## Step 3. Make `Connector` abstract 

Open `connectors/base.py` and make changes to the definition of `Connector` to define it as an abstract class. In doing so, this will address the fact that `ForgetfulConnector` never overrides `load()`. The only changes you need are done in `base.py`

---

## Step 4. Check your work

Run both commands again:

```
python -m demos.inheritance_demo
pytest
```

1. What does step 3 in the demo say now? **When** does the error appear?
2. Do the three tests still pass? Why do `SpotifyConnector` and `NetflixConnector` still work without any changes?

Your answers:

1. ______________________________________________
2. ______________________________________________

---

## Step 5. Experiments 

Open a Python session (or a scratch file) in the project root and try each of these. **Predict first, then run.**

```python
from pathlib import Path
from connectors.base import Connector

# (a) Can you create a plain Connector?
Connector(Path("data"))

# (b) A subclass that implements nothing
class HalfDone(Connector):
    pass

HalfDone(Path("data"))

# (c) A subclass that implements load() but returns the wrong kind of thing
class Weird(Connector):
    def load(self):
        return "hello"

Weird(Path("data")).load()
```

Questions:

1. What happens in (a) and (b)? What does the error message say?
2. Does (c) work? What does that tell you about what Python checks, and what it does **not** check?
3. `FitTrackConnector` and `QuietSpotifyConnector` did not need to change. Why not?

---

## Step 6. Reflect

Be ready to share your answers with the class:

1. Wednesday's version failed *late*, and this one fails *early*. Why is early better in a real pipeline?
2. Which promises can an abstract class enforce (for example, that `load` exists), and which can it not (for example, that `load` returns the right data)? What could check the second kind?
3. In Java you would write `abstract class Connector` or `interface Connector`. When would Java report the error: while **compiling**, or while **running**?

---

## Extension (if you finish early)

1. Write a docstring for `load()` that lists, in your own words, **three promises** every connector should keep (for example: what time zone the times are in, or what unit `seconds` uses).
2. If you have `mypy` installed, put `c = Connector(Path("data"))` in a new file and run `mypy` on it. Does it catch the problem **before** you run the code?
