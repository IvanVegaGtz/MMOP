import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt

#Leer el archivo con los datos
datos = pd.read_csv("/Users/ivanvegagutierrez/Desktop/CIMAT/SEGUNDO/METOPT2/tsp_51_1.csv")
#Crear matriz de distancias
Dist = np.zeros((51, 51))
for i in range(51):
    for j in range(i+1, 51):
        Dist[i][j] = ((datos['x'][i]-datos['x'][j])**2 + (datos['y'][i]-datos['y'][j])**2)**0.5
        Dist[j][i] = Dist[i][j]

# Funcion graficar
def graficar(r):
    '''
    r: vector que contiene la ruta
    '''
    n = len(r)
    plot= plt.figure(1)
    plot.clear()
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
    plt.pause(.6)
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

def dos_opt(x):
    dim = len(x)
    x_nuevo = []
    opciones = np.arange(dim)
    k = True
    while k:
        indices = np.random.choice(opciones,2,replace = False)
        if indices[0] < indices[1]:
            min = indices[0]
            max = indices[1]
        else:
            min = indices[1]
            max = indices[0]
        if min + 1 != max and max+1 <= dim-1:
            k = False
    x = list(x)
    x.pop()
    x2 = []
    x1 = x[:min+1]
    x2.append(x[max])
    x2.append(x[max-1])
    x3 = x[min+1:max-1]
    x4 = x[max+1:]
    x_nuevo = x1 + x2 + x3 + x4
    return x_nuevo



# Funcion que realiza la busqueda utilizando evolucion diferencial
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
            # Mutacion 
            opciones = np.delete(lista,i)
            indices = np.random.choice(opciones, 3, replace = False)
            xhat = x[indices[0]][:] + F*(x[indices[1]][:]-x[indices[2]][:])
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
    return s

#Parametros
N = 50
F = 0.7
CR = 0.7
k_max = 800
sol = Busq_ED(N, F, CR, k_max)

n = len(sol)
for i in range(80000):
    x_nuevo = dos_opt(sol)
    x_nuevo.append(fobj(x_nuevo,Dist))
    if x_nuevo[n-1] < sol[n-1]:
        sol = x_nuevo
        print(sol)
        graficar(sol)