"""
Credit to: Lane
From: https://blog.boot.dev/computer-science/binary-search-tree-in-python/

On: Dec. 2023
"""
from datetime import datetime
import math
"""
Binary Search Tree
"""
#class Node:
class BinarySearchTree:

  def __init__(self, value):
    #self.root = root
    self.left = None
    self.right = None
    self.value = value

  def Insert(self, value):
    try:
      if ( not self.value ):
        self.value = value
        return

      if ( self.value == value ):
        return
  
      if ( value < self.value ):
        #Left
        """
        If this node has already a value return. If not, create a new node and insert it to the left of this node.
        """
        if ( self.left ):
          self.left.Insert(value)
          return
        else:
          self.left = BinarySearchTree(value)
        # Same logic for rigth node
        if ( self.right ): 
          self.right.Insert(value)
          return
        else:
          self.right = BinarySearchTree(value)        
  
    except Exception as e: print(e)


  
