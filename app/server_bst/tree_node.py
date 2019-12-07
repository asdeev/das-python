"""
    Title: tree_node.py
    Description: The tree node which will store a single data value and child pointers
    Author: Zaid Bhura
"""
from __future__ import annotations

from typing import Union


class TreeNode:
    def __init__(self, value: int = None):
        self.__value = value
        self.__left_node = None
        self.__right_node = None

    def get_value(self) -> int:
        return self.__value

    def set_value(self, value: int):
        self.__value = value

    def get_left_node(self) -> Union[TreeNode, str]:
        return self.__left_node

    def set_left_node(self, tree_node: Union[TreeNode, str]):
        self.__left_node = tree_node

    def get_right_node(self) -> Union[TreeNode, str]:
        return self.__right_node

    def set_right_node(self, tree_node: Union[TreeNode, str]):
        self.__right_node = tree_node
