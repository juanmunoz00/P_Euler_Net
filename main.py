from euler import EulerNet
from binarysearchtree import BinarySearchTree

Euler = EulerNet()
Tree = BinarySearchTree(None)

BINARY_SEARCH_TREE = 1
SUM_OF_MULTIPLES_3_5 = 0

"""
Create this tree:
        9
      /  \
     4    20
   /  \   /  \
  1   6  15  170
"""
if ( BINARY_SEARCH_TREE == 1 ):
  
  Tree.Insert(9)
  Tree.Insert(4)
  Tree.Insert(6)
  #inserted_node_value = Tree.root.value
  #print(f'Value of the inserted node: {inserted_node_value}')
  #Tree.Insert(20)
  #Tree.Insert(170)
  #Tree.Insert(15)
  #Tree.Insert(1)
  pass

if ( SUM_OF_MULTIPLES_3_5 == 1 ):
  n = 1000
  print(f'Sum Of Multiples Of 3 And 5 of {n} :     {Euler.SumOfMultiplesOf3And5(n)}' )

print(f'Done !!')