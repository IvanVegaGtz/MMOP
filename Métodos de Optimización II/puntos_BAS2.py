import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
import math

#Leer el archivo con los datos
datos = pd.read_csv("/Users/ivanvegagutierrez/Desktop/CIMAT/SEGUNDO/METOPT2/puntos.csv")
#Crear matriz de distancias de los datos
Dist = np.zeros((240, 240))
for i in range(240):
    for j in range(i+1, 240):
        Dist[i][j] = ((datos['x'][i]-datos['x'][j])**2 + (datos['y'][i]-datos['y'][j])**2)**0.5
        Dist[j][i] = Dist[i][j]
# Definimos la funcion objetivo
# x es un vector solucion
def fobj(x,dij):
    D = x*dij
    z = D.sum()
    return z
#Distancia minima de un punto a un conjunto de centros
#Regresa el centro mas cercano al punto 
def distmin(punto, centros, D):
    indice_centro = 0
    min = D[punto][centros[0]]
    for i in range(1, len(centros)):
        if min > D[punto][centros[i]]:
            min = D[punto][centros[i]]
            indice_centro = i
    return indice_centro
# Distancia minima entre centros
def distmin_centros(centros, D):
    tam = len(centros)
    M = np.zeros((tam,tam))
    for i in range(tam):
        M[i][i] = 1000000
        for j in range(i+1, tam):
            M[i][j] = D[centros[i]][centros[j]]
            M[j][i] = M[i][j]
    z = np.min(M)
    return z
# Funcion que calcula las distancias entre los puntos y el centro

#Construir solucion aleatoria
def solRandom():
    # Asignamos centros de manera aleatoria
    options = np.arange(0, 240)
    centros = np.random.choice(options, 10, replace = False)
    # Distancia minima entre los centros
    z = distmin_centros(centros, Dist)
    # inicializamos nuestra solucion
    x = np.zeros((240, 240))
    # creamos el conjunto de puntos (los que no son centros)
    puntos = []
    for i in range(240):
        if i not in centros:
            puntos.append(i)
    puntos = np.array(puntos)
    # Creamos una diccionario que va a contener los puntos agrupados
    y = {}
    for i in range(10):
        y['centro'+ str(i)] = [centros[i]]
    # Cada centro es asignado a si mismo 
    for i in centros:
        x[i][i] = 1
    # Asignamos los puntos a los centros
    puntos = set(puntos)
    asignados = []
    centros = list(centros)
    for j in puntos:
        centro_cercano = distmin(j, centros, Dist)
        fila = centros[centro_cercano]
        cont = centros.index(centro_cercano)
        x[fila, j] = 1
        asignados.append(j)
        y['centro' + str(cont)].append(j)
    puntos = puntos -set(asignados)
    return x, y, z, centros
# Construir solucion aleatorio a partir de una solucion
def solRandom2(centros_0):
    # Asignamos centros de manera aleatoria
    centros = centros_0
    indice = random.randint(0,len(centros_0)-1)
    band = True
    while band:
        centro_nuevo = random.randint(0,239)
        if centro_nuevo not in centros_0:
            band = False
    centros[indice] = centro_nuevo
    # Distancia minima entre los centros
    z = distmin_centros(centros, Dist)
    # inicializamos nuestra solucion
    x = np.zeros((240, 240))
    # creamos el conjunto de puntos (los que no son centros)
    puntos = []
    for i in range(240):
        if i not in centros:
            puntos.append(i)
    puntos = np.array(puntos)
    # Creamos una diccionario que va a contener los puntos agrupados
    y = {}
    for i in range(10):
        y['centro'+ str(i)] = [centros[i]]
    # Cada centro es asignado a si mismo 
    for i in centros:
        x[i][i] = 1
    # Asignamos los puntos a los centros
    puntos = set(puntos)
    asignados = []
    centros = list(centros)
    for j in puntos:
        centro_cercano = distmin(j, centros, Dist)
        fila = centros[centro_cercano]
        cont = centros.index(centro_cercano)
        x[fila, j] = 1
        asignados.append(j)
        y['centro' + str(cont)].append(j)
    puntos = puntos -set(asignados)
    return x, y, z, centros

# Busqueda aleatoria simple
def BAS(dij, N, Temp):
    iter = 0
    band = True
    while band:
        sol0 = solRandom()
        x = sol0[0]
        y = sol0[1]
        z = sol0[2]
        centros = sol0[3]
        if distmin_centros(centros, Dist) > 50:
            band = False
    while iter < N:
        iter += 1
        soliter = solRandom2(centros)
        xhat = soliter[0]
        yhat = soliter[1]
        zhat = soliter[2]
        centroshat = soliter[3]
        if fobj(xhat, dij) < fobj(x, dij):
            x = xhat
            y = yhat
            z = zhat
            centros = centroshat
            print("iter: {} funcion objetivo  = {} centros = {}  ".format(iter,fobj(x,dij), centros))
        else:
            r = np.random.uniform(0,1,1)
            if r < math.exp((fobj(x, dij) - fobj(xhat, dij))/Temp):
                x = xhat
                y = yhat
                z = zhat
                centros = centroshat
                print("iter: {} funcion objetivo  = {} centros = {}  ".format(iter,fobj(x,dij), centros))
        Temp = 0.99*Temp

    return x, fobj(x, dij), y
#Resultados
res = BAS(Dist, 1000, 200)
fun = res[1]
dic = res[2]
# Graficar
# Vector de colores
colores = ['r', 'b', 'g', 'k', 'grey', 'c', 'm', 'y', 'brown', 'pink' ]

def graficar():
    color = 0
    etiquetas = []
    for clave in dic:
        etiquetas.append(clave)
    #Graficamos
    for clave in dic:
        for j in range(len(dic[clave])):
            punto = dic[clave][j]
            #plt.pause(.0001)
            plt.scatter(datos['x'][punto], datos['y'][punto], c = colores[color])
            if j==0:
                plt.annotate(etiquetas[color], (datos['x'][punto],  datos['y'][punto]))
        color += 1
graficar()
print("El optimo es", fun)
plt.show()
