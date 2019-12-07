"""
    Description: An implementation of the Trie.

    Title: trie.py

    Author: Zaid Bhura
"""
from typing import List


class Trie(object):

    def __init__(self):
        """Initialize Trie object."""
        self._end = '*'
        self.trie = dict()

    def find_word(self, word: str):
        """Find word in trie

        This function will find a word in a trie.
        Runs in O(m) time

        :param
            word: str: The word to find in the trie

        """
        sub_trie = self.trie

        for letter in word:
            if letter in sub_trie:
                sub_trie = sub_trie[letter]
            else:
                return False
        else:
            if self._end in sub_trie:
                return True
            else:
                return False

    def add_word(self, word):
        """Add new word to trie

        This function will insert a new word into the trie
        Runs in O(m) time

        :param
            word: str: The word to add to the trie

        """
        if self.find_word(word):
            raise ValueError(f"Word '{word}' already exists")

        temp_trie = self.trie

        for letter in word:
            if letter in temp_trie:
                temp_trie = temp_trie[letter]
            else:
                temp_trie = temp_trie.setdefault(letter, {})
        temp_trie[self._end] = self._end
