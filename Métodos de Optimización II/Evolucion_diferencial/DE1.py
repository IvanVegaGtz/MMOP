import numpy as np
import random
import math
import matplotlib.pyplot as plt


def fobj(x):
    #z = 0.5*((x[0]**4 - 16*x[0]**2 +5*x[0])+(x[1]**4 - 16*x[1]**2 +5*x[1]))
    z = -20*np.exp(-0.2*np.sqrt(0.5*(x[0]**2 + x[1]**2))) - np.exp(0.5*(np.cos(2*np.pi*x[0]) + np.cos(2*np.pi*x[1]))) + 20 + np.exp(1)
    return z

# Definimos el espacio de busqueda
limX= [-5, 5] #Eje X
limY= [-5, 5] #Eje Y

# Funcion que inicializa la poblacion
def crea_padres(n):
    '''
    Funcion que genera n padres
    '''
    xpob = np.zeros((n,3))
    for i in range(n):
        for j in range(2):
            xpob[i][j] = random.uniform(limX[0], limX[1])
        xpob[i][2] = fobj((xpob[i][0],xpob[i][1]))
    return xpob

# Funcion para graficar 
def graficar(xpob, iter):
    plot = plt.figure(1)
    plot.clear()
    xx = np.linspace(limX[0], limX[1])
    yy = np.linspace(limY[0], limY[1])
    X, Y =  np.meshgrid(xx, yy)
    Z = fobj([X,Y])
    plt.contour(X, Y, Z, levels=16, cmap=plt.get_cmap('jet'))
    plt.title('iteracion {} fobj = {}'.format(iter,xpob[0,2]))
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.scatter(xpob[0,0],xpob[0,1], color="Green")
    for i in range(1,len(xpob)):
        plt.scatter(xpob[i,0],xpob[i,1], color="Blue")
    plt.xlim(limX[0], limX[1])
    plt.ylim(limX[0], limX[1])
    plt.pause(0.25)

# Funcion que realiza la busqueda utilizando evolución diferencial
def Busq_ED(N, F, CR, k_max):
    '''
    N tamano de poblacion
    F numero entre 0 y 2
    CR valor definido entre (.1, 1)
    kmax numero maximo de iteraciones
    '''
    x =  crea_padres(N)
    lista =np.arange(N)
    k = 0
    while k < k_max:
        graficar(x,k)
        Q = np.zeros((N,3))
        xhat = np.zeros((N,3))
        y = np.zeros((N,3))
        for i in range(N):
            # Mutacion 1
            '''
            opciones = np.delete(lista,i)
            indices = np.random.choice(opciones, 3, replace = False)
            for j in range(2):
                xhat[i][j] = x[indices[0]][j] + F*(x[indices[1]][j]-x[indices[2]][j])
            xhat[i][2] = fobj((xhat[i][0], xhat[i][1]))
            '''
            # Mutacion 2
            #'''
            # Ordenamos la poblacion para obtener al mejor
            x = x[x[:,2].argsort()]
            opciones = np.delete(lista,[i,0])
            indices = np.random.choice(opciones, 2, replace = False)
            for j in range(2):
                xhat[i][j] = x[0][j] + F*(x[indices[0]][j]-x[indices[1]][j])
            xhat[i][2] = fobj((xhat[i][0], xhat[i][1]))
            #'''
            # Mutacion 3
            '''
            # Ordenamos la poblacion para obtener al mejor
            x = x[x[:,2].argsort()]
            opciones = np.delete(lista,[i,0])
            indices = np.random.choice(opciones, 4, replace = False)
            for j in range(2):
                xhat[i][j] = x[0][j] + F*(x[indices[0]][j] + x[indices[1]][j] - x[indices[2]][j] - x[indices[3]][j])
            xhat[i][2] = fobj((xhat[i][0], xhat[i][1]))
            '''
            # Mutacion 4
            '''
            # Ordenamos la poblacion para obtener al mejor
            x = x[x[:,2].argsort()]
            F1 = F
            F2 = F1 + 0.1
            opciones = np.delete(lista,[i,0])
            indices = np.random.choice(opciones, 3, replace = False)
            for j in range(2):
                xhat[i][j] = x[indices[0]][j] + F1*(x[0][j] - x[indices[0]][j]) + F2*(x[indices[1]][j] - x[indices[2]][j])
            xhat[i][2] = fobj((xhat[i][0], xhat[i][1]))
            '''
            # Mutacion 5
            '''
            F1 = F
            F2 = F1 + 0.1
            opciones = np.delete(lista,i)
            indices = np.random.choice(opciones, 5, replace = False)
            for j in range(2):
                xhat[i][j] = x[indices[0]][j] + F1*(x[indices[1]][j] - x[indices[2]][j]) + F2*(x[indices[3]][j] - x[indices[4]][j])
            xhat[i][2] = fobj((xhat[i][0], xhat[i][1]))
            '''
            # Recombinacion
            I_i = np.random.choice([0,1])
            for j in range(2):
                R_j = random.uniform(0,1)
                if  R_j <= CR or j == I_i:
                    y[i][j] = xhat[i][j]
                else:
                    y[i][j] = x[i][j]
            y[i][2] = fobj((y[i][0],y[i][1]))
            # Seleccion
            if y[i][2] < x[i][2]:
                for j in range(3):
                    Q[i][j] = y[i][j]
            else:
                for j in range(3):
                    Q[i][j] = x[i][j]
        x = Q
        k += 1
    return x

#Parametros
N = 10
F = 0.5
CR = 0.1
k_max = 150
print(Busq_ED(N, F, CR, k_max))
            


