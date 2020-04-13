# Data Structures & Algorithms Nanodegree Program (Udacity)

Note: The following text was assembled using parts of the original descriptions available in the Nanodegree ND256 at the time of writing. For more information about the Nanodegree please visit the official page [here](https://www.udacity.com/course/data-structures-and-algorithms-nanodegree--nd256).

## Project 3: Problems vs. Algorithms

Table of Contents

- [Data Structures & Algorithms Nanodegree Program (Udacity)](#data-structures--algorithms-nanodegree-program-udacity)
  - [Project 3: Problems vs. Algorithms](#project-3-problems-vs-algorithms)
    - [Description](#description)
    - [Problem 1 - Square Root of an Integer](#problem-1---square-root-of-an-integer)
    - [Problem 2 - Search in a Rotated Sorted Array](#problem-2---search-in-a-rotated-sorted-array)
    - [Problem 3 - Rearrange Array Digits](#problem-3---rearrange-array-digits)
    - [Problem 4 - Dutch National Flag Problem](#problem-4---dutch-national-flag-problem)
    - [Problem 5 - Autocomplete with Tries](#problem-5---autocomplete-with-tries)
    - [Problem 6 - Unsorted Integer Array](#problem-6---unsorted-integer-array)
    - [Problem 7 - Request Routing in a Web Server with a Trie](#problem-7---request-routing-in-a-web-server-with-a-trie)

### Description

This project consists of *seven* questions laid out in the next sections. The questions cover a variety of topics related to the basic algorithms learned in the course. The answer consists of a clean and efficient code in Python, as well as a text explanation of the efficiency of the code and design choices.

### Problem 1 - Square Root of an Integer

Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is `O(log(n))`.

_The solution of problem 1 can be found [here](https://github.com/Sabathh/data_structures_proj3/blob/master/problem_1.py)._
_The efficiency explanation of problem 1 can be found [here](https://github.com/Sabathh/data_structures_proj3/blob/master/explanation_1.md)._

### Problem 2 - Search in a Rotated Sorted Array

You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and the algorithm's runtime complexity must be in the order of `O(log n)`.

Example:

Input:

```python
    nums = [4,5,6,7,0,1,2], target = 0, Output: 4
```

_The solution of problem 2 can be found [here](https://github.com/Sabathh/data_structures_proj3/blob/master/problem_2.py)._
_The efficiency explanation of problem 2 can be found [here](https://github.com/Sabathh/data_structures_proj3/blob/master/explanation_2.md)._

### Problem 3 - Rearrange Array Digits

Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is `O(nlog(n))`.

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

_The solution of problem 3 can be found [here](https://github.com/Sabathh/data_structures_proj3/blob/master/problem_3.py)._
_The efficiency explanation of problem 3 can be found [here](https://github.com/Sabathh/data_structures_proj3/blob/master/explanation_3.md)._

### Problem 4 - Dutch National Flag Problem

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

**Note:** `O(n)` does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an `O(n)` solution but it will not count as single traversal.

_The solution of problem 4 can be found [here](https://github.com/Sabathh/data_structures_proj3/blob/master/problem_4.py)._
_The efficiency explanation of problem 4 can be found [here](https://github.com/Sabathh/data_structures_proj3/blob/master/explanation_4.md)._

### Problem 5 - Autocomplete with Tries

Uses a Trie data structure to create an Autocomplete function.

_For more information, please refer to the [notebook here](https://github.com/Sabathh/data_structures_proj3/blob/master/problem_5.ipynb)._

_The efficiency explanation of problem 5 can be found [here](https://github.com/Sabathh/data_structures_proj3/blob/master/explanation_5.md)._

### Problem 6 - Unsorted Integer Array

In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

**Bonus Challenge:** Is it possible to find the max and min in a single traversal?

Sorting usually requires O(n log n) time Can you come up with a O(n) algorithm (i.e., linear time)?

_The solution of problem 6 can be found [here](https://github.com/Sabathh/data_structures_proj3/blob/master/problem_6.py)._
_The efficiency explanation of problem 6 can be found [here](https://github.com/Sabathh/data_structures_proj3/blob/master/explanation_6.md)._

### Problem 7 - Request Routing in a Web Server with a Trie

For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.

There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler.

First we need to implement a slightly different Trie than the one we used for autocomplete. Instead of simple words the Trie will contain a part of the http path at each node, building from the root node `/`.

In addition to a path though, we need to know which function will handle the http request. In a real router we would probably pass an instance of a class like Python's [SimpleHTTPRequestHandler](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler) which would be responsible for handling requests to that path. For the sake of simplicity we will just use a string that we can print out to ensure we got the right _handler_.

We could split the path into letters similar to how we did the autocomplete Trie, but this would result in a Trie with a very large number of nodes and lengthy traversals if we have a lot of pages on our site. A more sensible way to split things would be on the parts of the path that are separated by slashes ("/"). A Trie with a single path entry of: "/about/me" would look like:

(root, None) -> ("about", None) -> ("me", "About Me handler")

We can also simplify our RouteTrie a bit by excluding the suffixes method and the endOfWord property on RouteTrieNodes. We really just need to insert and find nodes, and if a RouteTrieNode is not a leaf node, it won't have a handler which is fine.

```python
# A RouteTrie will store our routes andtheir   associated handlers
class RouteTrie:
    def __init__(self, ...):
        # Initialize the trie with an root node     and a handler, this is the root path or     home page node
    def insert(self, ...):
        # Similar to our previous example you will  want to recursively add nodes
        # Make sure you assign the handler to only  the leaf (deepest) node of this path
    def find(self, ...):
        # Starting at the root, navigate the Trie   to find a match for this path
        # Return the handler for a match, or None   for no match
# A RouteTrieNode will be similar to our   autocomplete TrieNode... with one additional  element, a handler.
class RouteTrieNode:
    def __init__(self, ...):
        # Initialize the node with children as  before, plus a handler
    def insert(self, ...):
        # Insert the node as before
```

Next we need to implement the actual Router. The router will initialize itself with a RouteTrie for holding routes and associated handlers. It should also support adding a handler by path and looking up a handler by path. All of these operations will be delegated to the RouteTrie.

Hint: the RouteTrie stores handlers under path parts, so remember to split your path around the '/' character

Bonus Points: Add a not found handler to your Router which is returned whenever a path is not found in the Trie.

More Bonus Points: Handle trailing slashes! A request for '/about' or '/about/' are probably looking for the same page. Requests for '' or '/' are probably looking for the root handler. Handle these edge cases in your Router.

```python
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, ...):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!

    def add_handler(self, ...):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie

    def lookup(self, ...):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler


    def split_path(self, ...):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
```

_The solution of problem 7 can be found [here](https://github.com/Sabathh/data_structures_proj3/blob/master/problem_7.py)._
_The efficiency explanation of problem 7 can be found [here](https://github.com/Sabathh/data_structures_proj3/blob/master/explanation_7.md)._
