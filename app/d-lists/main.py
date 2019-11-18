#! /usr/local/bin/python3
"""
    Description: The main app to test out the Linked Lists.

    Title: main.py

    Author: Zaid Bhura
"""
from singly_linked_list import SinglyLinkedList
from doubly_linked_list import DoublyLinkedList


def main():
    """Provides access to the module as standalone project."""
    sll = SinglyLinkedList()
    dll = DoublyLinkedList()

    dll.insert_head(10)
    dll.insert_head(11)
    dll.insert_tail(5)
    dll.insert_head(15)
    dll.insert_tail(200)
    dll.print()


if __name__ == '__main__':
    main()
