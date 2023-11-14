# Algoritmo 1 - Pré-ordem iterativo
def pre_ordem(pont):
  pilha = [None] * 10
  topo = -1

  while (topo >= 0 or pont != None):
    while (pont != None):
      print(pont.valor)
      topo = topo + 1
      pilha[topo] = pont
      pont = pont.esq
    pont = pilha[topo]
    topo = topo - 1
    pont = pont.dir

# Algoritmo 2 - Em ordem iterativo
def em_ordem(pont):
  pilha = [None] * 10
  topo = -1

  while (topo >= 0 or pont != None):
    while (pont != None):
      topo = topo + 1
      pilha[topo] = pont
      pont = pont.esq
    pont = pilha[topo]
    topo = topo - 1
    print(pont.valor)
    pont = pont.dir

# Algoritmo 3 - Pós-ordem iterativo
def pos_ordem(pont):
  pilha1 = [None] * 10
  pilha2 = [None] * 10
  topo1 = -1
  topo2 = -1

  topo1 = topo1 + 1
  pilha1[topo1] = pont

  while (topo1 >= 0):
    pont = pilha1[topo1]
    topo1 = topo1 - 1
    topo2 = topo2 + 1
    pilha2[topo2] = pont

    if (pont.esq != None):
      topo1 = topo1 + 1
      pilha1[topo1] = pont.esq

    if (pont.dir != None):
      topo1 = topo1 + 1
      pilha1[topo1] = pont.dir

  while topo2 >= 0:
    print(pilha2[topo2].valor)
    topo2 = topo2 - 1


# Para testar
class No:
  def __init__(self):
    self.valor = None
    self.esq = None
    self.dir = None

raiz = No()
raiz.valor = 20
elemento1 = No()
elemento1.valor = 10
raiz.esq = elemento1
elemento2 = No()
elemento2.valor = 5
elemento1.esq = elemento2
elemento3 = No()
elemento3.valor = 40
raiz.dir = elemento3
elemento4 = No()
elemento4.valor = 30
elemento3.esq = elemento4
elemento5 = No()
elemento5.valor = 50
elemento3.dir = elemento5

pre_ordem(raiz)
em_ordem(raiz)
pos_ordem(raiz)
