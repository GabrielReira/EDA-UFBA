# Número de elementos alocados
n = 6

# Tamanho do vetor
m = 10

# Lista não ordenada
lista = [7,5,1,3,9,4,0,0,0,0]

# Algoritmo
class Elemento():
  def __init__(self):
    self.valor = 0
    self.prox = None
prim = Elemento()

for i in range(0, n):
  elem_lista = lista[i]
  pont = prim.prox
  ant = prim
  while ((pont != None) and (elem_lista > pont.valor)):
    ant = pont
    pont = pont.prox
  novo = Elemento()
  novo.valor = elem_lista
  novo.prox = pont
  ant.prox = novo

# Complexidade: O(n^2)
