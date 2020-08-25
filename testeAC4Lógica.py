#FUNÇÕES
def le_e_valida(a, b, msg):
  return

def exibe_total(nome, dia, mes, total, descontoPercentual):
  return

def registra_atendimentos(qtd_pessoas):
  cont = 1
  while cont != qtd_pessoas:
    nome = input()
    dia = le_e_valida(a, b, msg)
    mes = le_e_valida(a, b, msg)
    total = float(input())
    descontoPercentual =le_e_valida(a, b, msg)
    exibe_total(nome, dia, mes, total, descontoPercentual)
  return

#PROGRAMA PRINCIPAL
qtd_pessoas = int(input())
registra_atendimentos(qtd_pessoas)