'''
REMOVE(tree, target)
    IF tree.root IS None //if no tree
        RETURN False
    ELSE IF tree.root.data = target //if tree root is target
        IF tree.root.left IS None AND tree.root.right IS None
            tree.root ← None
        ELSE IF tree.root.left AND tree.root.right IS None
            tree.root ← tree.root.left
        ELSE IF tree.root.left IS None AND tree.root.right
            tree.root ← tree.root.right
        ELSE IF tree.root.left AND tree.root.right
            IF_LEFT_AND_RIGHT(tree.root)
                parent ← None
                node ← tree.root
    
    WHILE node and node.data != target
        parent ← node
        IF target < node.data
            node ← node.left
        ELSE IF target > node.data
            node ← node.right

    IF node IS None OR node.data != target //CASE 1: Target not found
        RETURN False //for info only (we could not find it)
    ELSE IF node.left IS None AND node.right IS None //CASE 2: Target has no children
        IF target < parent.data
            parent.left ← None
        ELSE
            parent.right ← None
        RETURN True //info only
    
    ELSE IF node.left AND node.right IS None //CASE 3: Target has left child only
        IF target < parent.data
            parent.left ← node.left
        ELSE
            parent.right ← node.left
        RETURN True //info only

    NOT IMPLEMENTED //CASE 4: Target has right child only

    ELSE //CASE 5: Target has left and right children
        IF_LEFT_AND_RIGHT(node)

IF_LEFT_AND_RIGHT(node) //called if delete node whether root or otherwise
    delNodeParent ← node //has left and right children
    delNode = node.right

    WHILE delNode.left
        delNodeParent ← delNode
        delNode ← delNode.left

    node.data ← delNode.data

    IF delNode.right
        IF delNodeParent.data > delNode.data
            delNodeParent.left ← delNode.right
        ELSE
            delNodeParent.right ← delNode.right

    ELSE
        IF delNode.data < delNodeParent.data
            delNodeParent.left ← None
        ELSE
            delNodeParent.right ← None

Author: Annija Balode

Algorithm: BST Delete Method
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


    def _remove(self, target):
        # If there is no binary tree..
        if self.root is None:
            # Return False.
            print(False)
            return False
        # Else if the the value at the root of the tree is the target..
        elif self.root.data == target: #if tree root is target
            # If the value on the left and right of the root value is None..
            if self.root.left is None and tree.root.right is None:
                # Set root to None.
                self.root = None
            # If there is a value on the left and None on the right..
            elif self.root.left and tree.root.right is None:
                # Set the root value to the value on the left.
                self.root = tree.root.left
            # If there is a value on the right and None on the left..
            elif self.root.left is None and tree.root.right:
                # Set the root value to the value on the right.
                self.root = tree.root.right
            # If there is a value on both the left and right..
            elif self.root.left and tree.root.right:
                # Call the recursive function using the root value.
                self._if_left_and_right(self.root)
        
        # Set parent to None.
        parent = None
        # Set node to the root value.
        node = self.root
        
        # While the value of the node is not equal to the target.
        while node and node.data != target:
            # Set the parent to the value of node.
            parent = node
            # If target value is less than the value of node..
            if target < node.data:
                # Set node to the value on the left of node.
                node = node.left
            # If the target value is greater than the value of node..
            elif target > node.data:
                # Set node to the value on the right of node.
                node = node.right

        # Case 1: If the target is not found..
        if node is None or node.data != target:
            # Return False and print out "Not Found".
            print("Not found")
            return False

        # Case 2:If the target has no children..
        elif node.left is None and node.right is None:
            # If the target value is less than the parent..
            if target < parent.data:
                # Set the value on the left of the parent to None.
                parent.left = None
            # Else..
            else:
                # Set the value on the right of the parent to None.
                parent.right = None
            #Return True
            print(True)
            return True
        
        # Case 3: If the target has a left child only..
        elif node.left and node.right is None:
            # If the target is less than the parent..
            if target < parent.data:
                # Set the left of the parent to the left of the node.
                parent.left = node.left
            # Else..
            else:
                # Set the right of the parent to the left of the node.
                parent.right = node.left
            # Return True.
            print(True)
            return True

        # Case 4: Target has a right child only.
        elif node.left is None and node.right:
            # If target is greater than the parent..
            if target > parent.data:
                # Set the right of the parent to the right of the node.
                parent.right = node.right
            # Else..
            else:
                # Set the left of the parent to the right of the node.
                parent.left = node.right
            # Return True
            print(True)
            return True
        
        # Case 5: Target has both left and right children.
        else:
            # Call another method using the value of the node.
           self._if_left_and_right(node)

    # Called whether root or has left and right children.
    def _if_left_and_right(self,node):
        # set delNodeParent to the node.
        delNodeParent = node 
        # set delNode to the value on the right of node.
        delNode = node.right

        # While true..
        while delNode.left:
            # Set delNodeParent to delNode.
            delNodeParent = delNode
            # Set delNode to the value on the left of delNode.
            delNode = delNode.left
        
        # Set node to the value of delNode.
        node.data = delNode.data

        if delNode.right:
            # If delNodeParent is less than delNode..
            if delNodeParent.data < delNode.data:
                # Set the value on the left of delNodeParent to the value on the right of delNode.
                delNodeParent.left = delNode.right
            else:
                # Set the value on the right of delNodeParent to the value on the right of delNode.
                delNodeParent.right = delNode.right
        
        else:
            # If delNode is less than delNodeParent..
            if delNode.data < delNodeParent.data:
                # Set the value on the left of delNodeParent to None.
                delNodeParent.left = None
            else:
                # Set the value on the right of delNodeParent to None.
                delNodeParent.right = None

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
bst._remove(6)
bst.display(bst.root)
