# Problem 1

## Requirement

Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

## Implementation

The requirement is asking the integer (floored) solution to the following equation:

$\sqrt(number) = x$

Which can be rewritten as:

$x^2 = number$ 

Since the requirement forbids us from using Python libraries we can solve the first equation by trying different $x$ values on the second equation until a value is found.

In order to reduce the number of guesses I've decided to apply the Bisection method. The search range is defined as follows:

$upper\_lim = number / 2$
$lower\_lim = 2$

Excluding the degenerated square root cases ($x=0$ and $x=1$, where $number=x$) the lowest posssible answer for the equation is $x=2$ ($number=2$) and the highest possible answer is always half of $number$ (also for $number=2$).

All the operations performed during the Bisection method are integer operations. Both limits are updated until there is a difference of 1 between them.

To make sure the result is always floored the final result squared is compared with the $number$. If the results squared is higher tahn $number$, then the value of the updated lower_lim is returned instead.

## Time complexity

$O(log(n))$, where n is half of the input number. This is due to the selected range.

Bisection method has the complexity of $O(log(n))$.

## Space complexity

$O(1)$: Space used is independent of the input value
