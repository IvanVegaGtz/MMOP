import numpy as np
from sympy import *
import matplotlib.pyplot as plt
import math
from collections import OrderedDict

linestyles_dict = OrderedDict(
    [('solid',               (0, ())),
     ('loosely dotted',      (0, (1, 10))),
     ('dotted',              (0, (1, 5))),
     ('densely dotted',      (0, (1, 1))),

     ('loosely dashed',      (0, (5, 10))),
     ('dashed',              (0, (5, 5))),
     ('densely dashed',      (0, (5, 1))),

     ('loosely dashdotted',  (0, (3, 10, 1, 10))),
     ('dashdotted',          (0, (3, 5, 1, 5))),
     ('densely dashdotted',  (0, (3, 1, 1, 1))),

     ('loosely dashdotdotted', (0, (3, 10, 1, 10, 1, 10))),
     ('dashdotdotted',         (0, (3, 5, 1, 5, 1, 5))),
     ('densely dashdotdotted', (0, (3, 1, 1, 1, 1, 1)))])

def Euler(a, b, y0, h, fun):
    print("Metodo de Euler")
    Y = [y0]
    T = [a]
    i = 0
    print("t = {}, y = {}".format(T[i], Y[i]))
    while T[i] < b:
        Y.append(Y[i] + h*fun.subs({t:T[i], y:Y[i]}))
        T.append(T[i] + h)
        i += 1
        print("t = {}, y = {}".format(T[i], Y[i]))
    return  Y
   
def Taylor_orden_2(a, b, y0, h, fun):
    print("Metodo de Taylor orden 2")
    # Hallamos las derivadas parciales
    parcial_f_t = fun.diff(t)
    parcial_f_y = fun.diff(y)
    k11 = parcial_f_t + fun * parcial_f_y
    # Inicializamos los arreglos para t,y
    T = [a]
    Y = [y0]
    i = 0
    print("t = {}, y = {}".format(T[i], Y[i]))
    while T[i] < b:
        K1 = fun.subs({t:T[i], y:Y[i]})
        K2 = k11.subs({t:T[i], y:Y[i]})
        Y.append(Y[i] + h*K1 + ((h**2)/2)*K2)
        T.append(T[i] + h)
        i += 1
        print("t = {}, y = {}".format(T[i], Y[i]))
    return Y
 
def Taylor_orden_4(a, b, y0, h, fun):
    print("Metodo de Taylor orden 4")
    # Hallamos las derivadas parciales
    f_t = fun.diff(t)
    f_ty = f_t.diff(y)
    f_tt = f_t.diff(t)
    f_tty = f_tt.diff(y)
    f_ttt = f_tt.diff(t)
    f_y = fun.diff(y)
    f_yy = f_y.diff(y)
    f_yyt = f_yy.diff(t)
    f_yyy = f_yy.diff(y)
    K11 =fun
    K22 = f_t + f_y*fun
    K33 = f_tt + 2*f_ty*fun + f_yy*fun**2 + f_y*f_t + fun*f_y**2
    K44 = f_ttt + f_tt*(2*f_ty+f_y) + f_t*(2*f_yy*fun + f_y**2) + 3*fun*(f_tty + f_yyt*fun) + f_ty*(3*f_y*fun + f_t + 2*f_y) + fun*f_y**3 + f_yy*(2*f_y*fun**2 + f_t*fun + 2*f_y*fun) + f_yyy*fun**3
    # Inicializamos los arreglos para t,y
    T = [a]
    Y = [y0]
    i = 0
    print("t = {}, y = {}".format(T[i], Y[i]))
    while T[i] < b:
        K1 = K11.subs({t:T[i], y:Y[i]})
        K2 = K22.subs({t:T[i], y:Y[i]})
        K3 = K33.subs({t:T[i], y:Y[i]})
        K4 = K44.subs({t:T[i], y:Y[i]})
        #print(K1, K2, K3, K4)
        Y.append(Y[i] + h*K1 + ((h**2)/2)*K2 + K3*((h**3)/6) + K4*((h**4)/24))
        T.append(T[i] + h)
        i += 1
        print("t = {}, y = {}".format(T[i], Y[i]))
    return Y

def RK_2(a, b, y0, h, fun):
    print("Metodo Runge-Kutta de orden 2")
    T = [a]
    Y = [y0]
    print("t = {}, y = {}".format(T[0], Y[0]))
    i = 0
    while T[i] < b:
        k1 = h*fun.subs({t:T[i],y:Y[i]})
        k2 = h*fun.subs({t:T[i]+ h, y:Y[i] + k1})
        Y.append( Y[i] + 0.5*(k1+k2) )
        T.append(T[i] + h)
        i +=1
        print("t = {}, y = {}".format(T[i], Y[i]))
    return Y

def RK_4(a, b, y0, h, fun):
    print("Metodo Runge-Kutta de orden 4")
    T = [a]
    Y = [y0]
    print("t = {}, y = {}".format(T[0], Y[0]))
    i = 0
    while T[i] < b:
        k1 = h*fun.subs({t:T[i],y:Y[i]})
        k2 = h*fun.subs({t:T[i]+ 0.5*h, y:Y[i] + 0.5*k1})
        k3 = h*fun.subs({t:T[i]+ 0.5*h, y:Y[i] + 0.5*k2})
        k4 = h*fun.subs({t:T[i]+ h, y:Y[i] + k3})
        Y.append(Y[i] + (k1 + 2*k2 + 2*k3 + k4)/6)
        T.append(T[i] + h)
        i +=1
        print("t = {}, y = {}".format(T[i], Y[i]))
    return  Y


# ================Ejercicio 1 ========================
# Parametros
t = Symbol('t')
y = Symbol('y')
a = 0
b = 2
y0 = 1
h = 0.25
N = int((b-a)/h)
T = np.linspace(a, b, N+1)
funcion1 = -y
# Resultados para el inciso A)
print('Ecuacion dy/dt = {}'.format(funcion1))
sol1 = [math.exp(-t) for t in T]
print("Solucion analitica")
for i in range(len(T)):
    print("i ={}, y = {}".format(T[i], round(sol1[i],6)))
E1 = Euler(a, b, y0, h, funcion1)
T21 = Taylor_orden_2(a, b, y0, h, funcion1)
T41 = Taylor_orden_4(a, b, y0, h, funcion1)
RK21 = RK_2(a, b, y0, h, funcion1)
RK41 = RK_4(a, b, y0, h, funcion1)

print('Errores')
for i in range(len(T)):
    print("t = {}, Euler = {}, T2 = {}, T4 ={}, RK2={}, RK4={}".format(T[i],round(sol1[i]-E1[i],6),round(sol1[i]- T21[i],6),round(sol1[i]- T41[i],6),round(sol1[i]- RK21[i],6),round(sol1[i]- RK41[i],6)))
plot1 = plt.figure(1)
plt.plot(T, sol1, label = 'Solución análitica')
plt.plot(T, E1, label = 'Euler', )
plt.plot(T, T21, label = 'Taylor orden 2')
plt.plot(T, T41, label = 'Taylor orden 4',marker = '*', linestyle = linestyles_dict['loosely dashed'])
plt.plot(T, RK21, label = 'Runge-Kutta orden 2', linestyle = 'dashed')
plt.plot(T, RK41, label = 'Runge-Kutta orden 4', linestyle = linestyles_dict['densely dashed'])
plt.xlabel("Tiempo (t)")
plt.ylabel("Solución Numérica de y(t)")
plt.title('Ecuacion dy/dt = {}'.format(funcion1), fontsize=13)
plt.legend()
# Resultados para el inciso B)
funcion2 = t*y
print('\n Ecuacion dy/dt = {}'.format(funcion2))
sol2 = [math.exp(0.5*t**2) for t in T]
print("Solucion analitica")
for i in range(len(T)):
    print("i={}, y = {}".format(T[i], round(sol2[i], 6)))
E2 = Euler(a, b, y0, h, funcion2)
T22 = Taylor_orden_2(a, b, y0, h, funcion2)
T42 = Taylor_orden_4(a, b, y0, h, funcion2)
RK22 = RK_2(a, b, y0, h, funcion2)
RK42 = RK_4(a, b, y0, h, funcion2)
print('Errores')
for i in range(len(T)):
    print("t = {}, Euler = {}, T2 = {}, T4 ={}, RK2={}, RK4={}".format(T[i],round(sol2[i]-E2[i],6),round(sol2[i]- T22[i],6),round(sol2[i]- T42[i],6),round(sol2[i]- RK22[i],6),round(sol2[i]- RK42[i],6)))
plot2 = plt.figure(2)
plt.plot(T, sol2, label = 'Solución análitica')
plt.plot(T, E2, label = 'Euler')
plt.plot(T, T22, label = 'Taylor orden 2')
plt.plot(T, T42, label = 'Taylor orden 4', linestyle = linestyles_dict['loosely dashed'])
plt.plot(T, RK22, label = 'Runge-Kutta orden 2', linestyle = 'dashed')
plt.plot(T, RK42, label = 'Runge-Kutta orden 4', linestyle = linestyles_dict['densely dashed']) 
plt.xlabel("Tiempo (t)")
plt.ylabel("Solución Numérica de y(t)")
plt.title('Ecuacion dy/dt = {}'.format(funcion2), fontsize=13)
plt.legend()
plt.show()
#===========================EJERCICIO 2 ALTERNATIVA================================
'''
# Parametros
t = Symbol('t')
y = Symbol('y')
a = 0
b = 1
y_0 = 0
h = 0.1
fun1 = 0.05*y - 0.15
print("Solucion  y''  ") 
U = Euler(a, b, 0.05, h, fun1)

def fun(u, y):
    f = (u + 0.15*y)/0.05
    return f

def Euler2(a, b, y0, U, h):
    Y = [y0]
    T = [a]
    i = 0
    while T[i] < b:
        Y.append(Y[i] + h*fun(U[i], Y[i]))
        T.append(T[i] + h)
        i += 1
    return  T,Y
#Resultados
T, Y = Euler2(a,b, y_0,U, h)
print('\n Resultados')
for i in range(len(T)):
    print("t = {}, y = {},  y' ={}".format(T[i], Y[i], (U[i] + 0.15*Y[i])/0.05))
'''
