def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Time complexity: O(n), where n is the number of items in input_list

    Space complexity: O(1): Only in-place switching is used to rearrange the list. 
                            Space is independent of lenght of input_list

    Args:
       input_list(list): List to be sorted
    """

    front_index = 0 # Front of unsorted array. Any position before this index contains a 0
    back_index = len(input_list)-1 # End of unsorted array. Any position after this index contains a 2

    curr_index = 0
    
    while curr_index <= back_index:
        if input_list[curr_index] == 0:
            # Found a 0. Switch it with value in front_index
            input_list[front_index], input_list[curr_index] = input_list[curr_index], input_list[front_index]

            front_index += 1 # All values before this are 0

            curr_index += 1 

        elif input_list[curr_index] == 2:
            # Found a 0. Switch it with value in back_index
            input_list[back_index], input_list[curr_index] = input_list[curr_index], input_list[back_index]

            back_index -= 1 # All values after this are 2
            # curr_index is not incremented. This is because the new value at curr_index has not been verified yet.
        else:
            # Item in correct position. Carry on
            curr_index += 1

    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    assert(sorted_array == sorted(test_case))

def test_edge_cases():
    # One of each, unsorted
    test_function([2, 0, 1])
    # One of each, sorted
    test_function([0, 1, 2])
    # One 0, one 2 and many 1s
    test_function([2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    # Long sorted
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

def test_regular_cases():

    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])

    test_function([0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2])

if __name__ == "__main__":
    
    test_edge_cases()

    test_regular_cases()
    
    
