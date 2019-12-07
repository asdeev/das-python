#! /usr/local/bin/python3
"""
    Description: The main app to test out the Trie.

    Title: main.py

    Author: Zaid Bhura
"""
from trie import Trie


def main():
    """Provides access to the module as standalone project."""
    test_trie = Trie()

    try:
        test_trie.add_word('apple')
        test_trie.add_word('orange')
        test_trie.add_word('apple')
    except ValueError as err:
        print(err)

    try:
        print(f"Word 'app' found? [{test_trie.find_word('app')}]")
        print("Adding word 'app' to trie")
        test_trie.add_word('app')
        print(f"Word 'app' found? [{test_trie.find_word('app')}]")
    except ValueError as err:
        print(err)

    print(test_trie.__dict__)


if __name__ == '__main__':
    main()
