# autores
# Leandro
# Michel

# data: 30/08/2022

# 2 –  Faça programa que calcule o fatorial de um número.

# https://pt.wikipedia.org/wiki/Fatorial
# A função fatorial é normalmente definida por:
# n! = n(n-1)*n(n-2)*...*3*2*1

# calculando de forma interativa com o FOR
valor = int(input("informe um número: "))

# calculando o fatorial do valor informado
fatorial = 1

for i in range(1, valor + 1):
  fatorial = fatorial * i
  
# saída de dados
print(f"o fatorial do valor {valor} = {fatorial}")
print("fim do programa!")