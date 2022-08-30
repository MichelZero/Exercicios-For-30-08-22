# autores
# Leandro
# Michel

# data: 30/08/2022

# 1 – Imprima de 1 a 9.

# range(parada)
# range(inicio, parada)
# range(inicio, parada, passo)

inicio = 1
parada = 9

######   1   #######
print("###  1  ###")
for i in range(parada + 1):
  print(f"i[{i}] -> {i}")


######   2   #######
print("###  2  ###")
for i in range(inicio, parada + 1):
  print(f"i[{i}] --> {i}")
  
###   3   ###
inicio = 9
parada = 0
passo = -1

for i in range(inicio, parada, passo):
  print(f"valor[{i}] = {i}")
