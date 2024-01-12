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
# Valores iniciales
N = 300                 #Numero de iteraciones
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
# Busqueda aleatoria localizada
def Busq_ES(mu, N, sigma):
    '''
    Argumentos:
    mu : no. de elementos de los padres
    N : no. maximo de iteraciones
    sigma : desv. estandar (paso de mutacion)
    '''
    iter = 0
    var_lambda = 7*mu
    # var_lambda = 4*mu
    xpob = crea_padres(mu)
    len = xpob.shape[0]
    padres = np.arange(len)
    # Se crean lambda hijos
    xhat = np.zeros((var_lambda,3))
    while iter < N:
        graficar(xpob,iter)
        iter +=1
        # Recombinacion intermedia local
        for i in range(var_lambda):
            eleccion = np.random.choice(padres, 2, replace = False)
            for j in range(2):
                xhat[i][j] = xpob[eleccion[0]][j] + random.uniform(0,1)*(xpob[eleccion[1]][j]-xpob[eleccion[0]][j])
        # Mutacion
        for i in range(var_lambda):
            xhat[i][0] = xhat[i][0] + np.random.normal(0,sigma)
            xhat[i][1] = xhat[i][1] + np.random.normal(0,sigma)
            xhat[i][2] = fobj((xhat[i][0],xhat[i][1]))
        # Reemplazo
        # Elegimos a los mejores mu hijos
        xpob = xhat[xhat[:,2].argsort()]
        xpob = xpob[0:mu,:]
    return xpob
#splt.show()
print(Busq_ES(mu, 300, .5)[0][2])

