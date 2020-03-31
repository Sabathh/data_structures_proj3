# TODO: Organize Heap class
class Heap:
    def __init__(self, initial_size):
        if initial_size < 3:
            # Makes sure the root will always have left and right nodes
            initial_size = 3
        self.cbt = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0                             # denotes next index where new element should go

    def size(self):
        return self.next_index 

    def is_empty(self):
        return self.size() == 0
    
    def _up_heapify(self):
        child_index = self.next_index
        parent_index = (child_index - 1) // 2
        
        child_val = self.cbt[child_index]
        parent_val = self.cbt[parent_index]
        
        while parent_val > child_val:
            # Swap values
            self.cbt[child_index] = parent_val
            self.cbt[parent_index] = child_val
            
            # Update indexes
            child_index = parent_index
            parent_index = (child_index - 1) // 2
            
            if parent_index < 0:
                # Reached root node
                break
            
            # Update values
            child_val = self.cbt[child_index]
            parent_val = self.cbt[parent_index]

    def _down_heapify(self):
        # Get initial indexes
        current_index = 0
        left_index = 1
        right_index = 2

        # Get initial values
        current_val = self.cbt[current_index]
        left_val = self.cbt[left_index]
        right_val = self.cbt[right_index]

        if right_val is None:
            if left_val is not None and left_val < current_val:
                self.cbt[current_index] = left_val
                self.cbt[left_index] = current_val
            return

        while current_val > left_val or current_val > right_val:
            if right_val > left_val:
                # Switch current_val with left_val
                self.cbt[current_index] = left_val
                self.cbt[left_index] = current_val

                # Update current index
                current_index = left_index
            else:
                # Switch current_val with right_val
                self.cbt[current_index] = right_val
                self.cbt[right_index] = current_val

                # Update current index
                current_index = right_index


            # Get new indexes
            left_index = 2 * (current_index + 1)
            right_index = 2 * (current_index + 2)
            if left_index >= self.size() or right_index >= self.size() :
                # Reached the end of the tree
                return

            # Get new values
            current_val = self.cbt[current_index]
            left_val = self.cbt[left_index]
            right_val = self.cbt[right_index]
            if left_val is None or right_val is None:
                return

    def insert(self, data):
        """
        Insert `data` into the heap

        Time complexity: O(log(n))
        Space complexity: O(1)
        """
        # Insert data at next index
        self.cbt[self.next_index] = data
        
        
        # Up Heapify
        if self.next_index != 0:
            self._up_heapify()
            
        # Increment next index
        self.next_index += 1
        
        # Double array if next_index is out of bounds
        if self.next_index >= len(self.cbt):
            new_array = [None for _ in range(2*len(self.cbt))]
            for index in range(len(self.cbt)):
                new_array[index] = self.cbt[index]
                
            self.cbt = new_array

    def remove(self):
        """
        Remove and return the element at the top of the heap

        Time complexity: O(log(n))
        Space complexity: O(1)
        """
        root = self.cbt[0]
        if root is None:
            return root

        # Move last element at the root
        self.cbt[0] = self.cbt[self.next_index - 1]
        self.cbt[self.next_index - 1] = None

        # Down heapify
        self._down_heapify()

        # Decrease next index
        self.next_index -= 1

        return root

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Time complexity: O(nlog(n)), where n is the number of items in input_list.
                                 Both Heap.insert and Heap.remove() have complexity
                                 of O(log(n)). Both of these methods are used n times each.
                                 
    Space complexity: O(n), where n is the number of items in input_list.
                            The Heap object created contains a list of size (n+1) 
                            to store all items of input_list.


    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # Min-heap is used because both insertion and removal of elements have complexity of O(log(n))
    heap = Heap(len(input_list) + 1) # len + 1 is used to prevent Heap from doubling its available size when last element is added

    # Inserting elements into heap. O(log(n)) for each element. O(nlog(n)) to populate heap 
    for item in input_list:
        heap.insert(item)

    order_magnitude = 0
    first_num = 0
    second_num = 0

    # Remove top element from heap to assemble both numbers. 
    # In order to maximize the sum of both the lower numbers are used for 
    # lower orders of magnitude. 
    for _ in input_list:
        
        if first_num < 10**order_magnitude:
            first_num += heap.remove() * 10**order_magnitude
        else:
            second_num += heap.remove() * 10**order_magnitude
            order_magnitude += 1 # order_magnitude is only incremented when both first_num and second_num are higher than that order of magnitude
    
    return [first_num, second_num]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    # The main requirement is to return two numbers whose sum is the highest possible
    # The order of the digits does not matter or numbers.
    assert(sum(output) == sum(solution))

def test_edge_cases():
    # Empty list
    test_function([[], [0, 0]])
    # List with single number
    test_function([[1], [1, 0]])

def test_regular_cases():
    test_function([[1, 2, 3, 4, 5], [542, 31]])
    test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

if __name__ == "__main__":

    test_edge_cases()

    test_regular_cases()

