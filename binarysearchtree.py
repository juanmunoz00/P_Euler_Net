from datetime import datetime
import math
"""
Binary Search Tree
"""
class Node:

  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value


class BinarySearchTree:

  def __init__(self, root=None):
    self.root = root

  def Insert(self, value):
    newNode = Node(value) # Instantiating a new Node
    """
    If the root is None, then the tree is empty so
    add the new node as the root.
    """
    if ( self.root == None ):
      self.root = newNode
      return
      
  def Lookup(self, value):
    pass

  # Remove

"""
Binary Search Tree
"""
