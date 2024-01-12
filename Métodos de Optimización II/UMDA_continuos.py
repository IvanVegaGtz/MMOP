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
    plt.pause(0.01)

def evalua(xpob):
    n = xpob.shape[0]
    for i in range(n):
        xpob[i,2] = fobj(xpob[i,:2])
    return xpob 

def estima(xpob):
    n,m = xpob.shape
    media = []
    desv_est = []
    for i in range(m-1):
        media.append(np.mean(xpob[:,i]))
        desv_est.append(np.std(xpob[:,i]))
    return media,desv_est


# EDA
def UMDA(N, M, iter):
    '''
    N : tamano de la poblacion
    M : tamano de seleccion
    iter: numero maximo de iteraciones    
    '''
    # Poblacion inicial
    k = 0
    xpob = np.zeros((N,3))
    xpob_selec = np.zeros((M,3))
    xpob[:,:2] = np.random.uniform(limX[0], limX[1], size=(N, 2))
    xpob = evalua(xpob)
    graficar(xpob,k)
    while k < iter:
        # Seleccion
        xpob = xpob[xpob[:,2].argsort()]
        graficar(xpob,k)
        xpob_selec = xpob[:M,:]
        # Estimacion
        mu, sigma = estima(xpob_selec)
        # Muestreo
        for i in range(len(mu)):
            xpob[:,i] = np.random.normal(mu[i], sigma[i], N)
        xpob = evalua(xpob)
        k += 1
    return xpob

print(UMDA(100,50, 50))
