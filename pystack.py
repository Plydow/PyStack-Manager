"""
Package to add the stack management in python

Package to add class, methode to manage stack in python

Class:
    Stack

Functions:
    push(value)
    pop() -> value
    last() -> calue
    get_size() -> int
    copy() -> Stack
    transfer(stack)
    is_limited() -> boolean
    is_typed() -> boolean
    is_full() -> boolean
    get_capacity() -> int

Raises:
    EmptyStackError
    StackOverflowError
    EmptyStackError
    NotStackError
"""


class StackError(Exception):
    """Set of stack module errors"""


class StackOverflowError(StackError):
    """Raised when trying to add an extra element to an already full stack"""


class StackTypedError(StackError):
    """Raised when trying to add a different type element in a typed stack"""


class EmptyStackError(StackError):
    """Raised when trying to access of last element in empty stack"""


class NotStackError(StackError):
    """Raised when trying to do a stack action on a no stack element"""


class Stack:
    """
    Class for stack management in python

    Class to create and use stack in python

    Args:
        limite (int): limite of element in stack, set to -1 for unlimited stack

    Raises:
        ValueError: limite or typed argument not match with int and type
    """

    def __init__(self, limite=-1, typed=()):
        if not isinstance(limite, (int, float)):
            raise ValueError("limite argument must be a int")

        self.__stack = []
        self.LIMITE = limite
        self.TYPED = typed

    def push(self, value):
        """
        Add element at the end of the stack

        Add element at the end of the stack by checking the specific
        requirements of the stack (size, type)

        Args:
            value (all): element to add to the stack

        Raises:
            StackOverflowError: the stack has already full (limite option validated)
            StackTypedError: value type doesn't match with stack element type (typed stack)

        """
        if self.is_limited() and len(self.__stack) >= self.get_capacity():
            raise StackOverflowError(
                "the stack is already full (limited option validated)"
            )
        if self.is_typed() and not isinstance(value, self.get_type()):
            raise StackTypedError("the stack are typed and argument doesn't this type")

        self.__stack.append(value)

    def pop(self):
        """
        Return and remove the last element in the stack

        Return and remove the last element in the stack

        Returns:
            all: the last element of stack

        Raises:
            EmptyStackError: raised if the stack is empty
        """
        if len(self.__stack) == 0:
            raise EmptyStackError("the stack are empty")

        return self.__stack.pop()

    def last(self):
        """
        Return the last element in the stack

        Return without removing the last value from the stack

        Returns:
            all: the last element in the stack

        Raises:
            EmptyStackError: raised if the stack is empty
        """

        if len(self.__stack) == 0:
            raise EmptyStackError("The stack is empty")

        return self.__stack[-1]

    def get_size(self):
        """
        Return the size of the stack

        Return the size of the stack (not the limite size)

        Returns:
            int: number of stack element
        """
        return len(self.__stack)

    def copy(self):
        """
        Create new stack with the same option and value

        Create new stack with the same limite, type and value

        Returns:
            Stack: copy of the stack
        """
        stack_copy = Stack(limite=self.get_capacity(), typed=self.get_type())

        for element in self.__stack:
            stack_copy.push(element)

        return stack_copy

    def transfer(self, stack_origin):
        """
        Transfers element of stack_origin to the stack_object (instance of class)

        Transfers element included in the stack put in argument in this stack
        object keeping order. If the stack_origin are empty or stack_object are
        full, errors will not be returned.
        This function also allows to add the elements of a list to the stack in
        the order of the list.

        Args:
            stack_origin (Stack): Stack with new element

        Raises:
            NotStackError: stack_origin isn't a Stack Object
            TypedStackError: one element of stack_origin doesn't match with stack type
        """
        if not isinstance(stack_origin, (Stack, list, tuple)):
            raise NotStackError("The argument is not a stack, list or tuple")

        if isinstance(stack_origin, Stack):
            stack_origin_copy = stack_origin.copy()
            stack_size = stack_origin_copy.get_size()

            temp_list = [stack_origin_copy.pop() for _ in range(0, stack_size)]
        else:
            temp_list = stack_origin[::-1]

        for element in temp_list[::-1]:
            try:
                self.push(element)
            except StackOverflowError:
                pass
            except Exception as error:
                raise error

    def reverse(self):
        """
        Reverse the stack.
        """
        self.__stack = self.__stack[::-1]

    def split(self, index):
        """
        Split the stack in two stacks around the value of index.

        Split the stack in two stacks, the first part (0->index), index excluded,
        rest in this stack, and the rest goes in a new stack.

        Args:
            index (int): value of split

        Returns:
            new_stack (Stack): the stack container values between index and the end

        Raise:
            ValueError: if index is not a int or float and not between 0 and stack size
        """
        if isinstance(index, (int, float)) and 0 <= index <= self.get_size():
            raise ValueError(
                "Value of split must be a integer or float and be between 0 and the stack size"
            )

        new_stack = Stack(limite=self.get_capacity(), typed=self.get_type())
        new_stack.transfer(self.__stack[:index])
        self.__stack = self.__stack[index:]

        return new_stack

    def is_limited(self):
        """
        Return if the stack is at limited capacity

        Returns:
            boolean: state of limited option
        """
        if self.get_capacity() == -1:
            return False
        return True

    def is_typed(self):
        """
        Return if the stack is of fixed type

        Returns:
            boolean: state of fixed type option
        """
        if self.TYPED == ():
            return False
        return True

    def get_capacity(self):
        """
        Return the value of limited capacity option

        Returns:
            int: value of limited capacity option
        """
        return self.LIMITE

    def is_full(self):
        """
        Return if the stack is full

        Returns:
            boolean: if the stack is full
        """
        if self.is_limited():
            if self.get_size() == self.get_capacity():
                return True
        return False

    def get_type(self):
        """
        Return if the stack is typed

        Returns:
            boolean: state of typed option
        """
        return self.TYPED

    def __str__(self):
        return str(self.__stack)

    def __add__(self, other):
        if not isinstance(other, Stack):
            raise NotStackError("The addition element is not a stack")
        self_copy = self.copy()
        self_copy.transfer(other)
        return self_copy

    def __repr__(self):
        message = "Stack Object"
        if self.is_limited():
            message += f" limited ({self.get_capacity()} elements max)"
        if self.is_typed():
            message += f" typed ({self.get_type()})"
        message += f" contain {self.get_size()} elements"
        return message

    def __contains__(self, value):
        return value in self.__stack

    def __iadd__(self, other):
        return self.__add__(other)

    def __radd__(self, other):
        return self.__add__(other)

    def __eq__(self, other):
        other = other.copy()
        other_size = other.get_size()
        other_element = [other.pop() for _ in range(0, other_size)][::-1]

        if other_element == self.__stack:
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)
