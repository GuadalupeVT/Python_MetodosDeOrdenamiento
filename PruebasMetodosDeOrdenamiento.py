'''
Created on 16/11/2018

@author: GVT
'''
from time import time
import random
import copy

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
    print (numeros)


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
    print (numeros)
    

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
    print (numeros)
    
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
    print (numeros)
    
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
    print (numeros)

def ordenamientoShellsort (numeros):
    n=len(numeros)
    gap=n//2
    comparaciones=0
    intercambios=0
    recorridos=0
    start_time = time()
    while gap > 0:
        for i in range(gap,n):
            temp = numeros[i]
            j = i 
            comparaciones=comparaciones+1
            while  j >= gap and numeros[j-gap] >temp:
                numeros[j] = numeros[j-gap] 
                j -= gap
                intercambios=intercambios+1
            numeros[j] = temp 
            recorridos=recorridos+1
        gap //= 2
    elapsed_time = time() - start_time
    print("Tiempo de ejecucion: %.10f seconds." % elapsed_time)
    print ("Recoridos: "+str (recorridos))
    print ("Intercambios: "+str (intercambios))
    print ("Comparaciones: "+str (comparaciones))
    print(numeros)
   
def particion(numeros,primero,ultimo):
    i = ( primero-1 ) 
    pivote = numeros[ultimo]
    for j in range(primero , ultimo):
        if   numeros[j] <= pivote:
            i = i+1 
            numeros[i],numeros[j] = numeros[j],numeros[i]
    numeros[i+1],numeros[ultimo] = numeros[ultimo],numeros[i+1] 
    return ( i+1 )  
    
def ordenamientoQuicksort(numeros,primero,ultimo):
    if primero < ultimo: 
        pi = particion(numeros,primero,ultimo)
        ordenamientoQuicksort(numeros, primero, pi-1) 
        ordenamientoQuicksort(numeros, pi+1, ultimo)
  
  
def countingSort(arr, exp1,comparaciones): 
    n = len(arr) 
    output = [0] * (n)
    count = [0] * (10) 
    for i in range(0, n): 
        index = (arr[i]/exp1) 
        c=(index)%10
        count[ int(c) ] += 1
    for i in range(1,10): 
        count[i] += count[i-1]
    i = n-1
    comparaciones=comparaciones+1
    while i>=0: 
        index = (arr[i]/exp1) 
        output[ count[ int((index)%10) ] - 1] = arr[i] 
        count[ int((index)%10) ] -= 1
        i -= 1
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 
    return comparaciones   
        
def ordenamientoRadixSort(numeros):
    comparaciones=0
    intercambios=0
    recorridos=0
    start_time = time()
    max1 = max(numeros) 
    exp = 1
    while max1/exp > 0: 
        intercambios=intercambios+1
        comparaciones=comparaciones+countingSort(numeros,exp,comparaciones)    
        exp *= 10
        recorridos=recorridos+1
    elapsed_time = time() - start_time
    print("Tiempo de ejecucion: %.10f seconds." % elapsed_time)
    print ("Recoridos: "+str (recorridos))
    print ("Intercambios: "+str (intercambios))
    print ("Comparaciones: "+str (comparaciones))
        
def ordenamientoIntercalacion():
    archivo3=open ("ArchivoSalida.txt", "w")
    archivo1=open("Archivo1.txt", "r")
    archivo2=open("Archivo2.txt", "r")
    repetir=True
    lineaArchivo1=archivo1.readline() 
    lineaArchivo2=archivo2.readline()
    while(repetir):
        if(int(lineaArchivo1)<int(lineaArchivo2)):
            archivo3.write(lineaArchivo1)
            lineaArchivo1=archivo1.readline()
            if(lineaArchivo1==""):
                archivo3.write("\n")
                archivo3.write(lineaArchivo2)
                lineaArchivo2=archivo2.readline()
                while(lineaArchivo2!=""):
                    archivo3.write(lineaArchivo2)
                    lineaArchivo2=archivo2.readline()
                repetir=False
        elif(int(lineaArchivo1)>int(lineaArchivo2)):
            archivo3.write(lineaArchivo2)
            lineaArchivo2=archivo2.readline()
            if(lineaArchivo2==""):
                archivo3.write("\n")
                archivo3.write(lineaArchivo1)
                lineaArchivo1=archivo1.readline()
                while(lineaArchivo1!=""):
                    archivo3.write(lineaArchivo1)
                    lineaArchivo1=archivo1.readline()
                repetir=False
        else:
            archivo3.write(lineaArchivo1)
            archivo3.write(lineaArchivo2)
            lineaArchivo1=archivo1.readline()
            if(lineaArchivo1==""):
                archivo3.write("\n")
                archivo3.write(lineaArchivo2)
                lineaArchivo2=archivo2.readline()
                while(lineaArchivo2!=""):
                    archivo3.write(lineaArchivo2)
                    lineaArchivo2=archivo2.readline()
                repetir=False
            lineaArchivo2=archivo2.readline()
            if(lineaArchivo2==""):
                archivo3.write("\n")
                archivo3.write(lineaArchivo1)
                lineaArchivo1=archivo1.readline()
                while(lineaArchivo1!=''):
                    archivo3.write(lineaArchivo1)
                    lineaArchivo1=archivo1.readline()
                repetir=False
    archivo2.close
    archivo1.close
    print("Archivos combinados y ordenados correctamente")
    archivo3.close

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
while(menu!=11):
    print ("-------------------MENU----------------------")
    print("-----Ordenamiento interno------")
    print ("1. Ordenamiento Burbuja")
    print ("2. Ordenamiento Seleccion")
    print ("3. Ordenamiento Insercion")
    print ("4. Ordenamiento Shellsort") 
    print ("5. Ordenamiento Quicksort")
    print ("6. Ordenamiento Radix")
    print("-----------Ordenamiento externo--------")
    print ("7. Intercalacion")
    print("8. Mezcla directa")
    print ("9.Mezcla natural")
    print("10. Tabla de eficiencia")
    menu=int(input("11. Salir"))
    if menu==1:
        copiaVector1 = copy.copy(arregloDesordenado1)
        copiaVector2 = copy.copy(arregloDesordenado2)
        copiaVector3 = copy.copy(arregloDesordenado3)
        copiaVector4 = copy.copy(arregloDesordenado4)
        print ("\n==================ORDENAMIENTO CON BURBUJA====================")
        print ("1. Burbuja0")
        print ("2. Burbuja1")
        submenu=int(input("3. Burbuja2"))  
        if submenu==1:
            print ("*********Burbuja0*********")
            print ("*************Arreglo con 1,000 datos************")
            print ("Vector original: ")
            print (copiaVector1)
            ordenamientoBurbuja0(copiaVector1)
            print ("*************Arreglo con 10,000 datos************")
            print ("Vector original: ")
            print (copiaVector2)
            ordenamientoBurbuja0(copiaVector2)
            print ("*************Arreglo con 100,000 datos************")
            print ("Vector original: ")
            print (copiaVector3)
            ordenamientoBurbuja0(copiaVector3)
            print ("*************Arreglo con 1,000,000 datos************")
            print ("Vector original: ")
            print (copiaVector4)
            ordenamientoBurbuja0(copiaVector4)
        elif submenu==2:
            print ("*********Burbuja1*********")
            print ("*************Arreglo con 1,000 datos************")
            print ("Vector original: ")
            print (copiaVector1)
            ordenamientoBurbuja1(copiaVector1)
            print ("*************Arreglo con 10,000 datos************")
            print ("Vector original: ")
            print (copiaVector2)
            ordenamientoBurbuja1(copiaVector2)
            print ("*************Arreglo con 100,000 datos************")
            print ("Vector original: ")
            print (copiaVector3)
            ordenamientoBurbuja1(copiaVector3)
            print ("*************Arreglo con 1,000,000 datos************")
            print ("Vector original: ")
            print (copiaVector4)
            ordenamientoBurbuja1(copiaVector4)
        elif submenu==3:
            print ("*********Burbuja2*********")
            print ("*************Arreglo con 1,000 datos************")
            print ("Vector original: ")
            print (copiaVector1)
            ordenamientoBurbuja2(copiaVector1)
            print ("*************Arreglo con 10,000 datos************")
            print ("Vector original: ")
            print (copiaVector2)
            ordenamientoBurbuja2(copiaVector2)
            print ("*************Arreglo con 100,000 datos************")
            print ("Vector original: ")
            print (copiaVector3)
            ordenamientoBurbuja2(copiaVector3)
            print ("*************Arreglo con 1,000,000 datos************")
            print ("Vector original: ")
            print (copiaVector4)
            ordenamientoBurbuja2(copiaVector4)
        else:
            print ("Opcion incorrecta!!")
    elif menu==2:
        copiaVector5 = copy.copy(arregloDesordenado1)
        copiaVector6 = copy.copy(arregloDesordenado2)
        copiaVector7 = copy.copy(arregloDesordenado3)
        copiaVector8 = copy.copy(arregloDesordenado4)
        print ("\n==================ORDENAMIENTO CON SELECCION====================")
        print ("*************Arreglo con 1,000 datos************")
        print ("Vector original: ")
        print (copiaVector5)
        ordenamientoPorSeleccion(copiaVector5)
        print ("*************Arreglo con 10,000 datos************")
        print ("Vector original: ")
        print (copiaVector6)
        ordenamientoPorSeleccion(copiaVector6)
        print ("*************Arreglo con 100,000 datos************")
        print ("Vector original: ")
        print (copiaVector7)
        ordenamientoPorSeleccion(copiaVector7)
        print ("*************Arreglo con 1,000,000 datos************")
        print ("Vector original: ")
        print (copiaVector8)
        ordenamientoPorSeleccion(copiaVector8)   
    elif menu==3:
        copiaVector9 = copy.copy(arregloDesordenado1)
        copiaVector10 = copy.copy(arregloDesordenado2)
        copiaVector11= copy.copy(arregloDesordenado3)
        copiaVector12= copy.copy(arregloDesordenado4)
        print ("\n==================ORDENAMIENTO POR INSERCION====================")
        print ("*************Arreglo con 1,000 datos************")
        print ("Vector original: ")
        print (copiaVector9)
        ordenamientoPorInsercion(copiaVector9)
        print ("*************Arreglo con 10,000 datos************")
        print ("Vector original: ")
        print (copiaVector10)
        ordenamientoPorInsercion(copiaVector10)
        print ("*************Arreglo con 100,000 datos************")
        print ("Vector original: ")
        print (copiaVector11)
        ordenamientoPorInsercion(copiaVector11)
        print ("*************Arreglo con 1,000,000 datos************")
        print ("Vector original: ")
        print (copiaVector12)
        ordenamientoPorInsercion(copiaVector12)
        
    elif menu==4:
        copiaVector13 = copy.copy(arregloDesordenado1)
        copiaVector14 = copy.copy(arregloDesordenado2)
        copiaVector15= copy.copy(arregloDesordenado3)
        copiaVector16= copy.copy(arregloDesordenado4)
        print ("\n==================ORDENAMIENTO SHELLSORT====================")
        print ("*************Arreglo con 1,000 datos************")
        print ("Vector original: ")
        print (copiaVector13)
        ordenamientoShellsort(copiaVector13)
        print ("*************Arreglo con 10,000 datos************")
        print ("Vector original: ")
        print (copiaVector14)
        ordenamientoShellsort(copiaVector14)
        print ("*************Arreglo con 100,000 datos************")
        print ("Vector original: ")
        print (copiaVector15)
        ordenamientoShellsort(copiaVector15)
        print ("*************Arreglo con 1,000,000 datos************")
        print ("Vector original: ")
        print (copiaVector16)
        ordenamientoShellsort(copiaVector16)
        
    elif menu==5:
        copiaVector17 = copy.copy(arregloDesordenado1)
        copiaVector18 = copy.copy(arregloDesordenado2)
        copiaVector19= copy.copy(arregloDesordenado3)
        copiaVector20= copy.copy(arregloDesordenado4)
        print ("\n==================ORDENAMIENTO QUICKSORT====================")
        print ("*************Arreglo con 1,000 datos************")
        print ("Vector original: ")
        print (copiaVector17)
        start_time = time()
        ordenamientoQuicksort(copiaVector17)
        elapsed_time = time() - start_time
        print("Tiempo de ejecucion: %.10f seconds." % elapsed_time)
        print (copiaVector17)
        print ("*************Arreglo con 10,000 datos************")
        print ("Vector original: ")
        print (copiaVector18)
        start_time = time()
        ordenamientoQuicksort(copiaVector18)
        elapsed_time = time() - start_time
        print("Tiempo de ejecucion: %.10f seconds." % elapsed_time)
        print (copiaVector18)
        print ("*************Arreglo con 100,000 datos************")
        print ("Vector original: ")
        print (copiaVector19)
        start_time = time()
        ordenamientoQuicksort(copiaVector19)
        elapsed_time = time() - start_time
        print("Tiempo de ejecucion: %.10f seconds." % elapsed_time)
        print (copiaVector19)
        print ("*************Arreglo con 1,000,000 datos************")
        print ("Vector original: ")
        print (copiaVector20)
        start_time = time()
        ordenamientoQuicksort(copiaVector20)
        elapsed_time = time() - start_time
        print("Tiempo de ejecucion: %.10f seconds." % elapsed_time)
        print (copiaVector20)
    
    elif menu ==6:
        copiaVector21 = copy.copy(arregloDesordenado1)
        copiaVector22 = copy.copy(arregloDesordenado2)
        copiaVector23= copy.copy(arregloDesordenado3)
        copiaVector24= copy.copy(arregloDesordenado4)
        print ("\n==================ORDENAMIENTO RADIXSORT====================")
        print ("*************Arreglo con 1,000 datos************")
        print ("Vector original: ")
        print (copiaVector21)
        ordenamientoRadixSort(copiaVector21)
        print (copiaVector21)
        print ("*************Arreglo con 10,000 datos************")
        print ("Vector original: ")
        print (copiaVector22)
        ordenamientoRadixSort(copiaVector22)
        print (copiaVector22)
        print ("*************Arreglo con 100,000 datos************")
        print ("Vector original: ")
        print (copiaVector23)
        ordenamientoRadixSort(copiaVector23)
        print (copiaVector23)
        print ("*************Arreglo con 1,000,000 datos************")
        print ("Vector original: ")
        print (copiaVector24)
        ordenamientoRadixSort(copiaVector24)
        print (copiaVector24)
    elif menu==7:
        ordenamientoIntercalacion()
    elif menu==11:
        print ("Saliendo...")
    else: print("Opcion incorrecta!!")
    
