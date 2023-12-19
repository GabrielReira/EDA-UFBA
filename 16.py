# Tamanho do Heap
n = 10

# Heap de prioridade
heap = [70, 52, 28, 48, 50, 10, 25, 18, 34, 14]

def descer(i, n):
  while (i * 2 <= n):
    j = i * 2
    if (j < n):
      if (heap[j] < heap[j+1]):
        j = j + 1
    if (heap[i] < heap[j]):
      heap[i], heap[j] = heap[j], heap[i]
      i = j
    else:
      i = n + 1
