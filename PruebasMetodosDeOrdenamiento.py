'''
Created on 16/11/2018

@author: GVT
'''
from time import time
import random

def ordenamientoPorSeleccion(numeros):
    start_time = time()
    for i in range(0,len(numeros)):    
        minimo = i
        for j in range(i+1,len(numeros)) :
            if numeros[j] < numeros[minimo] :
                minimo = j
        if min is not i :
            aux = numeros[i]
            numeros[i] = numeros[minimo]
            numeros[minimo] = aux
    elapsed_time = time() - start_time
    print("Tiempo de ejecucion: %.10f seconds." % elapsed_time)
    print numeros

def ordenamientoPorInsercion(numeros):
    for i in range(1,len(numeros)):
        aux=numeros[i]
        j=i-1
        while j>=0:
            if(aux<numeros[j]):
                numeros[j+1]=numeros[j]
                
                numeros[j]=aux
                j=j-1
            else:
                break
    
    

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

print "---------Ordenamiento por seleccion------------"          
     
edades=[54,26,93,17,77,31,44,55,20]
print(arregloDesordenado1)
ordenamientoPorSeleccion(arregloDesordenado1)