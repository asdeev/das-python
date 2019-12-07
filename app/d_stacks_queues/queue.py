"""
    Description: An implementation of the Queue.

    Title: queue.py

    Author: Zaid Bhura
"""
from collections import deque


class Queue(object):

    def __init__(self):
        """Initialize Queue object."""
        self.queue = deque()
        self.size = 0

    def enqueue(self, data: int):
        """Add an item to queue

        This function will add an item to the end of the queue.
        Runs in O(1) time.

        :param
            data: int: The integer to add to the queue

        """
        self.queue.append(data)
        self.size += 1

    def dequeue(self):
        """Remove an item from queue

        This function will remove an item from the beginning of the queue.
        Runs in O(1) time.

        """
        if not self.is_empty():
            self.queue.popleft()
            self.size -= 1
        else:
            raise ValueError('Queue is empty')

    def peek(self):
        """Look at the head value of the queue

        This function will return an item from the beginning of the queue.
        Runs in O(1) time.

        """

        return self.queue[0]

    def get_size(self):
        """Return size of queue"""
        return self.size

    def is_empty(self):
        """Check if queue is empty or not"""
        if self.get_size() == 0:
            return True
        return False
