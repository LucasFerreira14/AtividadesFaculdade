altura = float(input())
peso = float(input())

imc = peso/(altura * altura)

if imc <= 17.0:
	print(round(imc, 2))
	print("Muito abaixo do peso")
elif imc >= 17.0 and imc < 18.50:
	print(round(imc, 2))
	print("Abaixo do peso")
elif imc >= 18.50 and imc < 25.00:
	print(round(imc, 2))
	print("Peso normal")
elif imc >= 25.0 and imc <30.00:
	print(round(imc, 2))
	print("Acima do peso")
elif imc >= 30.0 and imc < 35.00:
	print(round(imc, 2))
	print("Obesidade grau I")
elif imc >= 35.0 and imc < 40.00:
	print(round(imc, 2))
	print("Obesidade grau II")
else:
	print(round(imc, 2))
	print("Obesidade grau III")