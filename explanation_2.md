# Problem 2

## Requirement

You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of $O(log n)$.

## Implementation

The solution implemented is a modified version of the binary search.

The initial lower and upper boundaries are the first and last index of the input array.

First I do a comparison between the input $number$ and the first position of the input array. If $number$ is higher then I know that $number$ is located to the left of the pivot. Otherwise it is on the right.

The I start the binary search as usual, except that instead of comparing the $mid_value$ against the input $number$ I verify whether the $mid_value$ is on the left or right of the pivot, using the same logic as before. Then I move one of the boundaries of the search to the index of $mid_value$, depending on which side of the pivot $number$ is.

After a $mid_value$ on the correct side of the pivot is located the search reverts to a regular bisection search, comparing $mid_value$ against $number$ and updating the boundaries accordingly. This can be done because, as implied on the requirement, each side of the pivot is a sorted list.

## Time complexity

$O(log(n))$, where n is the number of elements in input_list. 
The algorithm does as many iterations as a bisection search

## Space complexity

$O(1)$: Space used is independent of the size of input_list

