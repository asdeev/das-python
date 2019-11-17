"""
    Description: This is a Node class for lists to use.
    Name: node.py
    Author: Zaid Bhura
"""
from __future__ import annotations


# Node class
class Node(object):

    # initialize the Node object
    def __init__(self, data=None, prev_node=None, next_node=None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    # return the data of a Node instance
    def get_data(self) -> any:
        return self.data

    # return the previous Node pointer of a Node instance
    def get_prev(self) -> Node:
        return self.prev_node

    # return the next Node pointer of a Node instance
    def get_next(self) -> Node:
        return self.next_node

    # set the previous Node pointer of a Node instance
    def set_prev(self, new_prev: Node):
        self.prev_node = new_prev

    # set the next Node pointer of a Node instance
    def set_next(self, new_next: Node):
        self.next_node = new_next
