"""
Solving https://projecteuler.net/archives
"""
prime_nums_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

sol = 3  ##Select solution to display

##Largest prime factor
def Sol_03(num):
  print("Init...")
  original_num = num
  primeNums = []
  residue = num
  pI = 0
  residue_op = 2

  while ( residue_op > 1 ):
    prime = prime_nums_100[pI]
    residue_op = num / prime
    residue = ( (num % prime) == 0 )#isinstance(residue_op, int)
    #print(str(num) + "|" + str(prime) + "(" + str(residue_op) + ")[" + str(num / 1) + "]")

    if( residue ):
      ##Is prime factor
      primeNums.append(prime)##(residue_op)
      num = residue_op
    else:
      pI += 1

  print(primeNums)
  ##Check
  i = 1
  for n in primeNums:
    if ( i == 1 ):
      m = n
    else:
      m = m * n
    
    i += 1
  
  print(str(original_num))
  print(str(m))
  if ( m == original_num):
    print("Lista de primos es óptima")
  else:
    print("Lista de primos no es óptima")


##Even Fibonacci numbers
def Sol_02(lim):
	print('Sol 02 started ...')
	suma = 0
	n1 = 1
	n2 = 2
	m = n1 + n2
	i = 0
	##Adding first known evens in Fibonacci sequence
	while m < lim:  #Aqui es m no i
		if i == 0:
			m = 0
		if i == 1:
			m = 1
		else:
			n2 = n1
			n1 = m
			m = n1 + n2
			##print("Is Even: " + str(m % 2))
		if ((m % 2 == 0)):
			suma += m

		i += 1

	print(str(suma))


##Multiples of 3 and 5
def Sol_01():
	sum = 0
	for n in range(1000):
		print(str(n))
		if ((n % 3) == 0):
			sum = sum + n
			print("Mult 3")
		elif ((n % 5) == 0):
			sum = sum + n
			print("Mult 5")

	print(str(sum))


if (sol == 3): Sol_03(7000000000000) ##600,851,475,143
if (sol == 2): Sol_02(4000001)
if (sol == 1): Sol_01()
