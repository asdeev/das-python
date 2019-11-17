"""
    Description: An implementation of the Doubly Linked List.
    Name: doubly_linked_list.py
    Author: Zaid Bhura
"""
from node import Node
from typing import Union


class DoublyLinkedList:

    def __init__(self, head: Node = None, tail: Node = None):
        self.head = head
        self.tail = tail

    # runs in O(1) time
    def insert_head(self, data: Union[int, str]):
        # allocate new_node and put in data
        new_node = Node(data=data)

        # make next of new_node as head and prev as None
        new_node.set_next(new_next=self.head)
        new_node.set_prev(new_prev=None)

        # change prev of head node to new_node
        if self.head is not None:
            self.head.set_prev(new_node)

        # move head to point to new_node
        self.head = new_node

    # runs in O(n) time
    def insert_tail(self, data: Union[int, str]):
        # allocate new_node and put in data
        new_node = Node(data=data)
        last = self.head

        # new_node will be last node so set its next as None
        new_node.set_next(None)

        # make new_node as head if list is empty
        if self.head is None:
            new_node.set_prev(None)
            self.head = new_node
            return

        # traverse till last node
        while last.get_next() is not None:
            last = last.get_next()

        # change next of last node
        last.set_next(new_node)

        # make last node as prev of new_node
        new_node.set_prev(last)

    # runs in O(n) time
    def insert_after(self, prev_node: Node, data: Union[int, str]):
        # check if given prev_node is None
        if prev_node is None:
            raise ValueError('Node not in list')

        # allocate new_node and put in data
        new_node = Node(data=data)

        # make next of new_node as next of prev_node
        new_node.set_next(prev_node.get_next())

        # make prev of new_node as prev_node
        new_node.set_prev(prev_node)

        # make next of prev_node as new_node
        prev_node.set_next(new_node)

        # make prev of next of new_node as new_node
        if new_node.get_next() is not None:
            new_node.get_next().set_prev(new_node)

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
        found = False

        # loop until value deleted or last node reached
        while current is not None and found is False:
            if current.get_data() == data:
                found = True
            else:
                # set current to next node
                current = current.get_next()
        if current is None:
            raise ValueError('Data not in list')
        else:
            # set current previous node to its next node
            current.get_prev().set_next(current.get_next())
            # set current next node to its previous node
            current.get_next().set_prev(current.get_prev())
