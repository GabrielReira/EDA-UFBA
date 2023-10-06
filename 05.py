# Criando a lista "vazia"
lista = [999] * 15

# Algoritmos da lista ordenada
def buscar(valor):
  i = 0
  while (i < 14 and lista[i] < valor):
    i = i + 1
  return i

def incluir(valor):
  indice = buscar(valor)
  if (lista[indice] != valor):
    for i in range(14, indice, -1):
      lista[i] = lista[i-1]
    lista[indice] = valor
  else:
    print("Valor existente na lista.")
  return lista

def excluir(valor):
  indice = buscar(valor)
  if (lista[indice] == valor):
    for i in range(indice, 14):
      lista[i] = lista[i+1]
  else:
    print("Valor não existente na lista.")
  return lista

# Realizando as operações
print(incluir(10))
print(incluir(20))
print(incluir(25))
print(incluir(15))
print(incluir(5))
print(incluir(30))
print(excluir(20))
print(excluir(10))
print(incluir(12))
print(incluir(8))
print(incluir(18))
