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

      """
      If this node has already a value return. If not, create a new node and insert it to the left of this node.
      """
      if ( value < self.value ):
        #Left
        if ( self.left ):
          self.left.Insert(value)
          return
        
        self.left = BinarySearchTree(value)
        return
        
      # Rigth
      if ( self.right ): 
        self.right.Insert(value)
        return
      self.right = BinarySearchTree(value)
  
    except Exception as e: print(e)

  def Delete(self, value):
    try:
      if self == None:
          return self
      if self.right == None:
          return self.left
      if self.left == None:
          return self.right
      if value < self.value:
          if self.left:
              self.left = self.left.Delete(value)
          return self
      if value > self.value:
          if self.right:
              self.right = self.right.Delete(value)
          return self
      min_larger_node = self.right
      while min_larger_node.left:
          min_larger_node = min_larger_node.left
      self.value = min_larger_node.value
      self.right = self.right.Delete(min_larger_node.value)
      return self

    except Exception as e: print(e)
  
  """
  These Min/Max functions recursively search the tree to find the minimum/maximum value.
  """
  def GetMinValue(self):
    try:
      current = self
  
      while current.left is not None:  
          current = current.left
  
      return current.value
    except Exception as e: print(e)
  
  
  def GetMaxValue(self):
    try:
      current = self
  
      while current.right is not None:  
          current = current.right
  
      return current.value
    except Exception as e: print(e)

  def Exists(self, value):
    try:
      if value == self.value:      
          return True
      
      if value < self.value:      
          if self.left == None:      
              return False      
          return self.left.Exists(value)
      
      if self.right == None:      
          return False      
      return self.right.Exists(value)
      
    except Exception as e: print(e)

  
