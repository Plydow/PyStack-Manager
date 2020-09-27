# PyStack

PyStack is a Python library for use stack.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PyStack.

```bash
pip install pystack-manager
```

## Use

#### Basic example

```python
from pystack import Stack

stack = Stack() #create new stack
stack.add(5) #add element in stack
print(stack.get()) #return and delete last element in stack
print(stack.last()) #return and don't delete last element in stack
```
#### Particular stack

###### Limited stack

The package allows to create a stack of fixed size.

```python
from pystack import Stack

limited_stack = Stack(limite=5) #create new stack with fixed size
```

If we try to add more than the fixed size of the stack, an error is generated

###### Typed stack

The package allows to create a stack of stack with one element type.

```python
from pystack import Stack

typed_stack = Stack(typed=int) #create stack accepting only integer
typed_stack_2 = Stack(typed=(int, float)) #create stack accepting only integer or float
```

If we try to add an element with a type not corresponding to the type of the stack,
an error is generated.

###### In general

You can create stack with or without any of the previous options.

#### Stack modification

###### Add element

Several methods exist to add element to a stack.

Add one element:

```python
stack.add(value) # add items to a stack
```
*value* can a stack, an object, an integer, a float or other.

Add items from one stack to another:

```python
stack.transfer(another_stack) # add items from another_stack to a stack
```
*another_stack* can a stack, a list or a tuple.

Another solution:

```python
stack = first_stack + second_stack #create new stack with elements of first_stack and second_stack
```
*stack* have same option (fixed size, typed) as *first_stack*

###### Get element

Two methods exist to get the last element of the stack.

```python
value = stack.get() #return and delete the last element of the stack
value = stack.last() #return and doesn't delete the last element of the stack
```
If *stack* is empty, an error is generated.

###### Comparison

Different technique can be applied to study a stack.

Equality:
```python
if first_stack == second_stack:
    #True statement
else:
    #False statement
```
If *first_stack* elements are identical to those of the second, equality is respected (options are not necessarily the same).

Contains:
```python
if value in stack: # True if value in the stack
    #True statement
else:
    #False statement
```

## Support

if you encounter any bugs, you can report them by email, by attaching the error message and the program.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
