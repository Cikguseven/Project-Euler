'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the c of the even-valued terms.
'''

a = 1
b = 2
c = 2

while a+b < 4000000:
	a = a + b
	if a % 2 == 0:
		c += a
	b = a + b
	if b % 2 == 0:
		c += b

print(c)
