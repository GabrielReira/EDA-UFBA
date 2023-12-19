class No:
  def __init__(self):
      self.valor = None
      self.esq = None
      self.dir = None

def inclusao(pont, chave, h):
  if (pont == None):
    pont = No()
    pont.valor = chave
    h = True
  else:
      if (pont.valor > chave):
        pont.esq, h = inclusao(pont.esq, chave, h)
        if (h == True):
          if (pont.bal == 0):
            pont.bal = -1
          if (pont.bal == -1):
            pont.bal = -2
          if (pont.bal == -2):
            pont = rotacao_direita(pont)
          if (pont.bal == 1):
            pont.bal = 0
            h = False
          if (pont.bal == 2):
            pont.bal = 1
            h = False
      if (pont.valor < chave):
        pont.dir, h = inclusao(pont.dir, chave, h)
        if (h == True):
          if (pont.bal == 0):
            pont.bal = 1
          if (pont.bal == 1):
            pont.bal = 2
          if (pont.bal == 2):
            pont = rotacao_esquerda(pont)
          if (pont.bal == -1):
            pont.bal = 0
            h = False
          if (pont.bal == -2):
            pont.bal = -1
            h = False
      else:
        print("Valor de chave já existe na árvore.")
  return pont, h
