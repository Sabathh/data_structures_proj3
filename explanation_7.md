# Problem 7

## Requirement

Implement a HTTPRouter using a Trie.

## Implementation

The main function implemented are:

- $RouteTrie.insert$
  - Navigates through the Trie using the list of paths provided, creating nodes if the do not yet exist. After reaching the end of the path list a handler is stored on the leaf node.
- $RouteTrie.find$
  - Navigates through the Trie using the list of paths provided. After reaching the enf of the list returns the handler of the related node. If the path does not exist returns None.

## Time complexity

- $RouteTrie.insert$: $O(n)$, where n is the number of items in path_list.
- $RouteTrie.find$: $O(n)$, where n is the number of items in path_list.

## Space complexity

- $RouteTrie.insert$: $O(n)$. Number of nodes created scales linearly with the size of path_list
- $RouteTrie.find$: $O(1)$. Space used is independent of the inputs..
  