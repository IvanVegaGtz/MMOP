import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt

#Leer el archivo con los datos
datos = pd.read_csv("/Users/ivanvegagutierrez/Desktop/CIMAT/SEGUNDO/METOPT2/puntos.csv")
#Crear matriz de distancias
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

#Construir solucion aleatoria
def solRandom():
    # Asignamos centros de manera aleatoria
    options = np.arange(0, 240)
    centros = np.random.choice(options, 10, replace = False)
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
    for p in puntos:
        # A cada punto le asignamos un centro
        asig = distmin(p, centros, Dist)
        fila = centros[asig]
        x[fila][p] = 1
        # Agregamos el punto al centro en el vector de agrupamiento
        y['centro' + str(asig)].append(p)
    return x, y

# Busqueda aleatoria simple
def BAS(dij, N):
    iter = 0
    sol = solRandom()
    x = sol[0]
    y = sol[1]
    while iter < N:
        iter += 1
        sol_nueva = solRandom()
        xhat = sol_nueva[0]
        yhat = sol_nueva[1]
        if fobj(xhat, dij) < fobj(x, dij):
            x = xhat
            y = yhat
            print(fobj(x,dij))
    #plt.show()
    return x, fobj(x, dij), y

#Resultados
res = BAS(Dist, 1000)
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
            #plt.pause(.001)
            plt.scatter(datos['x'][punto], datos['y'][punto], c = colores[color])
            if j==0:
                plt.annotate(etiquetas[color], (datos['x'][punto],  datos['y'][punto]))
        color += 1
graficar()
plt.title('La solucion final es:  ' + str(fun))
plt.show()
print("El optimo es", fun)