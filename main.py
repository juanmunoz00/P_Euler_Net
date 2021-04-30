"""
Solving https://projecteuler.net/archives

"""
##import os
##import sys
##from os import system, name

##from alive_progress import alive_bar
##from progress.bar import ShadyBar

##import re

sol = 2 ##Select solution to display

##Even Fibonacci numbers
def Sol_02():
  lim = 4000001

  n1 = 1
  n2 = 2
  m = n1 + n2
  fibonacciEvens = []
  i = 1
  ##Adding first known evens in Fibonacci sequence
  fibonacciEvens.append(n1)
  fibonacciEvens.append(m)
  while i < lim:

    n1 = n2
    n2 = m
    m = n1 + n2
    ##print("Is Even: " + str(m % 2))
    if ( (m % 2 == 1) ): fibonacciEvens.append(m)
    ##print(str(n1))
    i += 1
    if( i == 1000000 ): print("hit one million")
    elif( i == 2000000 ): print("hit two million")
    elif( i == 3000000 ): print("hit three million")
    elif( i == 3999999 ): print("hit four million")

  print(fibonacciEvens)
  suma = sum(fibonacciEvens)
  print(str(suma))

##Multiples of 3 and 5
def Sol_01():
  sum = 0
  for n in range(1000):
    print(str(n))
    if ( (n % 3) == 0 ): 
      sum = sum + n
      print("Mult 3")
    elif ( (n % 5) == 0 ): 
      sum = sum + n
      print("Mult 5")

  print(str(sum))

if( sol == 2 ): Sol_02()
if( sol == 1 ): Sol_01()