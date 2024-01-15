import random
import numpy as np
import matplotlib.pyplot as plt
import math

#Valores iniciales
x0 = np.array([4, 4]) #Vector inicial
N = 500                 #Numero de iteraciones
n = 40                  #Numero de ejecuciones del algoritmo
opt = -78.33            #Solucion optima
# Definimos el espacio de busqueda
limX= [-4, 4] #Eje X
limY= [-4, 4] #Eje Y
# Definimos la funcion objetivo
def fobj(x):
    z = 0.5*((x[0]**4 - 16*x[0]**2 + 5*x[0])+ (x[1]**4 - 16*x[1]**2 + 5*x[1]))
    return z
# Graficarmos
def graficar():
    xx = np.linspace(limX[0], limX[1])
    yy = np.linspace(limY[0], limY[1])
    X, Y =  np.meshgrid(xx, yy)
    Z = fobj([X,Y])
    plt.contour(X, Y, Z, levels=16, cmap=plt.get_cmap('jet'))
    plt.title('Algoritmo de recocido simulado')
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.xlim(limX[0], limX[1])
    plt.ylim(limY[0], limY[1])
    #plt.show()
    return 
# Algoritmo de recocido simulado con BAS
def SA(x, N, Temp):
    iter = 0
    mu = 0
    sigma = 1
    graficar()
    plt.scatter(x[0],x[1], c = "blue")
    while iter < N:
        iter +=1
        d = np.random.normal(mu, sigma, 2)
        xhat = x + d
        if fobj(xhat) < fobj(x):
            #plt.pause(.001)
            plt.scatter(xhat[0], xhat[1], c = 'r')
            x = xhat
        else:
            r = np.random.uniform(0,1,1)
            if r < math.exp((fobj(x) - fobj(xhat))/Temp):
                #plt.pause(.001)
                plt.scatter(xhat[0], xhat[1], c = 'green')
                x = xhat
        Temp = 0.99*Temp
    plt.scatter(x[0], x[1], c = 'black', marker= '*')
    #plt.show()
    print('T_final = ', Temp)
    return x, fobj(x)

#graficar()
print(SA(x0, 1000, 200)[1])
plt.show()
