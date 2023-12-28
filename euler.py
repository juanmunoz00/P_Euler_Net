from datetime import datetime
import math

class EulerNet:
  def SumOfMultiplesOf3And5(self, n):
    nSum = 0
    for i in range(n):
      if i % 3 == 0 or i % 5 == 0:
        nSum += i
    return nSum