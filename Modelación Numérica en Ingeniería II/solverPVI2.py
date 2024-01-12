import numpy as np
from sympy import *

def Euler_2(a,b,y_0, y_prima_0, h, fun):
    '''
    Calcula la solucion de una ecuacion diferencial de segundo orden
    mediante el metodo de Euler
    Arugmentos:
    a : limite izquierdo del intervalo de la funcion
    b : limite derecho del intervalo de la funcion
    y_0 : valor inicial de la funcion y en el tiempo t_0
    y_prima_0 : valor inicial de la derivda de la funcion en t_o
    h : tamano de paso
    fun : ecuacion diferencial que queremos resolver, debe estar de la forma
          fun = y'' = by'(t) +cy(t) +d = f(t,y,y')
    Salida
    T : vector que contiene la particion de la variable independiente t
    Y : vector que contiene la solucion y en cada punto t_i en (a,b)
    U : vector que coneiten la solucion y' en cada punto t_i en (a,b)
    '''
    Y = [y_0]
    U = [y_prima_0]
    T = [a]
    i = 0
    while T[i] < b:
        Y.append(Y[i] + h*U[i])
        U.append(U[i] + h*funcion.subs({t:T[i], y_prima:U[i], y:Y[i]}))
        T.append(T[i] + h)
        i += 1
    return T, Y, U

# PARAMETROS
t = Symbol('t')
y = Symbol('y')
y_prima = Symbol('y_prima')
a = 0
b = 1
y_0 = 0
y_prima_0 = 1
h = 0.1
funcion = 0.05*y_prima - 0.15*y
# IMPRESION DE RESULTADOS
T, Y, U = Euler_2(a,b,y_0, y_prima_0, h, funcion)
N = len(T)
for i in range(N):
    print("t = {},  y = {}, y' = {}  ".format(T[i], Y[i], U[i]))

