# 1. List
# Definition: An ordered, mutable collection of elements, allowing duplicate values. Lists can contain elements of different types.
fruits = ["apple", "banana", "cherry"]

# 2. Tuple
# Definition: An ordered, immutable collection of elements. Tuples can contain elements of different types, but once created, their elements cannot be changed.
coordinates = (10.0, 20.0)

# 3. Set
# Definition: An unordered, mutable collection of unique elements. Sets do not allow duplicate values.
unique_numbers = {1, 2, 3, 4}

# 4. Dictionary
# Definition: An unordered, mutable collection of key-value pairs. Keys must be unique and immutable, while values can be of any data type.
student = {"name": "John", "age": 21, "grade": "A"}

# 5. String
# Definition: An immutable sequence of characters used to store and manipulate text. Strings can be indexed and sliced like lists.
greeting = "Hello, World!"

# 6. Array
# Definition: Similar to lists, but all elements must be of the same data type. Arrays are used for numerical operations and are typically implemented using external libraries like numpy.
import numpy as np
numbers = np.array([1, 2, 3, 4])

# 7. Stack
# Definition: A linear data structure following the Last In, First Out (LIFO) principle. The last element added is the first one to be removed. Can be implemented using a list.
stack = []
stack.append(1)
stack.append(2)
stack.pop()  # Removes and returns 2

# 8. Queue
# Definition: A linear data structure following the First In, First Out (FIFO) principle. The first element added is the first one to be removed. Can be implemented using collections.deque.
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)
queue.popleft()  # Removes and returns 1

# 9. Linked List
# Definition: A linear data structure where each element (node) contains a value and a reference (link) to the next node in the sequence. Unlike arrays, linked lists do not have fixed sizes.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

# 10. Binary Tree
# Definition: A hierarchical data structure where each node has at most two children, referred to as the left child and the right child. Used in searching and sorting algorithms.
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 11. Graph
# Definition: A collection of nodes (vertices) and edges connecting them. Graphs can be directed or undirected, and are used to represent networks, such as social connections or paths.
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
