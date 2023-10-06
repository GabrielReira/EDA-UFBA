# Definindo o algoritmo da pilha
class Elemento:
  def __init__(self):
    self.valor = 0
    self.prox = None

topo = None

def empilhar(valor):
  global topo
  novo = Elemento()
  novo.valor = valor
  novo.prox = topo
  topo = novo
  return topo

def desempilhar():
  global topo
  if (topo != None):
    aux = topo
    valor_desempilhado = aux.valor
    topo = topo.prox
    del(aux)
    return valor_desempilhado
  else:
    print("Pilha vazia.")

# Lista não ordenada de 20 posições com alocação sequencial
lista = [14,7,21,28,35,70,77,49,42,91,637,84,63,441,140,147,133,126,56,98]

# Algoritmo para inverter a ordem dos valores da lista
def inverter(lista):
  global topo
  lista_invertida = [0] * 20
  for i in range(20):
    empilhar(lista[i])
  for i in range(20):
    lista_invertida[i] = desempilhar()
  return lista_invertida

# Complexidade: O(n)


# Para testar
print(lista)
print(inverter(lista))
