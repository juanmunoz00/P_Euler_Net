"""
Solving https://projecteuler.net/archives
"""
sol = 2  ##Select solution to display


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


if (sol == 2): Sol_02(4000001)
if (sol == 1): Sol_01()
