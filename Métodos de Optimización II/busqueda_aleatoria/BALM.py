import random
import numpy as np
import matplotlib.pyplot as plt

#Valores iniciales
x0 = np.array([4, 6.4]) #Vector inicial
N = 500                 #Numero de iteraciones
n = 40                  #Numero de ejecuciones del algoritmo
opt = -78.33            #Solucion optima
# Definimos el espacio de busqueda
limX= [-8, 8] #Eje X
limY= [-8, 8] #Eje Y
# Definimos la funcion objetivo
def fobj(x):
    z = 0.5*((x[0]**4 - 16*x[0]**2 +5*x[0])+(x[1]**4 - 16*x[1]**2 +5*x[1]))
    return z
# Funcion para graficar 
def graficar():
    xx = np.linspace(limX[0], limX[1])
    yy = np.linspace(limY[0], limY[1])
    X, Y =  np.meshgrid(xx, yy)
    Z = fobj([X,Y])
    plt.contour(X, Y, Z, levels=16, cmap=plt.get_cmap('jet'))
    plt.title('Búsqueda aleatoria localizada mejorada')
    plt.xlabel("x1")
    plt.ylabel("x2")
    #plt.show()
    return 
# Busqueda aleatoria localizada mejorada
def BALM(x, N): 
    # Paso 0 Inicializacion
    iter = 0
    mu = 0
    sigma = 3**0.5
    b = np.array([0, 0])
    #graficar()
    #plt.scatter(x[0],x[1], c = "red")
    while iter < N:
        iter += 1
        # Paso 1 Generar el vector independiente dk
        band = True
        while band:
            d = np.random.normal(mu, sigma, 2)
            xhat = x + b + d
            # Verificamos que el vector se encuentre en el espacio de busqueda
            if limX[0] <= xhat[0] <= limX[1] and limY[0] <= xhat[1] <= limY[1]:
                band = False
        # Paso 2
        if fobj(xhat) < fobj(x):
            #plt.pause(1)
            #plt.arrow(x[0],x[1], xhat[0] - x[0], xhat[1] - x[1], head_width=0.2)
            x = xhat
            b = 0.2*b + 0.4*d
        # Paso 3
        else :
            xhat = x + b - d
            if limX[0] <= xhat[0] <= limX[1] and limY[0] <= xhat[1] <= limY[1]:
                if fobj(xhat) < fobj(x):
                    #plt.pause(1)
                    #plt.arrow(x[0],x[1], xhat[0] - x[0], xhat[1] - x[1], head_width=0.2)
                    x = xhat
                    b = b - 0.4*d
                # Paso 4
                else:
                    b = 0.5*b
            # Paso 3
            else:
                band = True
                while band:
                    d = np.random.normal(mu, sigma, 2)
                    xhat = x +b + d
                    if limX[0] <= xhat[0] <= limX[1] and limY[0] <= xhat[1] <= limY[1]:
                        band = False
                if fobj(xhat) < fobj(x):
                    #plt.pause(1)
                    #plt.arrow(x[0],x[1], xhat[0] - x[0], xhat[1] - x[1], head_width=0.2)
                    x = xhat
                    b = b - 0.4*d
                else:
                    b = 0.5*b
    #plt.show()
    return x, fobj(x)
# Numero de ejecuciones del algoritmo
def ejecuciones(n):
    res = []
    dif = np.zeros(n)
    sol = np.zeros(n)
    print('Ejec', '     x1          ', '        x2        ', '      f(x)')
    for i in range(n):
        res.append(BALM(x0,N))
        dif[i] = res[0][1] - opt
        sol[i] = res[0][1]
        print(i+1, res[0][0][0], res[0][0][1], res[0][1])
        res.pop()
    return dif, sol

muestra = ejecuciones(n)
media = np.mean(muestra[0])
varianza = np.var(muestra[0])
print('La peor solucion es ')
print(np.max(muestra[1]))
print('La mejor solucion es')
print(np.min(muestra[1]))
print('La media es:')
print(media)
print('La varianza es:')
print(varianza)
print("El intervalo de confianza es")
k = 2.023*(varianza/40)**0.5
print("[ {} , {} ]".format(media - k, media + k))
