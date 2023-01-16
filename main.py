from random import randint
from random import random
import random
import sys
import time
import numpy as np
import os
import pathlib

sys.setrecursionlimit(1000000)

# Mergesort
def mergeSort(lista):
    if len(lista) > 1:
        meio = len(lista)//2
        esq = lista[:meio]
        dir = lista[meio:]

        mergeSort(esq)
        mergeSort(dir)

        i=0
        j=0
        k=0

        while i < len(esq) and j < len(dir):
            if esq[i] < dir[j]:
                lista[k] = esq[i]
                i=i+1
            else:
                lista[k] = dir[j]
                j=j+1
            k=k+1

        while i < len(esq):
            lista[k] = esq[i]
            i=i+1
            k=k+1

        while j < len(dir):
            lista[k] = dir[j]
            j=j+1
            k=k+1

# QuickSort com Pivo Aleatorio
def quicksortPivoAleatorio(vetor, inicio , fim):
    if(inicio < fim):
        pivoindex = particaorand(vetor,inicio, fim)
        quicksortPivoAleatorio(vetor , inicio , pivoindex-1)
        quicksortPivoAleatorio(vetor, pivoindex + 1, fim)
 
def particaorand(vetor , inicio, fim):
    randpivo = random.randrange(inicio, fim)
 
    vetor[inicio], vetor[randpivo] = \
        vetor[randpivo], vetor[inicio]
    return particaoPivoAleatorio(vetor, inicio, fim)

def particaoPivoAleatorio(vetor,inicio,fim):
    pivo = inicio # pivo
     
    i = inicio + 1
     
    for j in range(inicio + 1, fim + 1):
        if vetor[j] <= vetor[pivo]:
            vetor[i] , vetor[j] = vetor[j] , vetor[i]
            i = i + 1
    vetor[pivo] , vetor[i - 1] =\
            vetor[i - 1] , vetor[pivo]
    pivo = i - 1
    return (pivo)

# QuickSort com pivo Medio

def median_of_three(L, low, high):
    mid = (low+high-1)//2
    a = L[low]
    b = L[mid]
    c = L[high-1]
    if a <= b <= c:
        return b, mid
    if c <= b <= a:
        return b, mid
    if a <= c <= b:
        return c, high-1
    if b <= c <= a:
        return c, high-1
    return a, low


def quickSortPivoMedio(L, ascending=True):
    quicksorthelp(L, 0, len(L), ascending)


def quicksorthelp(L, low, high, ascending=True):
    result = 0
    if low < high:
        pivot_location, result = Partition(L, low, high, ascending)
        result += quicksorthelp(L, low, pivot_location, ascending)
        result += quicksorthelp(L, pivot_location + 1, high, ascending)
    return result


def Partition(L, low, high, ascending=True):
    # print('Quicksort, Parameter L:')
    # print(L)
    result = 0
    pivot, pidx = median_of_three(L, low, high)
    L[low], L[pidx] = L[pidx], L[low]
    i = low + 1
    for j in range(low+1, high, 1):
        result += 1
        if (ascending and L[j] < pivot) or (not ascending and L[j] > pivot):
            L[i], L[j] = L[j], L[i]
            i += 1
    L[low], L[i-1] = L[i-1], L[low]
    return i - 1, result

# liste1 = list([3.14159, 1./127, 2.718, 1.618, -23., 3.14159])


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def aux_quicksort_pivo_medio(lista):
    quickSortPivoMedio(lista, True)


# QuickSort com funcao AchaPivo
def achaPivo(lista, esq, dir):
  pos = esq + 1
  pivo = 0

  while pos <= dir:
    if lista[pos] >= lista[pos - 1]:
      pos=pos+1
    else:
      pivo = pos
      break
  
  return pivo

def particaoAchaPivo(lista, esq, dir):
    pivo = lista[esq]
    i = esq
    j = dir

    while i <= j:
        while lista[i] <= pivo:
            i += 1
            if i == dir:
                break
        while pivo <= lista[j]:
            j -= 1
            if j == esq:
                break
        if i >= j:
            break
        lista[i], lista[j] = lista[j], lista[i]

    lista[esq], lista[j] = lista[j], lista[esq]

    return j

def quickSortAchaPivo(lista, esq, dir): 
    if esq >= dir:
        return

    pivo = achaPivo(lista, esq, dir)
    if(pivo != 0):
        lista[pivo], lista[esq] = lista[esq], lista[pivo]
        p = particaoAchaPivo(lista, esq, dir)
        quickSortAchaPivo(lista, esq, p-1)
        quickSortAchaPivo(lista, p+1, dir)

# HeapSort
def heapify(arr, n, i):
	largest = i
	l = 2 * i + 1
	r = 2 * i + 2

	if l < n and arr[i] < arr[l]:
		largest = l

	if r < n and arr[largest] < arr[r]:
		largest = r

	if largest != i:
		(arr[i], arr[largest]) = (arr[largest], arr[i])

		heapify(arr, n, largest)


def heapSort(arr):
	n = len(arr)

	for i in range(n // 2 - 1, -1, -1):
		heapify(arr, n, i)

	for i in range(n - 1, 0, -1):
		(arr[i], arr[0]) = (arr[0], arr[i])
		heapify(arr, i, 0)


# Caminho onde está armazenado o arquivo no computador
path = pathlib.Path(__file__).parent.resolve()

for n_execucao in range(1, 11):
    print(n_execucao)
    
    ################################################################################
    ################################# TAMANHO 100 ##################################
    ################################################################################

    pos1, pos2  = 1,50
    

    lista = range(1,101)
    lista

    arr=[]

    n = len(lista)
    for i in range(n):
        arr.append(lista[i])

    List = arr
    for x in range(10):
        pos1 = randint(1, 100)
        pos2 = randint(1, 100)
        while (pos1 == pos2):
            pos2 = randint(1, 100)
        resultado_vetor_100 = swapPositions(List, pos1-1, pos2-1)
        
        
    # Criando pasta caso ela não exista
    caminhoPasta = f'{path}/{n_execucao}_pouco_desordenado'
    if (not os.path.exists(caminhoPasta)):
        os.mkdir(caminhoPasta)

    arquivo_tamanho_100 = open(
        f'{caminhoPasta}/tamanho100_{n_execucao}.txt', "w")

    arquivo_tamanho_100.write("## Algortimos de Ordenacao - Lista de tamanho 100 - Caso pouco desordenado (10%) ## \n\n")

    # MERGE SORT
    arquivo_tamanho_100.write("MERGE SORT \n")
    ini = time.time()
    resultado_merge_100 = mergeSort(resultado_vetor_100)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_100.write("Tempo Medio: "+str(tempoMedio)+"s \n\n")
    # print(resultado_vetor_100)

    # QUICK SORT PIVO ALEATORIO
    arquivo_tamanho_100.write("Quick Sort Aleatorio: \n")
    ini = time.time()
    resultado_quick_100 = quicksortPivoAleatorio(resultado_vetor_100, 0, len(resultado_vetor_100) - 1)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_100.write("Tempo Medio: "+str(tempoMedio)+"s \n\n")
    # print(resultado_vetor_100)

    #QUICK SORT PIVO MEDIO
    arquivo_tamanho_100.write("Quick Sort Pivo Medio: \n")
    ini = time.time()
    quickSortPivoMedio(resultado_vetor_100, True)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_100.write("Tempo Medio: "+str(tempoMedio)+"s \n\n")
    # print(resultado_vetor_100)

    #QUICK SORT ACHA PIVO
    arquivo_tamanho_100.write("Quick Sort Acha Pivo: \n")
    ini = time.time()
    quickSortAchaPivo(resultado_vetor_100, 0, len(resultado_vetor_100) - 1)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_100.write("Tempo Medio: "+str(tempoMedio)+"s \n\n")
    # print(resultado_vetor_100)

    #HEAP SORT
    arquivo_tamanho_100.write("Heap Sort \n")
    ini = time.time()
    heapSort(resultado_vetor_100)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_100.write("Tempo Medio: "+str(tempoMedio)+"s")
    # print(resultado_vetor_100)

    arquivo_tamanho_100.close()
    
    ################################################################################
    ################################# TAMANHO 1000 ##################################
    ################################################################################

    pos1, pos2  = 1,50
    

    lista = range(1,1001)
    lista

    arr=[]

    n = len(lista)
    for i in range(n):
        arr.append(lista[i])

    List = arr
    for x in range(100):
        pos1 = randint(1, 1000)
        pos2 = randint(1, 1000)
        while (pos1 == pos2):
            pos2 = randint(1, 1000)
        resultado_vetor_1000 = swapPositions(List, pos1-1, pos2-1)

    # Criando pasta caso ela não exista
    caminhoPasta = f'{path}/{n_execucao}_pouco_desordenado'
    if (not os.path.exists(caminhoPasta)):
        os.mkdir(caminhoPasta)

    arquivo_tamanho_1000 = open(
        f'{caminhoPasta}/tamanho1000_{n_execucao}.txt', "w")

    arquivo_tamanho_1000.write("## Algortimos de Ordenacao - Lista de tamanho 1000 - Caso pouco desordenado (10%) ## \n\n")

    # MERGE SORT
    arquivo_tamanho_1000.write("MERGE SORT \n")
    ini = time.time()
    resultado_merge_1000 = mergeSort(resultado_vetor_1000)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_1000.write("Tempo Medio: "+str(tempoMedio)+"s \n\n")
    # print(resultado_vetor_1000)

    # QUICK SORT PIVO ALEATORIO
    arquivo_tamanho_1000.write("Quick Sort Aleatorio: \n")
    ini = time.time()
    resultado_quick_1000 = quicksortPivoAleatorio(resultado_vetor_1000, 0, len(resultado_vetor_1000) - 1)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_1000.write("Tempo Medio: "+str(tempoMedio)+"s \n\n")
    # print(resultado_vetor_1000)

    #QUICK SORT PIVO MEDIO
    arquivo_tamanho_1000.write("Quick Sort Pivo Medio: \n")
    ini = time.time()
    quickSortPivoMedio(resultado_vetor_1000, True)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_1000.write("Tempo Medio: "+str(tempoMedio)+"s \n\n")
    # print(resultado_vetor_1000)

    #QUICK SORT ACHA PIVO
    arquivo_tamanho_1000.write("Quick Sort Acha Pivo: \n")
    ini = time.time()
    quickSortAchaPivo(resultado_vetor_1000, 0, len(resultado_vetor_1000) - 1)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_1000.write("Tempo Medio: "+str(tempoMedio)+"s \n\n")
    # print(resultado_vetor_1000)

    #HEAP SORT
    arquivo_tamanho_1000.write("Heap Sort \n")
    ini = time.time()
    heapSort(resultado_vetor_1000)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_1000.write("Tempo Medio: "+str(tempoMedio)+"s")
    # print(resultado_vetor_1000)

    arquivo_tamanho_1000.close()
    
    ################################################################################
    ################################# TAMANHO 5000 ##################################
    ################################################################################

    pos1, pos2  = 1,50
    

    lista = range(1,5001)
    lista

    arr=[]

    n = len(lista)
    for i in range(n):
        arr.append(lista[i])

    List = arr
    for x in range(500):
        pos1 = randint(1, 5000)
        pos2 = randint(1, 5000)
        while (pos1 == pos2):
            pos2 = randint(1, 5000)
        resultado_vetor_5000 = swapPositions(List, pos1-1, pos2-1)

    # Criando pasta caso ela não exista
    caminhoPasta = f'{path}/{n_execucao}_pouco_desordenado'
    if (not os.path.exists(caminhoPasta)):
        os.mkdir(caminhoPasta)

    arquivo_tamanho_5000 = open(
        f'{caminhoPasta}/tamanho5000_{n_execucao}.txt', "w")

    arquivo_tamanho_5000.write("## Algortimos de Ordenacao - Lista de tamanho 5000 - Caso pouco desordenado (10%) ## \n\n")

    # MERGE SORT
    arquivo_tamanho_5000.write("MERGE SORT \n")
    ini = time.time()
    resultado_merge_5000 = mergeSort(resultado_vetor_5000)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_5000.write("Tempo Medio: "+str(tempoMedio)+"s \n\n")
    # print(resultado_vetor_5000)

    # QUICK SORT PIVO ALEATORIO
    arquivo_tamanho_5000.write("Quick Sort Aleatorio: \n")
    ini = time.time()
    resultado_quick_5000 = quicksortPivoAleatorio(resultado_vetor_5000, 0, len(resultado_vetor_5000) - 1)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_5000.write("Tempo Medio: "+str(tempoMedio)+"s \n\n")
    # print(resultado_vetor_5000)

    #QUICK SORT PIVO MEDIO
    arquivo_tamanho_5000.write("Quick Sort Pivo Medio: \n")
    ini = time.time()
    quickSortPivoMedio(resultado_vetor_5000, True)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_5000.write("Tempo Medio: "+str(tempoMedio)+"s \n\n")
    # print(resultado_vetor_5000)

    #QUICK SORT ACHA PIVO
    arquivo_tamanho_5000.write("Quick Sort Acha Pivo: \n")
    ini = time.time()
    quickSortAchaPivo(resultado_vetor_5000, 0, len(resultado_vetor_5000) - 1)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_5000.write("Tempo Medio: "+str(tempoMedio)+"s \n\n")
    # print(resultado_vetor_5000)

    #HEAP SORT
    arquivo_tamanho_5000.write("Heap Sort \n")
    ini = time.time()
    heapSort(resultado_vetor_5000)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_5000.write("Tempo Medio: "+str(tempoMedio)+"s")
    # print(resultado_vetor_5000)

    arquivo_tamanho_5000.close()
    
    ################################################################################
    ################################# TAMANHO 10000 ##################################
    ################################################################################

    pos1, pos2  = 1,50
    

    lista = range(1,10001)
    lista

    arr=[]

    n = len(lista)
    for i in range(n):
        arr.append(lista[i])

    List = arr
    for x in range(1000):
        pos1 = randint(1, 10000)
        pos2 = randint(1, 10000)
        while (pos1 == pos2):
            pos2 = randint(1, 10000)
        resultado_vetor_10000 = swapPositions(List, pos1-1, pos2-1)

    # Criando pasta caso ela não exista
    caminhoPasta = f'{path}/{n_execucao}_pouco_desordenado'
    if (not os.path.exists(caminhoPasta)):
        os.mkdir(caminhoPasta)

    arquivo_tamanho_10000 = open(
        f'{caminhoPasta}/tamanho10000_{n_execucao}.txt', "w")

    arquivo_tamanho_10000.write("## Algortimos de Ordenacao - Lista de tamanho 10000 - Caso pouco desordenado (10%) ## \n\n")

    # MERGE SORT
    arquivo_tamanho_10000.write("MERGE SORT \n")
    ini = time.time()
    resultado_merge_10000 = mergeSort(resultado_vetor_10000)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_10000.write("Tempo Medio: "+str(tempoMedio)+"s \n\n")
    # print(resultado_vetor_10000)

    # QUICK SORT PIVO ALEATORIO
    arquivo_tamanho_10000.write("Quick Sort Aleatorio: \n")
    ini = time.time()
    resultado_quick_10000 = quicksortPivoAleatorio(resultado_vetor_10000, 0, len(resultado_vetor_10000) - 1)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_10000.write("Tempo Medio: "+str(tempoMedio)+"s \n\n")
    # print(resultado_vetor_10000)

    #QUICK SORT PIVO MEDIO
    arquivo_tamanho_10000.write("Quick Sort Pivo Medio: \n")
    ini = time.time()
    quickSortPivoMedio(resultado_vetor_10000, True)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_10000.write("Tempo Medio: "+str(tempoMedio)+"s \n\n")
    # print(resultado_vetor_10000)

    # QUICK SORT ACHA PIVO
    arquivo_tamanho_10000.write("Quick Sort Acha Pivo: \n")
    ini = time.time()
    quickSortAchaPivo(resultado_vetor_10000, 0, len(resultado_vetor_10000) - 1)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_10000.write("Tempo Medio: "+str(tempoMedio)+"s \n\n")
    # print(resultado_vetor_10000)

    #HEAP SORT
    arquivo_tamanho_10000.write("Heap Sort \n")
    ini = time.time()
    heapSort(resultado_vetor_10000)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_10000.write("Tempo Medio: "+str(tempoMedio)+"s")
    # print(resultado_vetor_10000)

    arquivo_tamanho_10000.close()


    ################################################################################
    ################################# TAMANHO 50000 ##################################
    ################################################################################

    pos1, pos2  = 1,50
    

    lista = range(1,50001)
    lista

    arr=[]

    n = len(lista)
    for i in range(n):
        arr.append(lista[i])

    List = arr
    for x in range(5000):
        pos1 = randint(1, 50000)
        pos2 = randint(1, 50000)
        while (pos1 == pos2):
            pos2 = randint(1, 50000)
        resultado_vetor_50000 = swapPositions(List, pos1-1, pos2-1)

    # Criando pasta caso ela não exista
    caminhoPasta = f'{path}/{n_execucao}_pouco_desordenado'
    if (not os.path.exists(caminhoPasta)):
        os.mkdir(caminhoPasta)

    arquivo_tamanho_50000 = open(
        f'{caminhoPasta}/tamanho50000_{n_execucao}.txt', "w")

    arquivo_tamanho_50000.write("## Algortimos de Ordenacao - Lista de tamanho 50000 - Caso pouco desordenado (10%) ## \n\n")

    # MERGE SORT
    arquivo_tamanho_50000.write("MERGE SORT \n")
    ini = time.time()
    resultado_merge_50000 = mergeSort(resultado_vetor_50000)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_50000.write("Tempo Medio: "+str(tempoMedio)+"s \n\n")
    # print(resultado_vetor_50000)

    # QUICK SORT PIVO ALEATORIO
    arquivo_tamanho_50000.write("Quick Sort Aleatorio: \n")
    ini = time.time()
    resultado_quick_50000 = quicksortPivoAleatorio(resultado_vetor_50000, 0, len(resultado_vetor_50000) - 1)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_50000.write("Tempo Medio: "+str(tempoMedio)+"s \n\n")
    # print(resultado_vetor_50000)

    #QUICK SORT PIVO MEDIO
    arquivo_tamanho_50000.write("Quick Sort Pivo Medio: \n")
    ini = time.time()
    quickSortPivoMedio(resultado_vetor_50000, True)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_50000.write("Tempo Medio: "+str(tempoMedio)+"s \n\n")
    # print(resultado_vetor_50000)

    #QUICK SORT ACHA PIVO
    arquivo_tamanho_50000.write("Quick Sort Acha Pivo: \n")
    ini = time.time()
    quickSortAchaPivo(resultado_vetor_50000, 0, len(resultado_vetor_50000) - 1)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_50000.write("Tempo Medio: "+str(tempoMedio)+"s \n\n")
    # print(resultado_vetor_50000)

    #HEAP SORT
    arquivo_tamanho_50000.write("Heap Sort \n")
    ini = time.time()
    heapSort(resultado_vetor_50000)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_50000.write("Tempo Medio: "+str(tempoMedio)+"s")
    # print(resultado_vetor_50000)

    arquivo_tamanho_50000.close()

    ################################################################################
    ################################# TAMANHO 100000 ##################################
    ################################################################################

    pos1, pos2  = 1,50
    

    lista = range(1,100001)
    lista

    arr=[]

    n = len(lista)
    for i in range(n):
        arr.append(lista[i])

    List = arr
    for x in range(10000):
        pos1 = randint(1, 100000)
        pos2 = randint(1, 100000)
        while (pos1 == pos2):
            pos2 = randint(1, 100000)
        resultado_tamanho_100000 = swapPositions(List, pos1-1, pos2-1)

    # Criando pasta caso ela não exista
    caminhoPasta = f'{path}/{n_execucao}_pouco_desordenado'
    if (not os.path.exists(caminhoPasta)):
        os.mkdir(caminhoPasta)

    arquivo_tamanho_100000 = open(
        f'{caminhoPasta}/tamanho100000_{n_execucao}.txt', "w")

    arquivo_tamanho_100000.write("## Algortimos de Ordenacao - Lista de tamanho 100000 - Caso pouco desordenado (10%) ## \n\n")

    # MERGE SORT
    arquivo_tamanho_100000.write("MERGE SORT \n")
    ini = time.time()
    resultado_merge_100000 = mergeSort(resultado_tamanho_100000)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_100000.write("Tempo Medio: "+str(tempoMedio)+"s \n\n")
    # print(arquivo_tamanho_100000)

    # QUICK SORT PIVO ALEATORIO
    arquivo_tamanho_100000.write("Quick Sort Aleatorio: \n")
    ini = time.time()
    resultado_quick_100000 = quicksortPivoAleatorio(resultado_tamanho_100000, 0, len(resultado_tamanho_100000) - 1)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_100000.write("Tempo Medio: "+str(tempoMedio)+"s \n\n")
    # print(arquivo_tamanho_100000)

    #QUICK SORT PIVO MEDIO
    arquivo_tamanho_100000.write("Quick Sort Pivo Medio: \n")
    ini = time.time()
    quickSortPivoMedio(resultado_tamanho_100000, True)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_100000.write("Tempo Medio: "+str(tempoMedio)+"s \n\n")
    # print(arquivo_tamanho_100000)

    #QUICK SORT ACHA PIVO
    arquivo_tamanho_100000.write("Quick Sort Acha Pivo: \n")
    ini = time.time()
    quickSortAchaPivo(resultado_tamanho_100000, 0, len(resultado_tamanho_100000) - 1)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_100000.write("Tempo Medio: "+str(tempoMedio)+"s \n\n")
    # print(arquivo_tamanho_100000)

    #HEAP SORT
    arquivo_tamanho_100000.write("Heap Sort \n")
    ini = time.time()
    heapSort(resultado_tamanho_100000)
    fim = time.time()
    tempoMedio = fim - ini
    arquivo_tamanho_100000.write("Tempo Medio: "+str(tempoMedio)+"s")
    # print(arquivo_tamanho_100000)

    arquivo_tamanho_100000.close()