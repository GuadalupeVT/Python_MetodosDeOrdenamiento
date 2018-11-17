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
    for i in range(2,len(numeros)+1):
        for j in range(0,len(numeros)-i+1):
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
    while (i<len(numeros)+1 and ordenado==False):
        i=i+1
        ordenado=True
        for j in range(0,len(numeros)-i+1) :
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
    
#Si se implementa Burbuja3 en Python queda como Burbuja2

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
    
menu=0
submenu=0
while(menu!=4):
    print "-------------------MENU----------------------"
    print "1. Ordenamiento Burbuja"
    print "2. Ordenamiento Seleccion"
    print "3. Ordenamiento Insercion"
    menu=int(raw_input("4. Salir"))
    if menu==1:
        copiaVector1 = arregloDesordenado1.copy()
        copiaVector2 = arregloDesordenado2.copy()
        copiaVector3 = arregloDesordenado3.copy()
        copiaVector4 = arregloDesordenado4.copy()
        print "\n==================ORDENAMIENTO CON BURBUJA===================="
        print "1. Burbuja0"
        print "2. Burbuja1"
        menu=int(raw_input("3. Burbuja2"))  
        if submenu==1:
            print "*********Burbuja0*********"
            print "*************Arreglo con 1,000 datos************"
            print "Vector original: "
            print (copiaVector1)
            ordenamientoBurbuja0(copiaVector1)
            print "*************Arreglo con 10,000 datos************"
            print "Vector original: "
            print (copiaVector2)
            ordenamientoBurbuja0(copiaVector2)
            print "*************Arreglo con 100,000 datos************"
            print "Vector original: "
            print (copiaVector3)
            ordenamientoBurbuja0(copiaVector3)
            print "*************Arreglo con 1,000,000 datos************"
            print "Vector original: "
            print (copiaVector4)
            ordenamientoBurbuja0(copiaVector4)
        elif submenu==2:
            print "*********Burbuja1*********"
            print "*************Arreglo con 1,000 datos************"
            print "Vector original: "
            print (copiaVector1)
            ordenamientoBurbuja1(copiaVector1)
            print "*************Arreglo con 10,000 datos************"
            print "Vector original: "
            print (copiaVector2)
            ordenamientoBurbuja1(copiaVector2)
            print "*************Arreglo con 100,000 datos************"
            print "Vector original: "
            print (copiaVector3)
            ordenamientoBurbuja1(copiaVector3)
            print "*************Arreglo con 1,000,000 datos************"
            print "Vector original: "
            print (copiaVector4)
            ordenamientoBurbuja1(copiaVector4)
        elif submenu==3:
            print "*********Burbuja2*********"
            print "*************Arreglo con 1,000 datos************"
            print "Vector original: "
            print (copiaVector1)
            ordenamientoBurbuja2(copiaVector1)
            print "*************Arreglo con 10,000 datos************"
            print "Vector original: "
            print (copiaVector2)
            ordenamientoBurbuja2(copiaVector2)
            print "*************Arreglo con 100,000 datos************"
            print "Vector original: "
            print (copiaVector3)
            ordenamientoBurbuja2(copiaVector3)
            print "*************Arreglo con 1,000,000 datos************"
            print "Vector original: "
            print (copiaVector4)
            ordenamientoBurbuja2(copiaVector4)
        else:
            print "Opcion incorrecta!!"
    elif menu==2:
        copiaVector5 = arregloDesordenado1.copy()
        copiaVector6 = arregloDesordenado2.copy()
        copiaVector7 = arregloDesordenado3.copy()
        copiaVector8 = arregloDesordenado4.copy()
        print "\n==================ORDENAMIENTO CON SELECCION===================="
        print "*************Arreglo con 1,000 datos************"
        print "Vector original: "
        print (copiaVector5)
        ordenamientoPorSeleccion(copiaVector5)
        print "*************Arreglo con 10,000 datos************"
        print "Vector original: "
        print (copiaVector6)
        ordenamientoPorSeleccion(copiaVector6)
        print "*************Arreglo con 100,000 datos************"
        print "Vector original: "
        print (copiaVector7)
        ordenamientoPorSeleccion(copiaVector7)
        print "*************Arreglo con 1,000,000 datos************"
        print "Vector original: "
        print (copiaVector8)
        ordenamientoPorSeleccion(copiaVector8)   
    elif menu==3:
        copiaVector9 = arregloDesordenado1.copy()
        copiaVector10 = arregloDesordenado2.copy()
        copiaVector11= arregloDesordenado3.copy()
        copiaVector12= arregloDesordenado4.copy()
        print "\n==================ORDENAMIENTO POR INSERCION===================="
        print "*************Arreglo con 1,000 datos************"
        print "Vector original: "
        print (copiaVector9)
        ordenamientoPorInsercion(copiaVector9)
        print "*************Arreglo con 10,000 datos************"
        print "Vector original: "
        print (copiaVector10)
        ordenamientoPorInsercion(copiaVector10)
        print "*************Arreglo con 100,000 datos************"
        print "Vector original: "
        print (copiaVector11)
        ordenamientoPorInsercion(copiaVector11)
        print "*************Arreglo con 1,000,000 datos************"
        print "Vector original: "
        print (copiaVector12)
        ordenamientoPorInsercion(copiaVector12)
    else: print"Opcion incorrecta!!"
    
