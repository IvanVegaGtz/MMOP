import numpy as np
import matplotlib.pyplot as plt
def esquema(dx,dt):
    '''
    Funcion que grafica la solucion numerica y exacta
    Parametros:
    dx : tamano de paso en la variable x
    dt : tamano de paso en la variable t
    '''
    xi=0
    xf=10
    ti=0
    tf=25
    espx = int(xf//dx)+1
    espt = int(tf//dt)+1 
    x=np.linspace(xi,xf,espx) 
    t=np.linspace(ti,tf,espt) 
    s=dt/(dx**2)
    #Solucion diferencias finitas
    un=np.zeros((espt,espx))
    #Condiciones de frontera
    un[0,:-1]=np.sin((np.pi*x[:-1])/10)
    # Esquema explicito
    for j in range(0,espt-1):
        for i in range(1,espx-1):
            un[j+1,i]=s*un[j,i-1]+(1-2*s)*un[j,i]+s*un[j,i+1]
    fig,ax=plt.subplots()
    g=ax.contourf(x,t,un)
    fig.colorbar(g)
    ax.set_title(r"Esquema explícito de diferencias finitas con $\Delta x = {}$ y $\Delta t = {}$".format(dx,dt))
    ax.set_xlabel("x")
    ax.set_ylabel("t")
    plt.show()
    #Solución exacta 
    solution=np.zeros((espt,espx)) 
    for j in range(0,espt):
        for i in range(0,espx): 
            solution[j,i]= np.sin((np.pi*x[i])/10)*(np.exp(-((np.pi/10)**2)*t[j]))
    fig,ax=plt.subplots()
    g=ax.contourf(x,t,solution)
    fig.colorbar(g)
    ax.set_title("Solución exacta")
    ax.set_xlabel("x")
    ax.set_ylabel("t")
    plt.show()
    error = []
    for i in range(espt):
        error.append(max(np.abs(un[i]-solution[i]))) 
    return error

# Probar inestabilidad variando deltat
'''
T = np.linspace(0, 1, 100)
print(T)
for i in range(len(T) -1):
    esquema(0.5, T[i+1])
'''
#sol_est = esquema(0.5, 0.005)
#sol_inest = esquema(0.5, 0.145)



# Comparar errores maximos
sol1 = esquema(0.5, 0.125)
tam1 =  int(25//0.125)+1 
t1=np.linspace(0,25,tam1)
delta_t2 = ((0.25)**2)/2
sol2 = esquema(0.25,delta_t2) 
tam2 =  int(25//delta_t2)+1 
t2=np.linspace(0,25,tam2)
# Grafica de errores
plt.plot(t1,sol1, label=r"$\Delta x = 0.5$, $\Delta t = 0.125$") 
plt.plot(t2,sol2,label=r"$\Delta x = 0.25$, $\Delta t = (0.25)^2 /2$") 
plt.xlabel("t")
plt.ylabel("Error máximo")
plt.title("Comparación del error")
plt.legend()
plt.grid()
plt.show()


