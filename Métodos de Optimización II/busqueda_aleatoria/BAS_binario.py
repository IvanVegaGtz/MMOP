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
    # Creamos un diccionario que va a contener los puntos agrupados
    y = {}
    for i in range(10):
        y['centro'+ str(i)] = [centros[i]]
    # Cada centro es asignado a si mismo 
    for i in centros:
        x[i][i] = 1
    # Asignamos los puntos a los centros
    for p in puntos:
        # A cada punto le asignamos un centro
        asig = random.randint(0,9)
        fila = centros[asig]
        x[fila][p] = 1
        # Agregamos el punto al centro en el vector de agrupamiento
        y['centro' + str(asig)].append(p)
    return x, y
# Graficar
# Vector de colores
def graficar(sol, dic,dij):
    colores = ['r', 'b', 'g', 'k', 'grey', 'c', 'm', 'y', 'brown', 'pink' ]
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
    plt.title("La funcion objetivo es {}".format(fobj(sol,dij)))
# Busqueda aleatoria simple
def BAS(dij, N):
    k = 0
    sol_0 = solRandom()
    x = sol_0[0]
    y = sol_0[1]
    plot1 = plt.figure(1)
    graficar(x, y, dij)
    while k < N:
        k += 1
        sol_k = solRandom()
        xhat = sol_k[0]
        yhat = sol_k[1] 
        if fobj(xhat, dij) < fobj(x, dij):
            x = xhat
            y = yhat
            print("iter: {} funcion objetivo = {}".format(k, fobj(x,dij)))
    return x, y

#Resultados
res = BAS(Dist, 1000)
x = res[0]
dic = res[1]
plot2 = plt.figure(2)
graficar(x, dic, Dist)
plt.show()
print(fobj(x,Dist))