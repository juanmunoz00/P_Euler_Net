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