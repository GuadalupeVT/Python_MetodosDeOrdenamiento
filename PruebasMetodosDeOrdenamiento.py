'''
Created on 16/11/2018

@author: GVT
'''
from time import time
import random


def ordenamientoBurbuja0(numeros):
    comparaciones=0
    intercambios=0
    recorridos=0
    start_time = time()
    for i in range (0,len(numeros)-1):
        for j in range(0,len(numeros)-1):
            comparaciones=comparaciones+1
            if numeros[j] > numeros [j+1]:
                aux = numeros[j+1]
                numeros[j+1]=numeros[j]
                numeros[j]=aux
                intercambios=intercambios+1
            recorridos=recorridos+1
    elapsed_time = time() - start_time
    print("Tiempo de ejecucion: %.10f seconds." % elapsed_time)
    print ("Recoridos: "+str (recorridos))
    print ("Intercambios: "+str (intercambios))
    print ("Comparaciones: "+str (comparaciones))
    print numeros


def ordenamientoBurbuja1(numeros):
    comparaciones=0
    intercambios=0
    recorridos=0
    start_time = time()
    for i in range(2,len(numeros)):
        for j in range(0,len(numeros)-i):
            comparaciones=comparaciones+1
            if numeros[j]>numeros[j+1]:
                aux=numeros[j]
                numeros[j]=numeros[j+1]
                numeros[j+1]=aux
                intercambios=intercambios+1
            recorridos=recorridos+1
    elapsed_time = time() - start_time
    print("Tiempo de ejecucion: %.10f seconds." % elapsed_time)
    print ("Recoridos: "+str (recorridos))
    print ("Intercambios: "+str (intercambios))
    print ("Comparaciones: "+str (comparaciones))
    print numeros
    

 
def ordenamientoBurbuja2(numeros):
    comparaciones=0
    intercambios=0
    recorridos=0
    i=1
    ordenado=False
    start_time = time()
    while (i<len(numeros) and ordenado==False):
        i=i+1
        ordenado=True
        for j in range(0,len(numeros)-i) :
            comparaciones=comparaciones+1
            if numeros[j]>numeros[j+1]:
                ordenado=False
                aux=numeros[j]
                numeros[j]=numeros[j+1]
                numeros[j+1]=aux
                intercambios=intercambios+1
            recorridos=recorridos+1
    elapsed_time = time() - start_time
    print("Tiempo de ejecucion: %.10f seconds." % elapsed_time)
    print ("Recoridos: "+str (recorridos))
    print ("Intercambios: "+str (intercambios))
    print ("Comparaciones: "+str (comparaciones))
    print numeros
    
    
def ordenamientoPorSeleccion(numeros):
    comparaciones=0
    intercambios=0
    recorridos=0
    start_time = time()
    for i in range(0,len(numeros)):    
        minimo = i
        for j in range(i+1,len(numeros)) :
            comparaciones=comparaciones+1
            if numeros[j] < numeros[minimo] :
                minimo = j
        if min is not i :
            aux = numeros[i]
            numeros[i] = numeros[minimo]
            numeros[minimo] = aux
            intercambios=intercambios+1
        recorridos=recorridos+1
    elapsed_time = time() - start_time
    print("Tiempo de ejecucion: %.10f seconds." % elapsed_time)
    print ("Recoridos: "+str (recorridos))
    print ("Intercambios: "+str (intercambios))
    print ("Comparaciones: "+str (comparaciones))
    print numeros
    

def ordenamientoPorInsercion(numeros):
    comparaciones=0
    intercambios=0
    recorridos=0
    start_time = time()
    for i in range(1,len(numeros)):
        aux=numeros[i]
        j=i-1
        comparaciones=comparaciones+1
        while j>=0:
            if(aux<numeros[j]):
                numeros[j+1]=numeros[j]
                numeros[j]=aux
                j=j-1
                intercambios=intercambios+1
            else:
                break
            recorridos=recorridos+1
    elapsed_time = time() - start_time
    print("Tiempo de ejecucion: %.10f seconds." % elapsed_time)
    print ("Recoridos: "+str (recorridos))
    print ("Intercambios: "+str (intercambios))
    print ("Comparaciones: "+str (comparaciones))
    print numeros
    
arregloDesordenado1 = [0]  * 1000
for i in range(1000):
    arregloDesordenado1[i] = random.randint(0, 100)
arregloDesordenado2 = [0]  * 10000
for i in range(10000):
    arregloDesordenado2[i] = random.randint(0, 100)
arregloDesordenado3 = [0]  * 100000
for i in range(100000):
    arregloDesordenado3[i] = random.randint(0, 100)
arregloDesordenado4 = [0]  * 1000000
for i in range(1000000):
    arregloDesordenado4[i] = random.randint(0, 100)
    
ordenamientoBurbuja2(arregloDesordenado1)
