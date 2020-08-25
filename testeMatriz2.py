# FUNÇÕES 

def cria_matriz(pessoa, nota):
  nome = "aluno"
  valor = 0
  resultado = []
  contLinha = 0
  contColuna = 0
  while contLinha < pessoa:
    linha = []
    contColuna = 0
    while contColuna < nota:
      if contColuna == 0:
        linha.append(nome)
      contColuna += 1
      linha.append(valor)
    contLinha += 1
    resultado.append(linha)

  return resultado

def valida_qtd_alunos():
  # VALIDA ALUNOS

  alunos = int(input("Digite a quantidade de alunos: "))
  while alunos < 0:
    alunos = int(input("Digite a quantidade de alunos novamente: "))
  print("Quantidade de alunos aceita!")

  return alunos

def valida_qtd_notas():
  # VALIDA NOTAS

  notas = int(input("Digite a quantidade de notas: "))
  while notas < 0:
     notas = int(input("Digite a quantidade de notas novamente: "))
  print("Quantidade de notas aceita!")

  return notas
  
def define_nome_e_notas(matriz):
  #definir as notas dentro da matriz de cada aluno
  alunos = len(matriz)
  notas = len(matriz[0])
  contLines = 0
  contColuns = 0
  while contLines < alunos:
    contColuns = 0
    while contColuns < notas:
      if contColuns == 0:
        matriz[contLines][contColuns] = input("Digite o nome do aluno: ")
      else:
        matriz[contLines][contColuns] = int(input("Digite a %dº nota:" % (contColuns,)))
      contColuns += 1
    contLines += 1
  
  return matriz

# PROGRAMA PRINCIPAL

alunos = valida_qtd_alunos()
notas = valida_qtd_notas()
matriz = cria_matriz(alunos, notas)
resultado = define_nome_e_notas(matriz)

