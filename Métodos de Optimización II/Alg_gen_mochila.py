import numpy as np
import random 
import copy

#Funcion algoritmo genetico
#Parametros:
#obj = instancia peso y ganancia por objeto
#cap = capacidad de la mochila
#FOB = funcion objetivo
#n = numero de padres (poblacion)
#n_obj = numero de objetos
#selec = metodo de seleccion 1.-Ruleta, 2.-Ruleta estocastica, 3.-torneo, 4.-torneo_reemplazo
#cruz = metodo de cruzamiento 0 = uniforme; >0 multipunto
#p_cruz = probabilidad de cruzamiento uniforme
# p_mut = probabilidad de mutacion
# K = numero maximo de iteraciones 
def alg_gen(obj,cap,FOB,n,n_obj,selec,cruz,p_cruz,p_mut,K):
    #Generamos padres
    x = np.random.binomial(1,0.5,(n,n_obj))
    x_fit = [FOB(i,obj,cap) for i in x]

    k=0
    while k<K:
        #Seleccion
        if selec == 1:
            x_selec = roulette_wheel_selection(x_fit,x,2)
        elif selec == 2:
            x_selec = ruleta_est(x_fit,x,2)
        elif selec == 3:
            x_selec = torneo(x, FOB, 0)[0:2,:] 
        elif selec == 4:
            x_selec = torneo(x, FOB, 1)[0:2,:]
        
        #Cruzamiento
        print(x_selec)
        if cruz >= 1:
            hijos = cruzamiento_mult(x_selec[0],x_selec[1],cruz)
        else:
            hijos = cruzamiento_unif(x_selec[0],x_selec[1],p_cruz)
        
        #Mutación
        for i in range(2):
            mutacion(hijos[i],p_mut)
        
        #Selección
        x_fit2 = [FOB(i,obj,cap) for i in hijos]
        x_fit_ord = np.array(x_fit+x_fit2)

        xhat = np.concatenate((x,hijos))

        orden = x_fit_ord.argsort()


        x = xhat[orden[2:]]

        x_fit = [FOB(i,obj,cap) for i in x]
        print(k,"\n",x)
        print(x_fit)
        k +=1
    
    return(x,x_fit)

#Funcion objetivo
def fobj(x,obj,cap):
    #Obtenemos peso total
    peso = np.sum(x*obj[:,1])

    if peso > cap:
        return 1
    else:
        return np.sum(x*obj[:,0])

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
        if fun(xpob[competidor[i], :],obj,cap) > fun(xpob[i, :],obj,cap):
            x_new[i,:] = xpob[competidor[i], :]
        else:
            x_new[i,:] = xpob[i, :]
    return x_new

#función ruleta
def roulette_wheel_selection(x_fit, x, n):
    new_population = []
    for i in range(n):
        # calcular la suma de todos los valores de la funcion objetivo en la poblacion
        #population_fitness = sum([fobj(i) for i in x])
        population_fitness = sum(x_fit)

        # Calcular probabilidades
        #chromosome_probabilities = [fobj(i) / population_fitness for i in x]
        chromosome_probabilities = [x_fit[i]/population_fitness for i in range(len(x))]

        # Calculamos las probabilidades para minimización
        #chromosome_probabilities = (1 - np.array(chromosome_probabilities)) / (len(x) - 1)

        #Seleccionamos in indice basado en las probabilidades calculadas
        idx = np.random.choice(np.arange(len(x)), p=chromosome_probabilities)
        #introducimos el valor seleccionado en una nueva población
        new_population.append(list(x[idx]))
    return new_population


#Funcion ruleta estocastica
def ruleta_est(x_fit, x, n):
    new_population = []
    
    # calcular la suma de todos los valores de la funcion objetivo en la poblacion
    population_fitness = sum(x_fit)

    # Calcular probabilidades
    chromosome_probabilities = [x_fit[i]/population_fitness for i in range(len(x))]

    # Calculamos las probabilidades para minimización
    #chromosome_probabilities = (1 - np.array(chromosome_probabilities)) / (len(x) - 1)

    #Seleccionamos los elementos en base a las probabilidades
    idx = np.random.choice(np.arange(len(x)), p=chromosome_probabilities,size=n)
    new_population=x[idx]
    return(new_population)

#Función que realiza el mecanismo de cruzamiento multipunto (1-n)
#Parametros:
#x1 = Vector Padre 1 de tamaño d (debe ser del mismo tamaño que el vector Padre 2)
#x2 = Vector Padre 2 de tamaño d
#n = número de puntos de corte (el número máximo de puntos de corte es d-1)
def cruzamiento_mult(x1,x2,n):
    #Obtenemos tamaño de los padres
    d = len(x1)

    #declaramos hijos
    h1 = np.zeros(d)
    h2 = np.zeros(d)
    
    #Seleccionamos aleatoriamente los n puntos de corte
    cortes = random.sample([i for i in range(d-1)],n)
    cortes.sort()

    #Aleatoriamente elegimos si h1 recibe inicialmente el segmento de x1 o x2
    it = bool(np.random.binomial(1,0.5))

    #Cruzamiento
    for i in range(n+1):
        if i == 0:
            h1[i:cortes[i]+1] = x1[i:cortes[i]+1]*it + x2[i:cortes[i]+1]*(not it)
            h2[i:cortes[i]+1] = x2[i:cortes[i]+1]*it + x1[i:cortes[i]+1]*(not it)
        elif i == n:
            h1[cortes[i-1]+1:d] = x1[cortes[i-1]+1:d]*it + x2[cortes[i-1]+1:d]*(not it)
            h2[cortes[i-1]+1:d] = x2[cortes[i-1]+1:d]*it + x1[cortes[i-1]+1:d]*(not it) 
        else:
            h1[cortes[i-1]+1:cortes[i]+1] = x1[cortes[i-1]+1:cortes[i]+1]*it + x2[cortes[i-1]+1:cortes[i]+1]*(not it)
            h2[cortes[i-1]+1:cortes[i]+1] = x2[cortes[i-1]+1:cortes[i]+1]*it + x1[cortes[i-1]+1:cortes[i]+1]*(not it)
        it = not it

    #Regresamos hijos
    return [h1,h2]

def cruzamiento_unif(x1,x2,p):
    d=len(x1)
    h1=copy.deepcopy(x1)
    h2=copy.deepcopy(x1)
    mask1=np.random.binomial(1,p,d)
    mask2=np.random.binomial(1,p,d)
    for i in range(d):
        if mask1[i]==0:
            h1[i]=x2[i]
        if mask2[i]==0:
            h2[i]=x2[i]
    return [h1,h2]

def mutacion(x,p):
    #Obtenemos el tamaño del hijo
    d = len(x)

    for i in range(d):
        if np.random.uniform() <= p:
            x[i] = not x[i]

#/Users/ivanvegagutierrez/Desktop/CIMAT/SEGUNDO/METOPT2/ks_19_0

datos = np.loadtxt('/Users/ivanvegagutierrez/Desktop/CIMAT/SEGUNDO/METOPT2/ks_19_0',dtype='float')

n_obj = int(datos[0,0])
cap = datos[0,1]
obj = datos[1:,:]

print(cap)

n = 10

#obj,cap,FOB,n,n_obj,selec,cruz,p_cruz_unif,p_mut,K
sol = alg_gen(obj,cap,fobj,n,n_obj,1,0,0.5,0.1,1000)

print(sol[1])