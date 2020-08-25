import math

def distância():
  import math
  print("Vamos calcular a distância!")
  xa = int(input("XA:"))
  xb = int(input("XB:"))
  ya = int(input("YA:"))
  yb = int(input("YB:"))

  i1 = ((xa - xb) ** 2) + ((ya - yb) ** 2)
  i2 = math.sqrt(i1)

  print("Raiz de:", i1)
  print("A distância é:", "{0:.2f}".format(i2))

  x = int(input("\nDigite < 1 > pra calcular outro ou < 0 > para sair!\n"))

  if x == 1:
    distância()

def medio():
  print("Vamos calcular o ponto médio!")
  xa = int(input("XA:"))
  xb = int(input("XB:"))
  ya = int(input("YA:"))
  yb = int(input("YB:"))

  x = (xa + xb) / 2
  y = (ya + yb) / 2

  print("M:", x, ",", y)

  x = int(input("\nDigite < 1 > pra calcular outro ou < 0 > para sair!\n"))

  if x == 1:
    medio()

num1 = int(input("\nPara Distância digite < 1 > e para Médio digite < 2 >\n"))

if num1 == 2:
  medio()
else:
  distância()