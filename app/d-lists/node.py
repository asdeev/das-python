"""
    Description: This is a Node class for lists to use.
    Name: node.py
    Author: Zaid Bhura
"""
from __future__ import annotations
from typing import Union


# Node class
class Node(object):

    # initialize the Node object
    def __init__(self, data: Union[int, str] = None,
                 prev_node: Node = None,
                 next_node: Node = None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    # return the data of a Node instance
    def get_data(self) -> Union[int, str]:
        return self.data

    # return the previous Node pointer of a Node instance
    def get_prev(self) -> Node:
        return self.prev_node

    # return the next Node pointer of a Node instance
    def get_next(self) -> Node:
        return self.next_node

    # set the previous Node pointer of a Node instance
    def set_prev(self, new_prev: Union[Node, None]):
        self.prev_node = new_prev

    # set the next Node pointer of a Node instance
    def set_next(self, new_next: Union[Node, None]):
        self.next_node = new_next
