"""
    Title: main.py
    Description: The main module to execute the server binary tree program
    Author: Zaid Bhura
"""
from server import Server


def main():
    main_server = Server()

    values = [4, 10, 3, 200, 25, 26, 1, 15, 500, 100, 20, 30, 40, 100, 200, 300]

    for value in values:
        main_server.add_to_bst(value)

    print('\nInorder Binary Search Tree Traversal:\n')
    main_server_bst_root = main_server.get_server_bst_root()
    main_server.print_inorder(main_server_bst_root)
    print('\n\nPreorder Binary Search Tree Traversal:\n')
    main_server.print_preorder(main_server_bst_root)
    print('\n\nPostorder Binary Search Tree Traversal:\n')
    main_server.print_postorder(main_server_bst_root)


if __name__ == '__main__':
    """Runs the code as a standalone module"""
    main()
