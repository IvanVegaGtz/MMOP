import random
import numpy as np
import matplotlib.pyplot as plt


def evalua(xpob):
    n,m = xpob.shape
    for i in range(n):
        xpob[i,m-1] = np.sum(xpob[i,:m-1])
    return xpob 

def estima(xpob):
    n,m = xpob.shape
    prob = []
    tam = len(xpob[:,0])
    for i in range(m-1):
        prob.append(np.sum(xpob[:,i])/tam)
    return prob

# EDA
def UMDA(N,n, M, iter):
    '''
    N : tamano de la poblacion
    n : numero de variables
    M : tamano de seleccion
    iter: numero maximo de iteraciones    
    '''
    # Poblacion inicial
    k = 0
    xpob = np.zeros((N,n+1))
    xpob_selec = np.zeros((M,n+1))
    for i in range(n):
            xpob[:,i] = np.random.binomial(1,.5, N)
    #xpob[:,:n] = np.random.randint(2, size=(N,n))
    xpob = evalua(xpob)
    while k < iter:
        # Seleccion
        xpob = xpob[xpob[:,n].argsort()]
        xpob_selec = xpob[N-M:N,:]
        # Estimacion
        prob= estima(xpob_selec)
        # Muestreo
        for i in range(len(prob)):
            xpob[:,i] = np.random.binomial(1,prob[i], N)
        xpob = evalua(xpob)
        print("iter = {} \n {}".format(k,xpob))
        k += 1
    return xpob

UMDA(10,10,5,15)
