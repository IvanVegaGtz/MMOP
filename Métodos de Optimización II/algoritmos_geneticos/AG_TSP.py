
import numpy as np
import random
import matplotlib.pyplot as plt
import copy
import time
import csv

######################CRUZAMIENTOS#############################
#Cruzamiento CX
def cx(x1,x2):
    h1=copy.deepcopy(x2)
    h2=copy.deepcopy(x1)
    flag=0
    aux1=0
    while flag==0:
        
        aux2=x1[aux1]
        h1[aux1]=aux2
        aux1=x2[aux2]
        h2[aux2]=aux1
        if aux1==0:
            flag=1

    return [h1,h2]

#Cruzamiento OX1
def ox1(x1,x2):
    d = len(x1)
    h1 = np.zeros(d)
    h2 = np.zeros(d)
    
    cortes = random.sample([i for i in range(d-1)],2)
    cortes.sort()
    h1[range(cortes[0]+1,cortes[1]+1)]=x1[range(cortes[0]+1,cortes[1]+1)]
    h2[range(cortes[0]+1,cortes[1]+1)]=x2[range(cortes[0]+1,cortes[1]+1)]
    aux1=np.setdiff1d(x1,x1[range(cortes[0]+1,cortes[1]+1)])
    aux2=np.setdiff1d(x2,x2[range(cortes[0]+1,cortes[1]+1)])
    indices=np.zeros(d)
    indices[range(d-cortes[1]-1)]=np.arange(cortes[1]+1,d,1)
    indices[range(d-cortes[1]-1,d)]=np.arange(0,cortes[1]+1,1)
    
    cont=0
    for i in indices:
        if x2[int(i)] in aux1:
            h1[int(indices[cont])]=x2[int(i)]
            cont+=1
    cont=0
    for i in indices:
        if x1[int(i)] in aux2:
            h2[int(indices[cont])]=x1[int(i)]
            cont+=1

    return [h1,h2]

#Función mecanismo de cruzamiento OX2 (order based crossover)
#Parámetros:
#X: Vectores de los padres 1 y 2. X es de tamaño 2,n
#n_pos: Número de posiciones al azar para hacer el cruzamiento
#
#Devuelve X_h que son los vectores de los hijos 1 y 2. X_h es de tamaño 2,n
def ox2(X, n_pos):
    
    n = len(X[0])
    
    #Hacemos copia del padre
    X_h = np.array(X)

    #Seleccionamos posiciones al azar
    pos = random.sample([i for i in range(n)],n_pos)
    pos.sort()

    #Valores Padre 2
    seleccion = [X[1,i] for i in pos]

    #Copiamos valores a hijo 1
    j=0
    i=0
    while j < n_pos:
        if X[0,i] in seleccion:
            X_h[0,i] = seleccion[j]
            j += 1
        i += 1

    #Valores Padre 1
    seleccion = [X[0,i] for i in pos]

    #Copiamos valores a hijo 2
    j=0
    i=0
    while j < n_pos:
        if X[1,i] in seleccion:
            X_h[1,i] = seleccion[j]
            j += 1
        i += 1
    return(X_h)


##################### MUTACIONES #############################

#Función mutación IVM (Inversion mutation)
#Parámetros:
#X: Vector de datos de un individuo
#tam: Tamaño del subtour 
#Devuelve X_m que es el individuo mutado
def IVM(X, tam):
    n = len(X)
    #Obtenemos un subtour al azar
    pos_sub = random.randint(0,n-tam)
    subtour = X[pos_sub:pos_sub+tam]
    ind = [i for i in range(pos_sub,pos_sub+tam)]

    #Eliminamos subtour del vector original
    X_m = np.delete(X,ind,None)

    #Obtenemos una posición al azar
    pos = random.randint(0,n-tam)

    #Invertimos subtour
    subtour_inv = np.flip(subtour,None)

    #Insertamos en la posición el subtour invertido
    X_m = np.insert(X_m,pos,subtour_inv,None)
    return(X_m)

#Función de mutación DM
#m es el tamaño del subtour, x es el individuo
def DM(x, m):
    n = len(x)
    pos_inicio = random.randint(0, n-1)
    #print(pos_inicio)
    
    #creacion de sub tour
    x_s = []
    if m <= (n-1 - pos_inicio): 
        for i in range (m):
            x_s.append(x[pos_inicio + i])
        
    else:
        i = 0
        l = 0
        for j in range (n - pos_inicio):
            x_s.append(x[pos_inicio + i])
            i = i + 1
        for j in range (m - (n - pos_inicio)):
            x_s.append(x[l])
            l = l + 1
    #print(x_s)
    
    #seleccion al azar de posicion del remanente del individuo
    pos_insert = random.randint(0,n-m)
    #print(pos_insert)
    
    #individuo sin el subtour
    x_r = np.setdiff1d(x,x_s,True)   
    #print(x_r)    
    
    #se inserta el subtour a partir de la posicion pos_insert
    x_m = np.insert(x_r,pos_insert,x_s)
    
    #se regresa al individuo mutado
    return(x_m)

#Función de mutación EM
def EM(x):
    pos1=np.random.randint(0,len(x)-1)
    pos2=np.random.randint(0,len(x)-1)
    while pos1==pos2:
        pos2=np.random.randint(0,len(x)-1)
    x[pos1],x[pos2]=x[pos2],x[pos1]
    return(x)

#Función de mutación ISM
def ISM(x):
    pos1=np.random.randint(0,len(x)-1)
    elemento=x[pos1]
    pos2=np.random.randint(0,len(x)-1)
    while pos1==pos2:
        pos2=np.random.randint(0,len(x)-1)

    #Modificación para que funcione
    ####
    x_list = x.tolist()
    x_list.pop(pos1)
    x_list.insert(pos2,elemento)
    x = np.array(x_list)
    ####
    return(x)

#Función de mutación SIM
def SIM(x):
    x = x.tolist()
    n_subtour=3
    pos_subtour1=np.random.randint(0,len(x)-n_subtour+1)
    pos_subtour2=pos_subtour1+n_subtour
    subtour=x[pos_subtour1:pos_subtour2]
    subtour_inv=reversed(subtour)
    x[pos_subtour1:pos_subtour2]=subtour_inv
    return(x)

# Se reacomoda elemento i de x, m - 1 posiciones a la derecha
# m es el tamaño del subconjunto, x es el individuo
def SM(x, m):
    n = len(x)
    pos_inicio = random.randint(0, n-1)
    
    # Elemento i
    scramble_pos = x[pos_inicio]

    # Individuo sin elemento i
    x_r = np.setdiff1d(x,scramble_pos,True)   
    #print(x_r)    
    
    # Verificar si la posición de inicio es valida
    if m <= (n-1 - pos_inicio): 
        pos_insert = pos_inicio + m - 1

    else:
        pos_insert = m - len(x_r[pos_inicio:]) - 1


    #se inserta el elemento i, (m-1) posiciones a la derecha
    x_m = np.insert(x_r,pos_insert,scramble_pos)
    
    #se regresa al individuo mutado
    return(x_m)

##################### SELECCION #############################

#Mecanismo de selección de ruleta
#
def ruleta(x_dist,n):
    tam = len(x_dist)
    #calculamos probabilidad (para minimizar)
    p = x_dist / np.sum(x_dist)
    p = (1-p)/(tam-1)

    selec = random.choices([i for i in range(tam)],p,k=n)

    return selec

#Mecanismo de selección de torneo
#
def torneo(x_dist,n):
    tam = len(x_dist)
    selec = []

    for i in range(n):
        c1 = np.random.randint(0,tam)
        c2 = np.random.randint(0,tam)
        if x_dist[c1] <= x_dist[c2]:
            selec.append(c1)
        else:
            selec.append(c2)

    return selec


##################### Funcion Objetivo #############################
#Parámetros
#datos = matriz de posiciones de cada punto
#x = vector de permutaciones
#n = número de puntos
def f_obj(datos,x,n):
    dist = 0

    for i in range(n):
        if i < n-1:
            dist += ((datos[x[i],0]-datos[x[i+1],0])**2 + (datos[x[i],1]-datos[x[i+1],1])**2)**(1/2)
            
        else:
            dist += ((datos[x[i],0]-datos[x[0],0])**2 + (datos[x[i],1]-datos[x[0],1])**2)**(1/2)
    
    return dist


##################### Funcion MAIN #############################
#Parámetros
#K = número de iteraciones
#tam = número de puntos TSP
#datos = matriz de posiciones de los puntos
#n_p = número de padres
#n_h = número de hijos en cada iteracion (debe ser par)
def ga_tsp(K, tam, datos, n_p, n_h):

    #Vector de posibilidades tsp
    pos = [i for i in range(tam)]
    
    xh = np.zeros((n_h,tam),np.int32)
    xh_dist = np.zeros(n_h,np.int64)
    
    ##Generamos padres aleatorios
    x = np.zeros((n_p,tam),np.int32)
    x_dist = np.zeros(n_p,np.int64)
    for i in range(n_p):
        x[i] = random.sample(pos,tam)
        x_dist[i] = f_obj(datos,x[i],tam)

    ###Iteramos
    k=0
    ini = time.time()
    while k < K:
        ###Seleccionamos n_h padres
        #Ruleta
        #seleccion = ruleta(x_dist,n_h)
        #Torneo
        seleccion = torneo(x_dist,n_h)

        ###Cruzamiento
        
        for i in range(int(n_h/2)):
            ##Cruzamiento OX2
            #Necesita el parámtero de número de posiciones a cruzar                        ^
            #cruza = ox2(np.concatenate(([x[seleccion[i*2]]],[x[seleccion[i*2+1]]]),0), 5000)

            ##Cruzamiento cx
            #cruza = cx(x[seleccion[i*2]],x[seleccion[i*2+1]])

            ##Cruzamiento OX1
            cruza = ox1(x[seleccion[i*2]],x[seleccion[i*2+1]])

            xh[i*2] = cruza[0]
            xh[i*2+1] = cruza[1]

        
        ###Mutación y obtenemos valor fobjetivo
        for i in range(n_h):
            ##IVM
            #Necesita el parámtero de tamaño de subtour
            #xh[i] = IVM(xh[i],1000)

            ##DM
            #Necesita el parámtero de tamaño de subtour
            #xh[i] = DM(xh[i],5)

            ##EM
            #xh[i] = EM(xh[i])

            ##ISM
            #xh[i] = ISM(xh[i])

            ##SIM
            #xh[i] = SIM(xh[i])

            ##SM necesita parámetro de tamaño de subconjunto
            xh[i] = SM(xh[i],1000)

            xh_dist[i] = f_obj(datos,xh[i],tam)

        ###Reemplazo
        xhat = np.concatenate((x,xh),0)
        xhat_dist = np.concatenate((x_dist,xh_dist),0)
        orden = np.argsort(xhat_dist)
        
        xhat = xhat[orden,:]
        xhat_dist =  xhat_dist[orden]

        x = xhat[0:n_p,:]
        x_dist = xhat_dist[0:n_p]

        k+=1
        print("Iteracion: ", k)
        print("Mejor solución: ", x_dist[0])
    
    fin = time.time()
    print(fin-ini)
    return(x,x_dist)


#################### Función Graficar #####################
# Funcion graficar
# x = vector solución TSP
def graficar(x,datos):
    n = len(x)

    fig = plt.figure(1)
    fig.clear()
    
    #Obtenemos cordenadas
    cordx = np.zeros(n)
    cordy = np.zeros(n)
    for i in range(n):
        cordx[i] = datos[x[i],0]
        cordy[i] = datos[x[i],1]
    
    print(cordx.max())
    print(cordy.max())

    #Descomentar esto si se requiere ver rutas
    #plt.plot(cordx,cordy,color="Blue")
    #plt.plot([datos[x[0],0],datos[x[n-1],0]],[datos[x[0],1],datos[x[n-1],1]],color="Blue")
    plt.scatter(cordx,cordy,color='Red',s=0.5)
    
    plt.show()


######################## INICIO  ##########################
##Abrimos archivo
file = open("/Users/ivanvegagutierrez/Desktop/CIMAT/SEGUNDO/METOPT2/reto1_tsp", 'r')

###Leemos los datos
l=0
datos = {}
for linea in file:
    if l==0:
        n = int(linea)
    else:
        lista = linea.split(" ")
        datos[l-1,0] = int(lista[1])
        datos[l-1,1] = int(lista[2])

    if l == n:
        break

    l+=1

K = 500
tam = n
n_p = 10
n_h = 2

#Función main
#ga_tsp(K, tam, datos, n_p, n_h)
#Parámetros
#K = número de iteraciones
#tam = número de puntos TSP
#datos = matriz de posiciones de los puntos
#n_p = número de padres
#n_h = número de hijos en cada iteracion (debe ser par)
xres = ga_tsp(K,tam,datos,n_p,n_h)

#Guardamos resultados:
with open('/Users/ivanvegagutierrez/Desktop/CIMAT/SEGUNDO/METOPT2/resultados_reto1.txt','w',encoding='UTF8',newline='') as f:
    escribir = csv.writer(f)
    #Producción
    escribir.writerow(['F_obj'])
    escribir.writerow([xres[1][0]])
    escribir.writerow(['Permutacion'])
    for i in range(tam):
        escribir.writerow([xres[0][0][i]])

print(xres[1])
print(xres[0][0])

graficar(xres[0][0],datos)
