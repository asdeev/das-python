"""
    Description: This is a Node class for lists to use.

    Title: node.py

    Author: Zaid Bhura
"""
from __future__ import annotations
from typing import Union


class Node(object):

    def __init__(self, data: Union[int, str] = None,
                 prev_node: Node = None,
                 next_node: Node = None):
        """Initialize Node object."""
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    def get_data(self) -> Union[int, str]:
        """Return the data of a Node instance."""
        return self.data

    def get_prev(self) -> Node:
        """Return the previous Node pointer of a Node instance."""
        return self.prev_node

    def get_next(self) -> Node:
        """ Return the next Node pointer of a Node instance."""
        return self.next_node

    def set_prev(self, new_prev: Union[Node, None]):
        """Set the previous Node pointer of a Node instance."""
        self.prev_node = new_prev

    def set_next(self, new_next: Union[Node, None]):
        """Set the next Node pointer of a Node instance."""
        self.next_node = new_next
