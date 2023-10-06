# Tamanho das pilhas
m1 = 10
m2 = 5

# Criando o vetor "vazio"
vetor = [0] * (m1+m2)

# Índice do último elemento das pilhas
topo1 = -1
topo2 = m1-1

def empilhar(n_pilha, valor):
  global vetor, topo1, topo2
  if (n_pilha == 1):
    if (topo1 < m1 - 1):
      topo1 = topo1 + 1
      vetor[topo1] = valor
    else:
      print("A pilha 1 está cheia.")
  if (n_pilha == 2):
    if (topo2 < m1 + m2 - 1):
      topo2 = topo2 + 1
      vetor[topo2] = valor
    else:
      print("A pilha 2 está cheia.")
  print(vetor)

def desempilhar(n_pilha):
  global vetor, topo1, topo2
  if (n_pilha == 1):
    if (topo1 >= 0):
      vetor[topo1] = 0
      topo1 = topo1 - 1
    else:
      print("A pilha 1 está vazia.")
  if (n_pilha == 2):
    if (topo2 >= m1):
      vetor[topo2] = 0
      topo2 = topo2 - 1
    else:
      print("A pilha 2 está vazia.")
  print(vetor)

# Complexidade: O(1)


# Para testar
empilhar(1, 14)
desempilhar(2)
empilhar(1, 14)
empilhar(1, 14)
empilhar(1, 14)
empilhar(2, 14)
desempilhar(1)
empilhar(1, 14)
desempilhar(2)
desempilhar(2)
desempilhar(2)
empilhar(2, 14)
empilhar(2, 14)
empilhar(2, 14)
empilhar(2, 14)
empilhar(2, 14)
empilhar(1, 14)
empilhar(1, 14)
empilhar(1, 14)
empilhar(1, 14)
empilhar(1, 14)
empilhar(1, 14)
empilhar(1, 14)
