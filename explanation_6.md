# Problem 6

## Requirement

In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?

## Implementation

Initialized 2 paramenters with the first element of the input list:

- $min$ - Shall store the lowest value in the list so far
- $max$ - Shall store the highest value in the list so far

Traverse the entire list. 
- If the current value is lower than $min$: update $min$
- If the current value is higher than $max$: update $max$

## Time complexity

$O(n)$, where n is the number of items in ints.
The $min$ and $max$ values are retrieved in a single traversal of the list.

## Space complexity

$O(1)$: Space used is independent of the size of ints
