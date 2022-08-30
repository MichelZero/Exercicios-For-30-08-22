# autores
# Leandro
# Michel

# data: 30/08/2022

# 3 - Faça um algoritmo que receba dez números 
# inteiros do usuário e exiba qual o maior número 
# informado.

# valore inicial
parada = 10
maior = -10000

# processamento
###   1   ###
for i in range(10):
  numero = int(input(f"informe o valor[{i+1}]: "))
  if maior <= numero:
    maior = numero
    
# saída
print(f"o maior número informado foi {maior}")
print("fim do programa.")

###   2   ###
posicao = 0
for i in range(parada):
  valor = int(input(f"informe um número[{i}]: "))
  if maior < valor:
    maior = valor
    posicao = i
    
print(f"entrada[{posicao}] é {maior}")
