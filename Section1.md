# Python

- Python is an interpreted, interactive, object-oriented programming language.
  It incorporates modules, exceptions, dynamic typing, very high level dynamic
  data types, and classes. Python combines remarkable power with very clear
  syntax.
- Python is a high level, general purpose language. It supports different domains,
  like science computation, network services, webs, games, system scripting, ...
- Currently, Python2 and Python3 are the 2 major versions.

```plain
Question
What is CPython?
```

```plain
Question
What is the most significant limitation of CPython?
```

## Interpreter

There are 2 ways to run Python in terminal

- interactive mode / IDLE
- script mode

```plain
Question
What is the difference between interactive mode and script mode?
```

```plain
Question
Usually you could run a Python script (let's call it test.py) in terminal by
$ python test.py

Is there a way to run the script directly, like this
$ ./test.py
```

## Number

Please read the articles below

- https://www.tutorialspoint.com/python/python_numbers.htm
- https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator
- https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
- https://docs.python.org/3/library/stdtypes.html#truth-value-testing

### Integer

```plain
Question
What are the largest and smallest values that can be reliably stored in a variable of type int?
```

```plain
Which value will variable n have?
n = 3 / 2
```

### Float

```plain
Question
What is the differance between / and // in both Python2 and Python3?
```

```plain
Question
What is the biggest and smallest numbers that can be stored in a float variable?
```

### Boolean

- Titled case ``True``, not ``true``

### Operator

Below are the frequently used operators in Python

- #### Arithmetic Operator `+ - * / ** // %`

- #### Logical Operators `and or not`

- #### Comparison Operators `== != > >= < <=`

- #### Assignment Operators `= += -= *= **= /= //= %=`

- #### Bitwise Operators `& | ^ ~ << >>`

- #### Membership Operators `in, not in`

- #### Identity Operators `is, is not`

```plain
Question
What is short-circuit in programming? Does python support short-circuiting?
```

```python
Question
# Explain why
not A == B
# is valid syntax but
A == not B
# is invalid?
```

## Conditional execution

https://docs.python.org/3/tutorial/controlflow.html

- `if else`
- `for`
- `while`

```plain
Question
What is Ternary Operator in Python?
```

```plain
Question
Does Python have `do while` loop?
```

## Data Structure

### List

https://docs.python.org/3/tutorial/introduction.html#lists (section 3.1.3. Lists)

```plain
Question
What is method in Python?
```

```plain
Question
What is the difference between list.append() and list.extend()? Which one should we use?
```

```plain
Question
How to check if a value exists in a list?
```

```plain
Question
What is list comprehension?
```

### String

https://docs.python.org/3/tutorial/introduction.html#strings (section 3.1.2. Strings)

```plain
Question
Distinguish the differences between single quote and double quote and triple quote.
```

```plain
Question
What escaping characters are used in Python?
```

```plain
Question
What is string slicing?
```

```plain
Question
I have "Apple", I want "elppA", how to do it?
```

```python
Question
s = "Python"
# What happen when I want to have "Jython" from s if I try:
s[0] = "J"
# What's wrong, why?
```

### Dictionary

https://docs.python.org/3/tutorial/datastructures.html#dictionaries (section 5.5 Dict)

```plain
Question
What is Dict Comprehension?
```

```plain
Question
Does dictionary maintain input order?
If not how do we keep it?
```

### Tuple

https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences (section 5.3. Tuples and Sequences)

```plain
Question
How to create an empty Tuple?
```

```Python
Question
# Read a snippet below
a = ([1,2],3,4)
a[0][0] = 5
# a = ([5,2],3,4)
# We all know that tuple is immuatable why can we still be able to change its values?
```

```plain
Question
What is unpacking?
Write a code that swap 2 variables' values by using unpacking.
```

### Set

https://docs.python.org/3/tutorial/datastructures.html#sets (section 5.4. Sets)

```plain
What are the different between Set and Dict?
```
