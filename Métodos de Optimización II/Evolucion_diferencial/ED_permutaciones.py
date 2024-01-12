import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt

#Leer el archivo con los datos
#datos = pd.read_csv("/Users/ivanvegagutierrez/Desktop/CIMAT/SEGUNDO/METOPT2/tsp_51_1.csv")
datos = pd.read_csv("/Users/ivanvegagutierrez/Desktop/CIMAT/SEGUNDO/METOPT2/reto1.csv")
#Crear matriz de distancias
row = datos.shape[0]
Dist = np.zeros((row, row))
for i in range(row):
    for j in range(i+1, row):
        Dist[i][j] = ((datos['x'][i]-datos['x'][j])**2 + (datos['y'][i]-datos['y'][j])**2)**0.5
        Dist[j][i] = Dist[i][j]

# Funcion graficar
def graficar(r):
    '''
    x: vector que contiene la ruta
    '''
    n = len(r)
    plt.scatter(datos['x'], datos['y'])
    plt.scatter(datos['x'][int(r[0])], datos['y'][int(r[0])], c="red")
    plt.scatter(datos['x'][int(r[n-2])], datos['y'][int(r[n-2])], c="red")
    x = [datos['x'][int(r[i])] for i in range(n-1)]
    x.append(datos['x'][int(r[0])])
    y = [datos['y'][int(r[i])] for i in range(n-1)]
    y.append(datos['y'][int(r[0])])
    plt.plot(x,y)
    #x0 = [datos['x'][0], datos['x'][n-2]]
    #y0 = [datos['y'][0], datos['y'][n-2]]
    #plt.plot(x0,y0)
    plt.title("Distancia :  {}".format(r[n-1]))
    plt.show()
    return 


def fobj(x,dij):
    '''
    x : vector solucion
    dij: matriz de distancias
    '''
    sum = 0
    for i in range(len(x)-1):
        sum += dij[int(x[i])][int(x[i+1])]
    sum = sum + dij[int(x[0])][int(x[len(x)-1])]
    return sum


def decodifica(x):
    '''
    Decodifica al individuo x en x_deco (permutacion)
    '''
    dim = len(x)
    x_deco = np.zeros(dim)
    # matriz  auxiliar que relaciona a x con la permutacion
    x_aux = np.zeros((dim, 2))
    # sera la permutacion de x
    perm = np.arange(dim)
    # Concatenamos x con aux para poder decodificar a x 
    x_aux[:,0] = x
    x_aux[:,1] = perm
    x_aux = x_aux[x_aux[:,0].argsort()]
    x_deco[:dim] = x_aux[:,1]
    #Agregamos el valor de la funcion objetivo al vector decodificado
    x_sol = list(x_deco)
    x_sol.append(fobj(x_deco,Dist))
    return x_sol

def mejor(x):
    '''
    x: vector de llaves aleatorias
    x_best: mejor individuo de x codificado (aleatorios)
    indice :  indice origial del mejor individuo 
    '''
    N, n = x.shape
    x_pob = np.zeros((N,n+2))
    x_pob[:,range(n)] = x
    for i in range(N):
        x_obj = decodifica(x[i,:])
        x_pob[i][n] = x_obj[n]
        x_pob[i][n+1] = i
    x_pob = x_pob[x_pob[:,n].argsort()]
    x_best = x_pob[0, :n]
    indice = x_pob[0,n+1]
    return x_best, indice

# Funcion que realiza la busqueda utilizando evoluciOn diferencial
def Busq_ED(N, F, CR, k_max):
    '''
    N tamano de poblacion
    F numero entre 0 y 2
    CR valor definido entre (.1, 1)
    kmax numero maximo de iteraciones
    '''
    n = Dist.shape[0]
    #Inicializacion
    x =  np.random.uniform(0, 1, size=(N, n)) 
    lista =np.arange(N)
    k = 0
    while k < k_max:
        Q = np.zeros((N,n))
        xhat = np.zeros(n)
        y = np.zeros(n)
        for i in range(N):
            # Mutacion 1
            #'''
            opciones = np.delete(lista,i)
            indices = np.random.choice(opciones, 3, replace = False)
            xhat = x[indices[0]][:] + F*(x[indices[1]][:]-x[indices[2]][:])
            #'''
            # Mutacion 2
            '''
            # Ordenamos la poblacion para obtener al mejor
            x_best, indice = mejor(x)
            opciones = np.delete(lista,[i,int(indice)])
            indices = np.random.choice(opciones, 2, replace = False)
            xhat = x_best + F*(x[indices[0]][:]-x[indices[1]][:])
            '''
            # Mutacion 3
            '''
            # Ordenamos la poblacion para obtener al mejor
            x_best, indice = mejor(x)
            opciones = np.delete(lista,[i,int(indice)])
            indices = np.random.choice(opciones, 4, replace = False)
            xhat = x_best + F*(x[indices[0]][:] + x[indices[1]][:] - x[indices[2]][:] -x[indices[3]][:])
            '''
            # Mutacion 4
            '''
            # Ordenamos la poblacion para obtener al mejor
            F1 = F
            F2 = F1 + 0.1
            x_best, indice = mejor(x)
            opciones = np.delete(lista,[i,int(indice)])
            indices = np.random.choice(opciones, 3, replace = False)
            xhat = x[indices[0]][:]+ F1*(x_best - x[indices[0]][:]) + F2*(x[indices[1]][:] -x[indices[2]][:])
            '''
            # Mutacion 5
            '''
            F1 = F
            F2 = F1 + 0.1
            opciones = np.delete(lista,i)
            indices = np.random.choice(opciones, 5, replace = False)
            xhat = x[indices[0]][:]+ F1*(x[indices[1]][:] - x[indices[2]][:]) + F2*(x[indices[3]][:] -x[indices[4]][:])
            '''
            # Recombinacion
            I_i = np.random.choice(lista)
            for j in range(N):
                R_j = random.uniform(0,1)
                if  R_j <= CR or j == I_i:
                    y[j] = xhat[j]
                else:
                    y[j] = x[i][j]
            # Decodificacion
            Y = decodifica(y)
            X = decodifica(x[i,:])
            # Seleccion
            if Y[n] < X[n]:
                Q[i,:] = y
            else:
                Q[i,:] = x[i, :]
        x = Q
        k += 1
    # Poblacion final
    S = np.zeros((N,n+1))
    for i in range(N):
        S[i, :] = decodifica(x[i,:])
    # Mejor individuo
    S = S[S[:,n].argsort()]
    s  = S[0,:]
    print("La ruta mas corta es : \n", s)
    graficar(s)
    return S

#Parametros
N = 50
F = 0.7
CR = 0.7
k_max = 800
Busq_ED(N, F, CR, k_max)