def pre_ordem(pont):
  if (pont != None):
    print(pont.valor)
    pre_ordem(pont.esq)
    pre_ordem(pont.dir)

def em_ordem(pont):
  if (pont != None):
    em_ordem(pont.esq)
    print(pont.valor)
    em_ordem(pont.dir)

def pos_ordem(pont):
  if (pont != None):
    pos_ordem(pont.esq)
    pos_ordem(pont.dir)
    print(pont.valor)

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
