"""
    Title: server.py
    Description: A server simulation for where the binary search tree will live
    Author: Zaid Bhura
"""
from __future__ import annotations

from tree_node import TreeNode
from binary_search_tree import BinarySearchTree

import random
from ipaddress import IPv4Address
from typing import Dict, Union


def provision_server():
    """Return a provisioned server IP address"""
    return str(IPv4Address(random.getrandbits(32)))


class Server:
    def __init__(self):
        self.__bst = BinarySearchTree()
        self.__expansion_servers: Dict[str, Server] = {}

    def add_to_bst(self, value: int):
        direction = self.__bst.add_node(value=value)

        if direction is not None:
            # the tree node which will have either its right or left sub-tree point to a server ip
            tree_node = direction[0]
            if direction[1] == 'right':
                # server ip will exist on the right sub-tree of the returned tree node
                if tree_node.get_right_node() is None:
                    # if no server ip exists on sub-tree, create it
                    new_server = provision_server()
                    self.__expansion_servers[new_server] = Server()

                    # point the tree node sub-tree to the new server ip
                    tree_node.set_right_node(new_server)
                    # add the attempted insertion value into the new server bst
                    self.__expansion_servers[new_server].add_to_bst(value=value)
                elif tree_node.get_right_node() in self.__expansion_servers:
                    # if server ip already exists as a sub-tree value, then continue adding to that server's bst
                    self.__expansion_servers[tree_node.get_right_node()].add_to_bst(value=value)
            else:
                if direction[1] == 'left':
                    # server ip will exist on the left sub-tree of the returned tree node
                    if tree_node.get_left_node() is None:
                        # if no server ip exists on sub-tree, create it
                        new_server = provision_server()
                        self.__expansion_servers[new_server] = Server()

                        # point the tree node sub-tree to the new server ip
                        tree_node.set_left_node(new_server)
                        # add the attempted insertion value into the new server bst
                        self.__expansion_servers[new_server].add_to_bst(value=value)
                    elif tree_node.get_left_node() in self.__expansion_servers:
                        # if server ip already exists as a sub-tree value, then continue adding to that server's bst
                        self.__expansion_servers[tree_node.get_left_node()].add_to_bst(value=value)

    def get_server_bst_root(self) -> TreeNode:
        """Return the binary search tree root node for this server"""
        return self.__bst.get_root()

    def print_inorder(self, root: Union[TreeNode, str]):
        """Print the inorder traversal of the binary search tree"""
        if root:
            if type(root) == str:
                root = self.__expansion_servers[root].get_server_bst_root()

            self.print_inorder(root=root.get_left_node())
            print(root.get_value())
            self.print_inorder(root=root.get_right_node())

    def print_preorder(self, root: Union[TreeNode, str]):
        """Print the preorder traversal of the binary search tree"""
        if root:
            if type(root) == str:
                root = self.__expansion_servers[root].get_server_bst_root()

            print(root.get_value())
            self.print_preorder(root=root.get_left_node())
            self.print_preorder(root=root.get_right_node())

    def print_postorder(self, root: Union[TreeNode, str]):
        """Print the postorder traversal of the binary search tree"""
        if root:
            if type(root) == str:
                root = self.__expansion_servers[root].get_server_bst_root()

            self.print_postorder(root=root.get_left_node())
            self.print_postorder(root=root.get_right_node())
            print(root.get_value())
