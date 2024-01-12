import random
import numpy as np
import matplotlib.pyplot as plt
import math

# Definimos la funcion objetivo
def fobj(x):
    z = 0.5*((x[0]**4 - 16*x[0]**2 +5*x[0])+(x[1]**4 - 16*x[1]**2 +5*x[1]))
    return z
# Definimos el espacio de busqueda
limX= [-4, 4] #Eje X
limY= [-4, 4] #Eje Y
# Valores iniciales
N = 50                 #Numero de iteraciones
opt = -78.33            #Solucion optima
mu = 10                  #Numero de padres
#Creamos a los padres
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
# Crea a los padres con su resp. sigma
def crea_padres_1(n, sigma):
    '''
    Funcion que genera n padres
    '''
    xpob = np.zeros((n,4))
    for i in range(n):
        for j in range(2):
            xpob[i][j] = random.uniform(limX[0], limX[1])
        xpob[i][2] = fobj((xpob[i][0],xpob[i][1]))
        xpob[i][3] = sigma
    return xpob
# Crea a los padres con sigma para cada entrada
def crea_padres_2(n, sigma):
    '''
    Funcion que genera n padres
    '''
    xpob = np.zeros((n,5))
    for i in range(n):
        for j in range(2):
            xpob[i][j] = random.uniform(limX[0], limX[1])
        xpob[i][2] = fobj((xpob[i][0],xpob[i][1]))
        xpob[i][3] = sigma
        xpob[i][4] = sigma
    return xpob
# Crea a los padres con sigma y alpha para cada entrada
def crea_padres_3(n, sigma, alpha):
    '''
    Funcion que cre n padres
    '''
    xpob = np.zeros((n, 6))
    for i in range(n):
        for j in range(2):
            xpob[i][j] = random.uniform(limX[0], limX[1])
        xpob[i][2] = fobj((xpob[i][0],xpob[i][1]))
        xpob[i][3] = sigma
        xpob[i][4] = sigma
        xpob[i][5] = alpha
    return xpob

def signo(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1

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
    #plt.show()
    return
# Mutacion caso 1 
def mutacion1(individuo):
    epsilon_0 = 0.0001
    N_c = np.random.normal(0,1)
    tao = 1/(math.sqrt(2))
    sigma = individuo[3]
    sigmahat = sigma*math.exp(tao*N_c)
    if sigmahat < epsilon_0:
        sigmahat = epsilon_0
    individuo[0] = individuo[0] + sigmahat* np.random.normal(0,1)
    individuo[1] = individuo[1] + sigmahat* np.random.normal(0,1)
    individuo[2] = fobj((individuo[0],individuo[1]))
    individuo[3] = sigmahat
    return individuo
# Mutacion caso 2
def mutacion2(individuo):
    epsilon_0 = 0.0001
    N_c = np.random.normal(0,1)
    tao = 1/(math.sqrt(2*math.sqrt(2)))  
    tao_0 = 1/math.sqrt(4)
    sigmahat = [0, 0]
    for i in range(2):
        sigmahat[i] = individuo[i+3]*math.exp(tao_0*N_c + tao*np.random.normal(0,1))
        if sigmahat[i] < epsilon_0:
            sigmahat[i] = epsilon_0
        individuo[i] = individuo[i] + sigmahat[i]*np.random.normal(0,1)
        individuo[i+3] = sigmahat[i]
    individuo[2] = fobj((individuo[0],individuo[1]))
    return individuo
# Mutacion caso 3
def mutacion3(individuo):
    epsilon_0 = 0.0001
    N_c = np.random.normal(0,1)
    tao = 1/(math.sqrt(2*math.sqrt(2)))  
    tao_0 = 1/math.sqrt(4)
    sigmahat = [0, 0]
    beta = 0.0873
    alpha = individuo[5]
    for i in range(2):
        sigmahat[i] = individuo[i+3]*math.exp(tao_0*N_c + tao*np.random.normal(0,1))
        if sigmahat[i] < epsilon_0:
            sigmahat[i] = epsilon_0
    alphahat = alpha + beta*np.random.normal(0,1)
    if abs(alphahat) > math.pi:
        alphahat = alphahat - 2*(math.pi)*signo(alphahat)
    y = np.zeros(2)
    for i in range(2):
        y[i] = sigmahat[i]*np.random.normal(0,1)
    y[0] = y[0]*math.cos(alphahat) - y[1]*math.sin(alphahat)
    y[1] = y[0]*math.sin(alphahat) + y[1]*math.cos(alphahat)
    for i in range(2):
        individuo[i] = individuo[i] + y[i]
        individuo[i+3] = sigmahat[i]
    individuo[2] = fobj((individuo[0],individuo[1]))
    individuo[5] = alphahat 
    return individuo
# Busqueda aleatoria localizada
def Busq_ES(mu, N, sigma, alpha):
    '''
    Argumentos:
    mu : no. de elementos de los padres
    N : no. maximo de iteraciones
    sigma : desv. estandar (paso de mutacion)
    '''
    iter = 0
    #var_lambda = 7*mu
    var_lambda = 4*mu
    xpob = crea_padres_3(mu, sigma, alpha)
    len = xpob.shape[0]
    padres = np.arange(len)
    # Se crean lambda hijos
    xhat = np.zeros((var_lambda,6))
    while iter < N:
        graficar(xpob, iter)
        iter +=1
        # Recombinacion intermedia local
        for i in range(var_lambda):
            eleccion = np.random.choice(padres, 2, replace = False)
            for j in range(2):
                xhat[i][j] = xpob[eleccion[0]][j] + random.uniform(0,1)*(xpob[eleccion[1]][j]-xpob[eleccion[0]][j])
        # Mutacion Caso 1
        '''
        for i in range(var_lambda):
            xhat[i] = mutacion1(xhat[i])
        '''
        # Mutacion Caso 2
        '''
        for i in range(var_lambda):
            xhat[i] = mutacion2(xhat[i])
        '''
        # Mutacion caso 3
        for i in range(var_lambda):
            xhat[i] = mutacion3(xhat[i])
        # Seleccion
        # Elegimos a los mejores mu hijos
        xpob = xhat[xhat[:,2].argsort()]
        xpob = xpob[0:mu,:]
    return xpob
#splt.show()
print(Busq_ES(mu, N, .5, .4))
plt.show()
