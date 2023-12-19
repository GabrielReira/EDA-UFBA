# Classe Nó que será utilizada para Árvore Binária
class No:
  def __init__(self):
    self.valor = None
    self.esq = None
    self.dir = None
    self.pai = None
raiz = None 


# Classe e funções que serão utilizadas na Pilha Encadeada
class Elemento:
  def __init__(self):
    self.no = None
    self.prox = None
topo = None

def empilhar(no):
  global topo
  novo = Elemento()
  novo.no = no
  novo.prox = topo
  topo = novo
  return topo

def desempilhar():
  global topo
  if (topo != None):
    aux = topo
    topo = topo.prox
    return aux


# Programa principal
def main():
  escolha = -1
  while (escolha != 5):
    print("\nEscolha uma das opções do menu abaixo.")
    print("""
      1 - Inclusão
      2 - Exclusão
      3 - Caminhamento pré-ordem
      4 - Mostrar a árvore
      5 - Fim
    """)
    escolha = int(input("Sua escolha: "))

    if (escolha == 1):
      chave = int(input("\nDigite o valor que você deseja incluir na árvore: "))
      inclusao(chave)
    elif (escolha == 2):
      chave = int(input("\nDigite o valor que você deseja excluir da árvore: "))
      exclusao(chave)
    elif (escolha == 3):
      print("\nCaminhamento pré-ordem da árvore binária:")
      pre_ordem(raiz)
    elif (escolha == 4):
      print("\nExibindo a árvore binária:")
      mostrar_arvore(raiz)
    elif (escolha != 5):
      print("Opcão inválida.")

def busca(pont, chave):
  if (pont == None):
    f = 0
    pai = None
  elif (chave == pont.valor):
    f = 1
    pai = pont.pai
  elif (chave < pont.valor):
    if (pont.esq == None):
      f = 2
      pai = pont.pai
    else:
      pont = pont.esq
      pont, pai, f = busca(pont, chave)
  else:
    if (pont.dir == None):
      f = 3
      pai = pont.pai
    else:
      pont = pont.dir
      pont, pai, f = busca(pont, chave)
  
  return pont, pai, f

def inclusao(chave):
  global raiz
  pont = raiz
  pont, pai, f = busca(pont, chave)
  if (f == 1):
    print("Valor já existe na árvore binária.")
  else:
    novo = No()
    novo.valor = chave
    if (f == 0):
      raiz = novo
    elif (f == 2):
      pont.esq = novo
      novo.pai = pont
    else:
      pont.dir = novo
      novo.pai = pont

def exclusao(chave):
  global raiz
  pont, pai, f = busca(raiz, chave)
  if (f == 0):
    print("A árvore binária está vazia.")
  elif (f == 1):
    if (pont.esq == None):
      if (pont == raiz):
        raiz = raiz.dir
      elif (pont == pai.esq): 
        pai.esq = pont.dir
      else:
        pai.dir = pont.dir
    elif (pont.dir == None):
      if (pont == raiz):
        raiz = raiz.esq
      elif (pont == pai.esq):
        pai.esq = pont.esq
      else:
        pai.dir = pont.esq
    else:
      pont_aux = pont.dir
      pai_aux = pont
      while (pont_aux.esq != None):
        pai_aux = pont_aux
        pont_aux = pont_aux.esq
      if (pai_aux != pont):
        pai_aux.esq = pont_aux.dir
        pont_aux.dir = pont.dir
      pont_aux.esq = pont.esq
      if (pont == raiz):
        raiz = pont_aux
      elif (pai.esq == pont):
        pai.esq = pont_aux
      else:
        pai.dir = pont_aux
    del(pont)
  else:
    print("Valor não existe na árvore binária.")

def pre_ordem(pont):
  global raiz, topo
  if (raiz == None):
    print("A árvore binária está vazia.")
  else:
    while (topo != None or pont != None):
      while (pont != None):
        print(pont.valor)
        empilhar(pont)
        pont = pont.esq
      if (topo != None):
        pont = desempilhar().no
        pont = pont.dir

def mostrar_arvore(pont, level=0):
  global raiz
  if (raiz == None):
    print("A árvore binária está vazia.")
  elif (pont != None):
    mostrar_arvore(pont.dir, level + 1)
    print(" " * 5 * level, "--", pont.valor)
    mostrar_arvore(pont.esq, level + 1)


# Executar o programa
if __name__ == "__main__":
  main()
