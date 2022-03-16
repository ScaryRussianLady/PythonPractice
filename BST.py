'''
Iterative Pseudocode:

BIN-TREE-FIND(tree, target)
    cur_node <- tree.root
    WHILE cur_node != NULL
        IF cur_node.value = taret
            RETURN cur_node (or TRUE) (or cur_node.value)
        ELSE IF cur_node.value > target
            cur_node <- cur_node.left
        ELSE
            cur_node <- cur_node.right
    RETURN FALSE
//Note that BST code is object oriented.
//That means 'self' is the argument rather than 'tree';
//tree is the object this method works on.

Recursive Pseudocode:

BIN-TREE-FIND(tree, target)
    IF tree.root
        IF tree._BIN-TREE-FIND(target, tree.root)
            RETURN True
        RETURN False
    ELSE
        RETURN None

_BIN-TREE-FIND(tree, target, cur_node)
    IF target > cur_node.data AND cur_node.right
        RETURN tree._BIN-TREE-FIND(target, cur_node.right)
    ELSE IF target < cur_node.data AND cur_node.left
        RETURN tree._BIN-TREE-FIND(target, cur_node.left)
    IF target == cur_node.data
        RETURN True

Author: Annija Balode

Algorithm: BST Search
'''
import math

# The Node constructor class containing data attributes and a method for nodes in the Binary Search Tree (BST).
class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

""" BST class with insert and display methods. display pretty prints the tree
"""
# The class for the BST.
class BinaryTree:
    def __init__(self):
        # Set the root node to None.
        self.root = None
        # Set the target node to None.
        self.target = None

    # Function to check whether there is a root node or not.
    def insert(self, data):
        if self.root is None:
            # Sets the first piece of data (the very first bst.insert(x) and sets it as the root node).
            self.root = Node(data)
        else:
            # If there is a root node, moves on to the next function: _insert
            self._insert(data, self.root)

    # Function for inserting nodes after the root node has been established.
    def _insert(self, data, cur_node):
        # If the data value is less than the current node value..
        if data < cur_node.data:
            # If there is no current left node then..
            if cur_node.left is None:
                # Set that data value to the current node on the left of the node above.
                cur_node.left = Node(data)
            else:
                # Recall the _insert function again.
                self._insert(data, cur_node.left)
        # If the data value is more than the current node value.
        elif data > cur_node.data:
            # If there is no current right node then..
            if cur_node.right is None:
                # Set the data value to the current node on the right of the node above.
                cur_node.right = Node(data)
            else:
                # Recall the _insert function again.
                self._insert(data, cur_node.right)
        else:
            # If a value is repeated, the following is printed. 
            print("Value already present in tree")

# A method for finding the target node using an iterative method.
    def find_i(self, target):
        # Set the current node variable as the root node (the node at the top of the tree).
        cur_node = self.root
        # While the current node is not empty.
        while cur_node != None:
            # If the current node is equal to the target (value we are trying to find) return true.
            if cur_node.data == target:
                print(True)
                return True       
            # Otherwise if the current node is greater than the target value..
            elif cur_node.data > target:
                # Set the current node to the value on the left of the current node.
                cur_node = cur_node.left
            # Otherwise if the current node is less than the target value..
            elif cur_node.data < target:
                # Set the current node to the value on the right of the current node.
                cur_node = cur_node.right
            # Else..
            else:
                # Return None.
                print(None)
                return None
        # Return False.
        print(False)
        return False

    # A method to find the target value using a recursive approach.
    def find_r(self, target): 
        if self.root:
            # If the target value has been found..
            if self._find_r(target,self.root):
                # Print True
                print(True)
            else:
                print(False)
        else:
            print(None)
    

    def _find_r(self,target,cur_node):
        # If the target value is greater than the value of the current node AND the value on the right..
        if target > cur_node.data and cur_node.right:
            # Return the target value and the value on the right of the current node.
            return self._find_r(target,cur_node.right)
        # If the target value is less than the value of the current node AND the value on the left..
        elif target < cur_node.data and cur_node.left:
            # Return the target value and the value on the left of the current node.
            return self._find_r(target, cur_node.left)
        # If the target value is equal to the value of the current node..
        if target == cur_node.data:
            # Return True.
            return True

bst = BinaryTree()
bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(7)
bst.insert(8)
bst.insert(9)

bst.display(bst.root)
bst.find_i(6)
bst.find_r(8)
bst.find_i(20)
bst.find_r(12)
