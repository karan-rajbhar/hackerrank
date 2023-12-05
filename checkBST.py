import unittest
from collections import deque
""" Node is defined as
"""
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isValidBST(root,min = float('-inf') , max =float('inf')):
    if root is None:
        return True
    
    if not (min < root.data < max):
        return False
    
    return isValidBST(root.left , min , root.data) and isValidBST(root.right,root.data,max)


def checkBST(root):
    return isValidBST(root)



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class TestCheckBST(unittest.TestCase):
    # def test_empty_tree(self):
    #     self.assertTrue(checkBST(None))

    # def test_single_node_tree(self):
    #     root = Node(1)
    #     self.assertTrue(checkBST(root))

    # def test_valid_binary_search_tree(self):
    #     root = Node(2)
    #     root.left = Node(1)
    #     root.right = Node(3)
    #     self.assertTrue(checkBST(root))

    # def test_invalid_binary_search_tree(self):
    #     root = Node(2)
    #     root.left = Node(3)
    #     root.right = Node(1)
    #     self.assertFalse(checkBST(root))
    # def test_complex_valid_binary_search_tree(self):
    #     root = Node(8)
    #     root.left = Node(3)
    #     root.right = Node(10)
    #     root.left.left = Node(1)
    #     root.left.right = Node(6)
    #     root.right.right = Node(14)
    #     root.left.right.left = Node(4)
    #     root.left.right.right = Node(7)
    #     root.right.right.left = Node(13)
    #     self.assertTrue(checkBST(root))

    def test_complex_invalid_binary_search_tree(self):
        root = Node(8)
        root.left = Node(3)
        root.right = Node(10)
        root.left.left = Node(1)
        root.left.right = Node(6)
        root.right.right = Node(14)
        root.left.right.left = Node(4)
        root.left.right.right = Node(7)
        root.right.right.left = Node(9)  # This node violates the BST property
        
        self.assertFalse(checkBST(root))

if __name__ == '__main__':
    unittest.main()