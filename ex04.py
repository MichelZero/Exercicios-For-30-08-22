# autores
# Leandro
# Michel

# data: 30/08/2022

# 4 - Elabore um algoritmo que recebe um texto do 
# usuário e informe quantas vogais estão presentes 
# neste texto.

###   1   ###
# entrada
texto = input("Digite uma mensagem: ")
quantidade = 0

# processamento
for i in texto:
  if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
    quantidade +=1
    
# saída
print(f"a quantidade de vogais do texto é {quantidade}")
print("fim do programa")


###   2   ###
quantidade = 0
vogais = {'a', 'e', 'i', 'o', 'u'} # dicionário
# processamento
for i in texto:
  if i in vogais:
    quantidade +=1
    
# saída
print(f"a quantidade de vogais do texto é {quantidade}")
print("fim do programa")