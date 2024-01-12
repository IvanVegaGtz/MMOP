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
n = 10                  #Numero de padres

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
    xpob = xpob[xpob[:,2].argsort()]
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
    return
# Funcion que halla al peor y mejor pare, regresa los indices indices
def PeorMejor(padres):
    y = padres[:,2]
    peor = y[0]
    mejor = y[0]
    pos_peor = 0
    pos_mejor = 0
    for i in range(1,len(y)):
        if y[i] > peor:
            peor = y[i]
            pos_peor = i
        if y[i] < mejor:
            mejor = y[i]
            pos_mejor = i
    return pos_peor, pos_mejor
# Funcion que reemplaza al peor padre por el hijo
def reemplazo(hijo, pos, poblacion):
    poblacion[pos][0] = hijo[0]
    poblacion[pos][1] = hijo[1]
    poblacion[pos][2] = hijo[2]
    return poblacion

# Busqueda aleatoria localizada
def Busq_ES(n, N, sigma):
    '''
    Argumentos:
    n : no. de elementos de los padres
    N : no. maximo de iteraciones
    sigma : desv. estandar (paso de mutacion)
    '''
    iter = 0
    xpob = crea_padres(n)
    len = xpob.shape[0]
    padres = np.arange(len)
    # Hijo
    xhat = [0 , 0, 0]
    while iter < N:
        graficar(xpob, iter)
        iter +=1
        # Se seleccionan dos padres
        eleccion = np.random.choice(padres, 2, replace = False)
        # Recombinacion discreta local
        '''
        for i in range(2):   
            if random.random() > 0.5:
                xhat[i] = xpob[eleccion[0]][i]
            else:
                xhat[i] = xpob[eleccion[1]][i]
        '''
        # Recombinacion intermedia local
        for i in range(2):
            xhat[i] = xpob[eleccion[0]][i] + random.uniform(0,1)*(xpob[eleccion[1]][i]-xpob[eleccion[0]][i])
        # Mutacion
        xhat[0] = xhat[0] + np.random.normal(0,sigma)
        xhat[1] = xhat[1] + np.random.normal(0,sigma)
        xhat[2] = fobj((xhat[0],xhat[1]))
        # Reemplazo
        pos_peor, pos_mejor = PeorMejor(xpob)
        xpob = reemplazo(xhat, pos_peor, xpob)
        #print(xpob)
    return xpob


#splt.show()
print(Busq_ES(n, 100, .5))

