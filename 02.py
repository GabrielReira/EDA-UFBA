# Tamanho lista circular
tam = 10

# Criando a lista "vazia"
lista = [0] * tam

# Índices dos elementos das extremidades
fim_esquerda = 5
fim_direita = 4

# Número de elementos na lista
num_elementos = 0

def enfileirar(valor, extremidade):
  global lista, fim_esquerda, fim_direita, num_elementos

  if (num_elementos < tam):
    if (extremidade == "esquerda"):
      fim_esquerda = fim_esquerda - 1
      if (fim_esquerda < 0):
        fim_esquerda = tam -1
      lista[fim_esquerda] = valor
    if (extremidade == "direita"):
      fim_direita = fim_direita + 1
      if (fim_direita >= tam):
        fim_direita = 0
      lista[fim_direita] = valor
    num_elementos = num_elementos + 1
  else:
    print("Overflow")
  print(lista)

# Complexidade: O(1)


# Para testar
enfileirar(14, "esquerda")
enfileirar(14, "esquerda")
enfileirar(14, "direita")
enfileirar(14, "esquerda")
enfileirar(14, "direita")
enfileirar(14, "direita")
enfileirar(14, "direita")
enfileirar(14, "direita")
enfileirar(14, "direita")
enfileirar(14, "direita")
enfileirar(14, "direita")
enfileirar(14, "esquerda")
