longestTerm = 0

def collatz(number):
	global longestTerm
	terms = []
	terms.append(number)
	while number != 1 :
		if number % 2 == 0:
			number = number // 2
			terms.append(number)
		else:
			number = number * 3 + 1
			terms.append(number)
	if len(terms) > longestTerm:
		longestTerm = len(terms)
		print(i)

for i in range(1,1000001):
	collatz(i)



