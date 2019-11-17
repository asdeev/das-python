"""
    Description: An implementation of the Singly Linked List.
    Name: singly_linked_list.py
    Author: Zaid Bhura
"""
from node import Node


class SinglyLinkedList(object):

    def __init__(self, head=None):
        self.head = head

    # runs in O(1) time
    def insert(self, data: any):
        new_node = Node(data=data)
        new_node.set_next(new_next=self.head)
        self.head = new_node

    # runs in O(n) time
    def size(self) -> int:
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    # runs in O(n) time
    def search(self, data) -> Node:
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError('Data not in list')
        return current

    # runs in O(n) time
    def delete(self, data: any):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError('Data not in list')
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(new_next=current.get_next())
