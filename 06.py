# Classe elemento que guarda o próximo e o anterior
class Elemento:
  def __init__(self):
    self.valor = 0
    self.prox = None
    self.ant = None

# Número de elementos na lista
num_elem = 0

# Elemento da extremidade esquerda e direita
elem_esq = None
elem_dir = None

# Algoritmo de inclusão
def incluir(extremidade, valor):
  global elem_esq, elem_dir, num_elem

  novo = Elemento()
  novo.valor = valor
  if (num_elem == 0):
    novo.prox = None
    novo.ant = None
    elem_esq = novo
    elem_dir = novo
  else:
    if (extremidade == "esquerda"):
      elem_esq.ant = novo
      novo.prox = elem_esq
      elem_esq = novo
      novo.ant = None
    elif (extremidade == "direita"):
      novo.ant = elem_dir
      novo.prox = None
      elem_dir.prox = novo
      elem_dir = novo

  num_elem = num_elem + 1

def excluir(extremidade):
  global elem_esq, elem_dir, num_elem

  elem_excluido = None
  if (num_elem == 0):
    print("Lista vazia.")
  else:
    if (extremidade == "esquerda"):
      elem_excluido = elem_esq.valor
      aux = elem_esq
      elem_esq = elem_esq.prox
      elem_esq.ant = None
      del(aux)
    elif (extremidade == "direita"):
      elem_excluido = elem_dir.valor
      aux = elem_dir
      elem_dir = elem_dir.ant
      elem_dir.prox = None
      del(aux)
  
  num_elem = num_elem - 1
  return elem_excluido

# Complexidade: O(1)
