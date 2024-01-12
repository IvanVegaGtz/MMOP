import numpy as np
import random

def fobj(x):
    z = 0.5*((x[0]**4 - 16*x[0]**2 +5*x[0])+(x[1]**4 - 16*x[1]**2 +5*x[1]))
    #z = -20*np.exp(-0.2*np.sqrt(0.5*(x[0]**2 + x[1]**2))) - np.exp(0.5*(np.cos(2*np.pi*x[0]) + np.cos(2*np.pi*x[1]))) + 20 + np.exp(1)
    return z


min = -4
max = 4
N = 10
D = 2
xpob = np.random.uniform(min, max, size=(N, D))
fun = fobj
reemplazo = True

def torneo(xpob, fun, reemplazo):
    '''
    Argumentos:
    xpob: matriz que contiene la poblacion inicial
    fun : funcion objetivo
    reemplazo : booleano que determina si el torneo es con sustitucion
                True con sustitucion y False sin sustitucion
    '''
    N, n= xpob.shape
    x_new = np.zeros((N,n)) 
    individuos = np.arange(N)
    competidor = np.random.choice(individuos, N, replace = reemplazo)
    for i in range(N):
        if fun(xpob[competidor[i], :]) < fun(xpob[i, :]):
            x_new[i,:] = xpob[competidor[i], :]
        else:
            x_new[i,:] = xpob[i, :]
    return x_new

print(torneo(xpob, fun, reemplazo))