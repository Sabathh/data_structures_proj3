# Problem 3

## Requirement

Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is $O(nlog(n))$.

## Implementation

To make the highest possible pair of number given a list of number I need to make sure that the highest numbers will occupy the highest orders of magnitude.

Or, by reverting the reasoning, I need to make sure the lowest numbers will occupy the lowest orders of magnitude.

Ex:

Given [9, 8, 7, 6] -> (97, 86)

In order to achieve this I first insert the numbers into a Min-Heap.

A Min-Heap was selected for 2 reasons:

- Both insertion and removal of elements have a complexity of $O(log(n))$.
- The lowest value value available is always on the root.

After assembling the Min-Heap I remove each element one by one and assemble the final pairs. I populate the first order of magnitude for both numbers ($10^0$) and only then move on to the next order ($10^1$), and so on.

## Time complexity

$O(nlog(n))$, where n is the number of items in $input_list$.
Both $Heap.insert$ and $Heap.remove()$ have complexity of $O(log(n))$. Both of these methods are used n times each.

## Space complexity

$O(n)$, where n is the number of items in $input_list$.
The Heap object created contains a list of size (n+1) to store all items of input_list.
