"""
    Description: An implementation of the Stack.

    Title: stack.py

    Author: Zaid Bhura
"""
from collections import deque


class Stack(object):

    def __init__(self):
        """Initialize Stack object."""
        self.stack = deque()
        self.size = 0

    def push(self, data: int):
        """Push an item onto the stack

        This function will add an item to the top of the stack.
        Runs in O(1) time.

        :param
            data: int: The integer to add to the stack

        """
        self.stack.append(data)
        self.size += 1

    def pop(self):
        """Pop an item off the stack

        This function will remove an item from the top of the stack.
        Runs in O(1) time.

        """
        if not self.is_empty():
            self.stack.pop()
            self.size -= 1
        else:
            raise ValueError('Stack is empty')

    def peek(self):
        """Look at the head value of the stack

        This function will return an item from the top of the stack.
        Runs in O(1) time.

        """

        return self.stack[0]

    def get_size(self):
        """Return size of stack"""
        return self.size

    def is_empty(self):
        """Check if stack empty or not"""
        if self.get_size() == 0:
            return True
        return False
