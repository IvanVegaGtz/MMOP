import numpy as np

def read_instance(archivo):
    instancia = open(archivo, 'r')
    valores = []
    for i in instancia:
        valores.append([int(i) for i in i.split()])
    return valores[::]

#valores=read_instance("3elt_graph")
#print(valores)

#solucion=np.random.binomial(1,0.5,valores[0][0])
#suma=0
#for i in range(1,valores[0][0]+1):
#    for j in valores[i]:
#        if solucion[i-1]!=solucion[j-1] and i<j:
#            suma+=1
#print(suma)

# Definimos la funcion objetivo
def fobj(x,D,valores):
    suma=0
    for i in range(1,D+1):
        for j in valores[i]:
            if x[i-1]!=x[j-1] and i<j:
                suma+=1
    #dif=D/2-np.sum(x)
    #if dif!=0:
    #    suma+=abs(dif)*500
    return suma

def evalua(xpob, N, D, valores):
    #n = xpob.shape[0]
    for i in range(N):
        xpob[i,D] = fobj(xpob[i,:D],D,valores)
    return xpob 

def estima(xpob,D,M):
    #n,m = xpob.shape
    p = []
    for i in range(D):
        p.append(np.sum(xpob[:,i])/M)
        #if p[i]==0:
            #p[i]=0.01
        #if p[i]==1:
            #p[i]=0.99
    return p

def UMDA(archivo,N, M, iter, p_0):
    '''
    N : tamano de la poblacion
    M : tamano de seleccion
    iter: numero maximo de iteraciones 
    D: dimension, no. de variables  
    '''
    # Poblacion inicial
    k = 0
    valores=read_instance(archivo)
    D=valores[0][0]
    xpob = np.zeros((N,D+1))
    xpob_selec = np.zeros((M,D+1))
    indices=np.arange(0,D,1)
    for i in range(N):
        xpob[i,:D] = np.random.binomial(1,p_0, size=(D))
        dif=D/2-np.sum(xpob[i,:D])
        cambios=[]
        if dif<0:
            while len(cambios)<abs(dif):
                cambio=np.random.choice(np.setdiff1d(indices,np.array(cambios)),1,replace='False')
                if xpob[i,cambio]==1:
                    cambios.append(cambio)
                    xpob[i,cambio]=0
        elif dif>0:
             while len(cambios)<abs(dif):
                cambio=np.random.choice(np.setdiff1d(indices,np.array(cambios)),1,replace='False')
                if xpob[i,cambio]==0:
                    cambios.append(cambio)
                    xpob[i,cambio]=1

        #while np.sum(xpob[i,:D])!=D/2:
        #    xpob[i,:D] = np.random.binomial(1,p_0, size=(D))
    #xpob[:,:D] = np.random.binomial(1,p_0, size=(N, D))
    xpob = evalua(xpob, N, D,valores)
    #print(k)
    #print(xpob)
    #aux=np.std(xpob[:,D])
    print(D/2)
    while k < iter:# and aux!=0:
        # Seleccion
        xpob = xpob[xpob[:,D].argsort()]
        xpob_selec = xpob[:M,:]
        # Estimacion
        p = estima(xpob_selec, D, M)
        # Muestreo
        for i in range(N):
            for j in range(D):
                xpob[i,j] = np.random.binomial(1,p[j], size=1)
            dif=D/2-np.sum(xpob[i,:D])
            cambios=[]
            if dif<0:
                while len(cambios)<abs(dif):
                    cambio=np.random.choice(np.setdiff1d(indices,np.array(cambios)),1,replace='False')
                    if xpob[i,cambio]==1:
                        cambios.append(cambio)
                        xpob[i,cambio]=0
            elif dif>0:
                while len(cambios)<abs(dif):
                    cambio=np.random.choice(np.setdiff1d(indices,np.array(cambios)),1,replace='False')
                    if xpob[i,cambio]==0:
                        cambios.append(cambio)
                        xpob[i,cambio]=1
            #while np.sum(xpob[i,:D])!=D/2:
            #    for j in range(D):
            #        xpob[i,j] = np.random.binomial(1,p[j], size=1)

                #xpob[i,:D] = np.random.binomial(1,p_0, size=(D))
        #for i in range(D):
            #xpob[:,i] = np.random.binomial(1,p[i], N)
        xpob = evalua(xpob,N, D, valores)
        k += 1
        print(f'iter {k}')
        print(xpob[:,D])
        #print(xpob[:,D])
        #aux=np.std(xpob[:,D])
        #print(p)
        #for i in range(N):
        #    print(np.sum(xpob[i,:D]))
    orden=xpob[:,D].argsort()
    return xpob[orden]

sol=UMDA('3elt_graph',100, 25, 150, 0.5)

print(sol)
