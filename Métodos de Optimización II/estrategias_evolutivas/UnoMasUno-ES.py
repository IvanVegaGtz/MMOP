import random
import numpy as np
import matplotlib.pyplot as plt


# Definimos la funcion objetivo
def fobj(x):
    z = 0.5*((x[0]**4 - 16*x[0]**2 +5*x[0])+(x[1]**4 - 16*x[1]**2 +5*x[1]))
    return z
# Definimos el espacio de busqueda
limX= [-4, 4] #Eje X
limY= [-4, 4] #Eje Y
# Funcion para graficar 
def graficar():
    xx = np.linspace(limX[0], limX[1])
    yy = np.linspace(limY[0], limY[1])
    X, Y =  np.meshgrid(xx, yy)
    Z = fobj([X,Y])
    plt.contour(X, Y, Z, levels=16, cmap=plt.get_cmap('jet'))
    plt.title('Estrategia evolutiva (1+1) Regla 1/5')
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.xlim(limX[0], limX[1])
    plt.ylim(limX[0], limX[1])
    #plt.show()
    return 
# Busqueda aleatoria localizada

def Busq_ES(N, c, sigma, h):
    '''
    Argumentos:
    x : vector inicial
    N : no. maximo de iteraciones
    c : valor numerico entre 0.8 y 1
    sigma : desv. estandar (paso de mutacion)
    h : ajusta sigma cada h iteraciones
    '''
    iter = 0
    exito = 0
    graficar()
    # Inicializacion
    x = np.random.uniform(limX[0], limX[1], 2)
    plt.scatter(x[0],x[1], c = "b")
    while iter < N:
        iter +=1
        #Mutacion
        d = np.random.normal(0, sigma, 2)
        xhat = x + d
        #Seleccion
        if fobj(xhat) < fobj(x):
            plt.pause(.1)
            plt.arrow(x[0],x[1], xhat[0] - x[0], xhat[1] - x[1], head_width=0.1)
            plt.scatter(xhat[0], xhat[1], c='green')
            x = xhat
            exito += 1
        else:
            plt.scatter(xhat[0], xhat[1], c='r')
        # Regla de Rochenberg de 1/5
        if iter%h ==0:
            ps = exito/h
            exito = 0
            if ps < 1/5:
                sigma = sigma*c
            elif ps > 1/5:
                sigma = sigma/c
    plt.show()
    return x


# Valores iniciales
N = 300                 
c = 0.917               
sigma = 0.4
h = 10
# Resultado
print(fobj(Busq_ES(N, c, sigma, h)))


