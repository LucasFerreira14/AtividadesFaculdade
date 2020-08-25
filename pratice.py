import math

nome = input("Digite o nome do Aluno:")

contNota = 0
contTrabalho = 0
somaNotas = 0
somaTrabalhos = 0

frequencia = int(input("Digite a Frequência do Aluno:"))
while frequencia < 0 or frequencia > 100:
  frequencia = int(input("Digite a Frequência do Aluno novamente:"))
print("Frequência Aceita")

while contNota < 4:
  print("Digite a", contNota+1,"º Nota:")
  nota = float(input())
  while nota < 0 or nota > 10:
    nota = float(input("Nota Inválida, digite novamente:"))
  print("Notas Aceita!")
  contNota = contNota + 1
  somaNotas = somaNotas + nota
  

while contTrabalho < 2:
  print("Digite a", contTrabalho+1,"º Nota do Trabalho:")
  trabalho = float(input())
  while trabalho < 0 or trabalho > 10:
    trabalho = float(input("Nota do Trabalho Inválido, digite novamente:"))
  contTrabalho = contTrabalho + 1
  somaTrabalhos = somaTrabalhos + trabalho

def mediaNotas(somaNotas):
  media = math.trunc(somaNotas / 4)
  return media

def mediaTrabalhos(somaTrabalhos):
  media = math.trunc(somaTrabalhos / 2)
  return media

mediaNota = mediaNotas(somaNotas)
mediaTrabalho = mediaTrabalhos(somaTrabalhos)

def mediaFinal(mediaNotas, somaTrabalhos):
  media = math.trunc((mediaNota + mediaTrabalho) / 2)
  return media

media_Final = mediaFinal(mediaNotas, mediaTrabalhos)

if media_Final >= 7 and frequencia >= 70.0:
  print("Aluno(a)",nome, "Aprovado!")
elif media_Final >= 5 and frequencia >= 70.0:
  print("Aluno(a)", nome, "Em Recuperação!")
else:
  print("Aluno(a)", nome, "Reprovado!")

input("Pressione <ENTER> para Sair!")







