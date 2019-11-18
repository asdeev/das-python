"""
    Description: An implementation of the Doubly Linked List.

    Title: doubly_linked_list.py

    Author: Zaid Bhura
"""
from node import Node
from typing import Union


class DoublyLinkedList(object):

    def __init__(self, head: Node = None, tail: Node = None):
        """Initialize DoublyLinkedList object."""
        self.head = head
        self.tail = tail

    def insert_head(self, data: Union[int, str]):
        """Insert Node at the beginning of list

        This function will allocate a new Node, change
        the pointer of its next Node to be the current head,
        and set the new Node to be the new head.
        Runs in O(1) time.

        :param
            data: Union[int, str]: The integer or string value to
                insert into the node.

        """

        # allocate new_node and put in data
        new_node = Node(data=data)

        # make next of new_node as head and prev as None
        new_node.set_next(new_next=self.head)
        new_node.set_prev(new_prev=None)

        # change prev of head node to new_node
        if self.head is not None:
            if self.tail is None:
                self.tail = self.head
            self.head.set_prev(new_node)

        # move head to point to new_node
        self.head = new_node

    def insert_tail(self, data: Union[int, str]):
        """Insert Node at the end of list

        This function will allocate a new Node, change
        the pointer of its prev Node to be the current tail,
        and set the new Node to be the new tail.
        Runs in O(1) time.

        :param
            data: Union[int, str]: The integer or string value to
                insert into the node.

        """

        # allocate new_node and put in data
        new_node = Node(data=data)

        # make prev of new_node as tail and next as None
        new_node.set_prev(new_prev=self.tail)
        new_node.set_next(new_next=None)

        # change next of tail node to new_node
        if self.tail is not None:
            if self.head is None:
                self.head = self.tail
            self.tail.set_next(new_node)

        # move tail to point to new_node
        self.tail = new_node

    def search(self, data: Union[int, str]) -> Node:
        """Find a Node with specified data.

        This function will search the list to find and
        return the first Node with the specified data.
        Runs in O(n) time.

        :param
            data: Union[int, str]: The integer or string value to insert
                into a Node.
        :return
            current: Node: The found Node.

        """

        # set current to head
        current = self.head
        found = False

        # loop until value found or last Node reached
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                # set current to next Node
                current = current.get_next()
        if current is None:
            raise ValueError('Data not in list')

        # return found Node
        return current

    def delete(self, data: Union[int, str]) -> Node:
        """Delete a Node with specified data.

        This function will search the list to find and
        delete the first Node with the specified data.
        Runs in O(n) time.

        :param
            data: Union[int, str]: The integer or string value to insert
                into a Node.
        :return
            current: Node: The deleted Node.

        """

        # set current to head
        current = self.head
        previous = None
        found = False

        # loop until value deleted or last Node reached
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                # set previous to current
                previous = current
                # set current to next Node
                current = current.get_next()
        if current is None:
            raise ValueError('Data not in list')
        if previous is None:
            # deleted Node is head Node
            self.head = current.get_next()
        else:
            # set previous Node to next Node of current to delete
            previous.set_next(new_next=current.get_next())

        # return deleted Node
        return current

    def size(self) -> int:
        """Returns the count of total Nodes in list."""
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.get_next()
        return count

    def print(self):
        """Prints out the list from beginning"""
        current = self.head

        while current:
            print(current.get_data())
            current = current.get_next()
