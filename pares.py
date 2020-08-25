def exerc1pares():
	n = int(input())
	i = 0 

	while i <= n:
		if (i % 2) == 0:
			print(i)
		i = i + 1

def exerc2pares():
	n = int(input())
	i = 0 

	while i <= n:
		print(i)
		i = i + 2

exerc1pares()
exerc2pares()