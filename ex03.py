# autores
# Leandro
# Michel

# data: 30/08/2022

# 3 - Faça um algoritmo que receba dez números 
# inteiros do usuário e exiba qual o maior número 
# informado.

# valore inicial
maior = -1000

# processamento
for i in range(10):
  numero = int(input(f"informe o valor[{i+1}]: "))
  if maior <= numero:
    maior = numero
    
# saída
print(f"o maior número informado foi {maior}")
print("fim do programa.")