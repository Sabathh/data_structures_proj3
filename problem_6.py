import random

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Time complexity: O(n), where n is the number of items in ints.
                           the min and max values are retrieved in a
                           single traversal of ints.

    Space complexity: O(1): Space used is independent of the size of ints

    Args:
       ints(list): list of integers containing one or more integers
    """
    # Sanity check: is ints empty?
    if len(ints) == 0:
       return None

    # Initialize min and max with the first value of ints
    min = ints[0] 
    max = ints[0]

    # Traverse ints once to find min and max values
    for item in ints:
       if item < min:
          min = item
       elif item > max:
          max = item

    return (min, max)


def test_edge_cases():
   # Empty list
   assert(get_min_max([]) == None)

   #Single item list
   assert(get_min_max([1]) == (1, 1))

   # List with repeated items
   assert(get_min_max([2, 2, 2, 2, 2]) == (2, 2))

def test_randomized_cases():
   # 10 integers suffled and tested 10 times 
   l = [i for i in range(0, 10)]  # a list containing 0 - 9
   for _ in range(10):
      random.shuffle(l)
      assert(get_min_max(l) == (0, 9))

if __name__ == "__main__":

    test_edge_cases()

    test_randomized_cases()

    