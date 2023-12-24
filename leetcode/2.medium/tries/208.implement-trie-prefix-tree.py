#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

from typing import Dict, List, Optional, Type


class TrieNode:
    def __init__(self) -> None:
        self.word_end: bool = False
        self.children: Dict = {}

    def tree_repr(self, level=0, last=True, prefix=""):
        # Construct the "graphic" part of the representation
        turn = "└── " if last else "├── "
        word_marker = "*" if self.word_end else ""
        part = [prefix + turn + word_marker]

        # Prepare the prefix for child nodes
        child_prefix = prefix + ("    " if last else "│   ")

        # Add all children to the representation
        child_count = len(self.children)
        for i, (char, child) in enumerate(sorted(self.children.items())):
            is_last = i == (child_count - 1)
            parts = child.tree_repr(level + 1, is_last, child_prefix)
            if parts:  # If the child added any parts
                part.append(char + parts[0])
                part.extend(parts[1:])

        return part

    def __repr__(self):
        return "\n".join(self.tree_repr())


class Trie:
    """
    A trie is a variant of an n-ary tree in which a node represents a character,
        and each path down the tree may represent a word
    Using the dictionary as the data structure for children of each trie node
        since checking if a child node exists (`char in node.children`) with dict is O(1)
    Runtime: O(n) for both insert, search and startswith operations where n
        is the length of the input word
    Space complexity: O(n) for insert, search and startswith, where n is the length of
        the word
    Note: Tries are very space-efficient when there are many common prefixes, as they share
        the same initial nodes for all words with the same prefix.
    """

    def __init__(self):
        self.root = TrieNode()

    def __repr__(self) -> str:
        return self._build_repr(self.root, "", "")

    def __repr__(self) -> str:
        # Start the representation from the root
        return repr(self.root)

    def insert(self, word: str) -> None:
        """
        Insert a word path into the Trie. Each node represent a character.
        Runtime and Space Complexity: O(n) where n is the length of the word, since we traverse
         the entire trie from the root to the leaf if the path does not exist
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word_end = True

    def search(self, word: str) -> bool:
        """
        search if word is in the Trie
        Runtime and Space Complexity: O(n) where n is the length of the word
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word_end

    def startsWith(self, prefix: str) -> bool:
        """
        search if words with prefix exist in the Trie
        Runtime and Space Complexity: O(n) where n is the length of the prefix
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("apple")
trie.insert("app")  # we want something like {"a": Trie({"p": Trie(word_end=True)})}
trie.insert("bee")  # we want something like {"a": Trie({"p": Trie(word_end=True)})}
trie.insert("beep")  # we want something like {"a": Trie({"p": Trie(word_end=True)})}
trie.insert("beef")  # we want something like {"a": Trie({"p": Trie(word_end=True)})}
print(trie)
print(trie.search(word="app"))
print(trie.search("apple"))
print(trie.startsWith("app"))
print(trie.startsWith("bee"))
print(trie.startsWith("apple"))
print(trie.startsWith("beeff"))
print(trie.search("beeff"))

# @lc code=end
