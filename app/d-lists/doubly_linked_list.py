"""
    Description: An implementation of the Doubly Linked List.
    Name: doubly_linked_list.py
    Author: Zaid Bhura
"""
from node import Node


class DoublyLinkedList:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    # runs in O(n) time
    def insert_head(self, data):
        new_node = Node(data=data)
        new_node.set_next(new_next=self.head)
        new_node.set_prev(new_prev=None)

        if self.head is not None:
            self.head.set_prev(new_node)

        self.head = new_node

    # runs in O(n) time
    def insert_tail(self, data):
        new_node = Node(data=data)
        

    def insert_after(self, prev_node, data):
        if prev_node is None:
            raise ValueError('Node not in list')

        new_node = Node(data=data)
        new_node.set_next(prev_node.get_next())
        new_node.set_prev(prev_node)

        prev_node.set_next(new_node)

        if new_node.get_next() is not None:
            new_node.get_next().set_prev(new_node)