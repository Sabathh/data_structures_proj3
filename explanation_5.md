# Problem 5

## Requirement

Implement an Autocomplete using a Trie.

## Implementation

The main function implemented are:

- $Trie.insert()$
  - Navigates through the Trie using the characters of the word provided, creating nodes if the do not yet exist. After reaching the end of the word the property $is\_word$ of the leaf node is set to $True$.
- $Trie.find()$
  - Navigates through the Trie using the characters of the word provided. After reaching the end of the word returns the related node. If the the word lead to a node that does not exist returns None.
- $TrieNode.suffixes()$
  - Iterates recursively through a single link of children of the TrieNode and assembles a string based on the keys of the property $children$ of each node until a node containing $is\_word=True$ is found. Returns the assembled string.


## Time complexity

- $Trie.insert()$
  - $O(c)$, where c is the number of characters of the word inserted.
- $Trie.find()$
  - $O(c)$, where c is the number of characters of the word being searched.
- $TrieNode.suffixes()$
  - $O(h)$, where h is the height of the Trie.

## Space complexity

- $Trie.insert()$
  - $O(c)$, where c is the number of characters of the word inserted.
- $Trie.find()$
  - $O(1)$. Space used is independent of the size of input_list.
- $TrieNode.suffixes()$
  - $O(1)$. Space used is independent of the size of input_list.



