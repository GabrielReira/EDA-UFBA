# Definindo o algoritmo da lista ordenada com nó header
class Elemento:
  def __init__(self):
    self.valor = 0
    self.prox = None

primeiro1 = Elemento()
primeiro2 = Elemento()

def buscar(valor, n_lista):
  if (n_lista == 1):
    anterior = primeiro1
    ponteiro = primeiro1.prox
    while ((ponteiro != None) and (ponteiro.valor < valor)):
      anterior = ponteiro
      ponteiro = ponteiro.prox
    return anterior
  if (n_lista == 2):
    anterior = primeiro2
    ponteiro = primeiro2.prox
    while ((ponteiro != None) and (ponteiro.valor < valor)):
      anterior = ponteiro
      ponteiro = ponteiro.prox
    return anterior

def incluir(valor, n_lista):
  anterior = buscar(valor, n_lista)
  ponteiro = anterior.prox
  if ((ponteiro == None) or (ponteiro.valor != valor)):
    novo = Elemento()
    novo.valor = valor
    novo.prox = ponteiro
    anterior.prox = novo
  else:
    print("Valor já existe na lista.")

# Algoritmo para intercalar as listas
primeiro3 = Elemento()

def intercalar(prim1, prim2):
  pont1 = prim1.prox
  pont2 = prim2.prox
  pont3 = primeiro3
  while ((pont1 != None) and (pont2 != None)):
    if ((pont1.valor < pont2.valor)):
      novo = Elemento()
      novo.valor = pont1.valor
      pont3.prox = novo
      pont3 = novo
      pont1 = pont1.prox
    else:
      novo = Elemento()
      novo.valor = pont2.valor
      pont3.prox = novo
      pont3 = novo
      pont2 = pont2.prox
    print(pont3.valor)

  if (pont1 != None):
    while (pont1 != None):
      novo = Elemento()
      novo.valor = pont1.valor
      pont3.prox = novo
      pont3 = novo
      pont1 = pont1.prox
      print(pont3.valor)
  else:
    while (pont2 != None):
      novo = Elemento()
      novo.valor = pont2.valor
      pont3.prox = novo
      pont3 = novo
      pont2 = pont2.prox
      print(pont3.valor)

# def intercalar(prim1, prim2):
#   pont1 = prim1.prox
#   pont2 = prim2.prox
#   pont3 = primeiro3.prox
#   while ((pont1 != None) or (pont2 != None)):
#     if ((pont1 != None) and (pont2 != None) and (pont1.valor == pont2.valor)):
#       novo = Elemento()
#       novo.valor = pont1.valor
#       pont1 = pont1.prox
#       pont2 = pont2.prox
#     elif ((pont2 == None) or (pont1.valor < pont2.valor)):
#       novo = Elemento()
#       novo.valor = pont1.valor
#       pont1 = pont1.prox
#     elif ((pont1 == None) or (pont1.valor > pont2.valor)):
#       novo = Elemento()
#       novo.valor = pont2.valor
#       pont2 = pont2.prox
#     pont3 = novo
#     print(pont3.valor)


# Para testar
# Lista 1: [1, 2, 7, 14]
incluir(1, 1)
incluir(2, 1)
incluir(7, 1)
incluir(14, 1)
# Lista 2: [2, 3, 5, 9, 12]
incluir(2, 2)
incluir(3, 2)
incluir(5, 2)
incluir(9, 2)
incluir(12, 2)

intercalar(primeiro1, primeiro2)
