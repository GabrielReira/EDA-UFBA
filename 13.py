def rotacao_esquerda(pt):
  ptu = pt.dir
  if (ptu.bal == 1):  # rotação simples
      pt.dir = ptu.esq
      ptu.esq = pt
      pt.bal = 0
      pt = ptu
      pt.bal = 0
  else:  # rotação dupla
      ptv = ptu.esq
      pt.dir = ptv.esq
      ptu.esq = ptv.dir
      ptv.dir = ptu
      ptv.esq = pt
      if (ptv.bal == 1):
          pt.bal = -1
      else:
          pt.bal = 0
      if (ptv.bal == -1):
          ptu.bal = 1
      else:
          ptu.bal = 0
      pt = ptv
      pt.bal = 0
