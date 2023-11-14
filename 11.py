def arvores_isomorfas(pont1, pont2):
  if (pont1 == None and pont2 == None):
    return True
  elif (pont1 == None or pont2 == None):
    return False
  elif (pont1.valor != pont2.valor):
    return False
  else:
    return (arvores_isomorfas(pont1.esq, pont2.esq) and arvores_isomorfas(pont1.dir, pont2.dir))
