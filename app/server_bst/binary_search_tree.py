"""
    Title: tree_node.py
    Description: The binary search tree structure
    Author: Zaid Bhura
"""
from tree_node import TreeNode


class BinarySearchTree:
    def __init__(self):
        self.__root = TreeNode()
        self.__count = 0
        self.__MAX_COUNT = 7

    def add_node(self, value: int):
        """Add a new node to the binary search tree

        This function will add a new tree node to the correct location in the binary search tree.

        :param value: The integer value which will be added to the tree
        :return: [temp, <'right', 'left'>] or None: The tree node and sub-tree
            direction to insert for new server if current server tree count is maxed, otherwise None

        """
        temp = self.__root

        # flag to keep searching for a spot to insert the new value
        searching = True

        while searching:
            if temp.get_value() is None:
                # if no root value exists, then initialize that value
                temp.set_value(value=value)
                self.__count += 1
                searching = False
            elif temp.get_value() >= value:
                # value is less than root so move into left sub-tree
                if temp.get_left_node() is not None and type(temp.get_left_node()) != str:
                    # left sub-tree has a node which is not a pointer to a server ip
                    temp = temp.get_left_node()
                elif self.__count < self.__MAX_COUNT:
                    # add a new node to the left sub-tree if the count is less than the max storage
                    new_node = TreeNode(value=value)
                    temp.set_left_node(new_node)
                    self.__count += 1
                    searching = False
                else:
                    # server ip pointer is existing or needs to be created on the left sub-tree of this node
                    return [temp, 'left']
            elif temp.get_value() < value:
                # value is greater than root so move into right sub-tree
                if temp.get_right_node() is not None and type(temp.get_right_node()) != str:
                    # right sub-tree has a node which is not a pointer to a server ip
                    temp = temp.get_right_node()
                elif self.__count < self.__MAX_COUNT:
                    # add a new node to the right sub-tree if the count is less than the max storage
                    new_node = TreeNode(value=value)
                    temp.set_right_node(new_node)
                    self.__count += 1
                    searching = False
                else:
                    # server ip pointer is existing or needs to be created on the right sub-tree of this node
                    return [temp, 'right']

    def get_root(self) -> TreeNode:
        """Return the root node of the binary search tree"""
        return self.__root
