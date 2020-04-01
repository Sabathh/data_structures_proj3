# Problem 4

## Requirement

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

## Implementation

Since moving the $0$s and $2$s to the correct position results in the $1$s being in the correct position, this is what will be done.

Three indexes are defined:

- $curr\_index$ - Current index in the traversal
- $front\_index$ - Front of the unsorted array. Any position before this index contains a 0.
- $back\_index$ - End of unsorted array. Any position after this index contains a 2.

A loop is performed until $curr\_index$ > $back\_index$. In each iteration one of these conditions is executed:

- If $curr\_index$ contains a 0:
  - Switch value in $curr\_index$ with the one in $front\_index$.
  - Increment $front\_index$.
  - Increment $curr\_index$.
- If $curr\_index$ contains a 2:
  - Switch value in $curr\_index$ with the one in $back\_index$.
  - Increment $back\_index$.
  - Since the new value in $curr\_index$ has not been evaluated yet, $curr\_index$ is not incremented.
- Else:
  - Contains a 1. Increment $curr\_index$.

## Time complexity

 $O(n)$, where n is the number of items in $input\_list$.
 All values in $input\_list$ are evaluated only once

## Space complexity

O(1): Only in-place switching is used to rearrange the list. Space is independent of lenght of $input\_list$.
