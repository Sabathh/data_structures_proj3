def sqrt(number : int) -> int:
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if  type(number) is not int:
        raise TypeError('Input provided is not an integer')
    elif number < 0:
        raise ValueError('Square root function cannot handle negative inputs')
    elif number < 2:
        return number
    
    upper_lim = number//2
    lower_lim = 2

    diff = upper_lim - lower_lim

    while diff > 1:

        mid_val = (lower_lim + upper_lim) // 2

        if mid_val*mid_val > number:
            upper_lim = mid_val
        else:
            lower_lim = mid_val

        diff = upper_lim - lower_lim

    # Check if mid_val^2 is bigger than the number and return lower_lim if it is
    if mid_val*mid_val > number:
        mid_val = lower_lim

    return mid_val

def test_sqrt(number : int, target : int):
    result = sqrt(number)
    print("sqrt(" + str(number) + ") = " + str(result) + " (expected " + str(target) + ")")
    assert(target == result)

if __name__ == "__main__":
    # Edge cases
    # sqrt(-1) 
    # ValueError
    # sqrt(None) 
    # TypeError
    test_sqrt(0, 0)
    # 0
    test_sqrt(1, 1)
    # 1

    # Regular cases
    test_sqrt(9, 3)
    # 3
    test_sqrt(16, 4)
    # 4
    test_sqrt(27, 5)
    # 5
    test_sqrt(35, 5)
    # 5
    test_sqrt(36, 6)
    # 6
    test_sqrt(37, 6)
    # 6

    # Big numbers
    test_sqrt(1763, 41)
    # 41
    test_sqrt(1764, 42)
    # 42
    test_sqrt(1765, 42)
    # 42
    test_sqrt(443555, 665)
    # 665
    test_sqrt(443556, 666)
    # 666
    test_sqrt(443600, 666)
    # 666
    