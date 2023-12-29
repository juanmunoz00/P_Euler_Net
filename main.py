from euler import EulerNet
from binarysearchtree import BinarySearchTree

Euler = EulerNet()
Tree = BinarySearchTree(None)

BINARY_SEARCH_TREE = 1
SUM_OF_MULTIPLES_3_5 = 0

LEFT = 1
RIGHT = 2

"""
Create this tree:
        9
      /  \
     4    20
   /  \   /  \
  1   6  15  170
"""
if ( BINARY_SEARCH_TREE == 1 ):

  numbers = [9,4,6,20,170,15,1]

  for n in numbers:
    Tree.Insert(n)
    print(f' {n} exists? {Tree.Exists(n)} ')
  
  #print(f' Min value: {Tree.GetMinValue()} ')
  #print(f' Max value: {Tree.GetMaxValue()} ')
  
  d = 15
  print(f' {d} exists? {Tree.Exists(d)} ')
  Tree.Delete(d)
  print(f' {d} exists? {Tree.Exists(d)} ')


if ( SUM_OF_MULTIPLES_3_5 == 1 ):
  n = 1000
  print(f'Sum Of Multiples Of 3 And 5 of {n} :     {Euler.SumOfMultiplesOf3And5(n)}' )

print(f'\nDone !!')