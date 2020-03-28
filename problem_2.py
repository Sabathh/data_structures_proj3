def rotated_array_search(input_list: list, number: int) -> int:
    """
    Find the index by searching in a rotated sorted array.

    Algorithm is a modified version of the binary search. 
    The search first finds a position on the side of the pivot where the number is located. 
    Once a position on the correct side of the pivot is found then a standard bisection search completes the process.

    Time complexity: O(log(n)), where n is the number of elements in input_list. 
                                The algorithm does as many iterations as a bisection search
    
    Space complexity: O(1): Space used is independent of the size of input_list

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # Sanity Check: Is list empty?
    if len(input_list) == 0:
        return -1
        
    lower_index = 0
    upper_index = len(input_list) - 1

    first_val = input_list[lower_index]
    last_val = input_list[upper_index]

    # Check if either end of the array is the result
    if first_val == number:
        return lower_index
    elif last_val == number:
        return upper_index

    # Boolean that verifies which side of the pivot the number is located
    number_left_of_pivot = number > first_val

    while upper_index - lower_index > 1:

        mid_index = (lower_index + upper_index) // 2
        mid_val = input_list[mid_index]

        if mid_val == number:
            return mid_index

        # Boolean that verifies which side of the pivot mid_val is located
        mid_val_left_of_pivot = mid_val > first_val

        # Check if mid_val is on the correct side of the pivot
        if number_left_of_pivot and not mid_val_left_of_pivot:
            # Move search towards left side of pivot
            upper_index = mid_index
        elif not number_left_of_pivot and mid_val_left_of_pivot:
            # Move search towards right side of pivot
            lower_index = mid_index
        else:
            # mid_val is on the correct side of pivot found. Perform bisection search
            if mid_val > number:
                upper_index = mid_index
            else:
                lower_index = mid_index

    # number not in input_list
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

def test_edge_cases():
    # Empty list
    test_function([[], 0])

    # List with single item
    test_function([[6], 6])

    # List with single item. Value not in list
    test_function([[6], 0])

    # List with negative numbers
    test_function([[-3, -2, -1, -8, -7, -6, -5, -4], -2])

    # List with negative and positive numbers
    test_function([[0, 1, 2, 3, -4, -3, -2, -1], -2])

    # Regular list. Number not in list
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])

if __name__ == "__main__":

    test_edge_cases()
    
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 7])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 9])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 10])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 2])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 3])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 4])
    
    test_function([[6, 7, 8, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 1, 2, 3, 4], 7])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 2])
    test_function([[6, 7, 8, 1, 2, 3, 4], 3])
    test_function([[6, 7, 8, 1, 2, 3, 4], 4])
    