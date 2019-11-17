"""
    Description: An implementation of the Singly Linked List.
    Name: singly_linked_list.py
    Author: Zaid Bhura
"""
from node import Node
from typing import Union


class SinglyLinkedList(object):

    def __init__(self, head: Node = None):
        self.head = head

    # runs in O(1) time
    def insert(self, data: Union[int, str]):
        # allocate new_node and put in data
        new_node = Node(data=data)

        # make next of new_node as head
        new_node.set_next(new_next=self.head)

        # move head to point to new_node
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
    def search(self, data: Union[int, str]) -> Node:
        # set current to head
        current = self.head
        found = False

        # loop until value found or last node reached
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                # set current to next node
                current = current.get_next()
        if current is None:
            raise ValueError('Data not in list')

        # return found node
        return current

    # runs in O(n) time
    def delete(self, data: Union[int, str]):
        # set current to head
        current = self.head
        previous = None
        found = False

        # loop until value deleted or last node reached
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                # set previous to current node
                previous = current
                # set current to next node
                current = current.get_next()
        if current is None:
            raise ValueError('Data not in list')
        if previous is None:
            # deleted node is head node
            self.head = current.get_next()
        else:
            # set previous node to next node of current to delete
            previous.set_next(new_next=current.get_next())
