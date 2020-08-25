def verifica_numero2():
	num = int(input())
	while (num < 1 or num > 50):
		num = int(input("Número fora de intervalo, digite novamente:"))
	print("Número Aceito")

def verifica_numero():
	num = int(input())
	while not (num >= 1 and num <= 50):
		num = int(input("Número fora de intervalo, digite novamente:"))
	print("Número Aceito")

verifica_numero()
verifica_numero2()