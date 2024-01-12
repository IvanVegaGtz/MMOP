import numpy as np #Para poder trabajar con arrays
import random #Para generar numeros de forma aleatoria
import math #Para hallar la raiz cuadrada

def LUfacto(A):
    """
    Esta funcion devuelve las matrices L, U,, las cuales
    son la facotrizacion de A (A = LU). Donde L es una 
    matriz triangular inferior y U es triangular superior.
    
    Argumentos:
    A(matriz): Matriz que se desea factorizar

    Excepciones:
    Division entre cero si U[j][j] =0 
    """
    # Hallamaos la dimension de la matriz
    n = A.shape[0]
    #Creamos la matriz U compuesta por ceros
    U = np.zeros((n,n))
    #La matriz L tendra unos en su diagonal
    L = np.identity(n)
    #La primera fila de U será igual a la primera fila de A
    U[0] = A[0]
    #Verificamos que no intentemos una división entre cero
    if A[0][0] == 0:
        print("Error de ejecución: División entre cero")
        return 
    else:
        #Hallamos la primera columna de L
        L[:,0] = A[:,0]/A[0][0]
        #Este ciclo recorrerá las filas i
        for i in range(1,n):
            #El siguiente ciclo recorrerá las columasn j
            for j in range(1,n):
                #Si la siguiente condición se cumple entonces llenaremos la matriz L
                if i>j:
                    suma = 0
                    for k in range(j):
                        suma += L[i][k]*U[k][j]  
                    if U[j][j] == 0:
                        print("Error de ejecución: Divisi{on entre cero")
                        return 
                    else:
                        L[i][j] = (A[i][j] - suma)/U[j][j]
                #Si i >= j entonces se llenará la matriz U
                else:
                    suma = 0
                    for k in range(i):
                        suma += L[i][k]*U[k][j]
                    U[i][j] = A[i][j] - suma
    return (L,U)
#----------------------------------------


#A = np.array([[2, 4, -4, 1], [-1, 1, 2, 3], [3, 6, 1, -2], [1, 1, -4, 1]])
#B = np.array([[-1, 3, 2], [3, -4, 1], [2, 5, -2]])
#C = np.zeros((4,4))
#b = [1, 1, 1, 1]

#(X,Y) = LUfacto(A)

#print(X)
#print(Y)

#---------------------------
def BackSub(A,b):
    """
    Esta función calcula la solución de un sistema Ax=b,
    mediante sustitución hacia atrás, donde A es una matriz
    triangular superior.
    
    Argumentos:
    A (matriz): Matriz triangular superior.
    b (vector): Vctor de términos independientes.
    """ 
    #Creamos el vector que contendrá los valores de la solución.
    n =  A.shape[0]
    x = np.empty(shape=n)
    #Hallamos el valor de la variable x_i (empezando por x_n)
    for i in range(n-1, -1, -1):
        suma = 0
        #A partir del valor x_i hallamos el valor de x_i-1
        for j in range(n-1, i, -1):
            suma += A[i][j]*x[j]
        x[i] = (b[i] - suma) / A[i][i]
    return x
#------------------------------------
def ForwSub(A,b):
    """
    Esta función calcula la solución de un sistema Ax=b,
    mediante sustitución hacia adelante, donde A es una 
    matriz triangular inferior.
    
    Argumentos:
    A (matriz): Matriz triangular inferior.
    b (vector): Vctor de términos independientes.
    """ 
    #Creamos el vector que contendrá los valores de la solución.
    n = A.shape[0]
    x = np.empty(shape=n)
    #Hallamos el valor de cada x_i
    for i in range(n):
        suma = 0
        #Este ciclo utiliza el valor de x_i, para hallar x_i+1
        for j in range(i):
            suma += A[i][j]*x[j]
        x[i] = (b[i] - suma)/ A[i][i]
    return x
#----------------------------------
def SymmetricMat(n):
    """
    Esta función devuelve una matriz simetrica de tamaño
    nxn.

    Argumentos:
    n (entero): Dimensión de la matriz que deseamos crear

    Observaciones:
    Los elementos de la matriz están entre 0 y 1
    """
    #Creamos la matriz que deseamos hallar 
    A = np.empty((n,n)) #Creamos una matriz de tamaño n
    #Rellenamos la matriz con valores aleatorios
    for i in range(n): 
        A[i][i] = random.random() 
        #El siguiente ciclo es para forzar que la matriz sea simétrica
        for j in range(i+1,n): 
            A[i][j] = random.random()
            A[j][i] = A[i][j]
    return A

#n=4
#print(SymmetricMat(n))

#--------------------------------------
def PdSMat(n):
    """
    Esta función regresa una matriz positiva definida de
    dimensión n.

    Argumentos:
    n(entero) : dimensión de la matriz que desamos construir
    
    Observaciones:
    Se necesita la función SymmetricMat(n)
    """
    #Creamos una matriz simetrica A
    A = SymmetricMat(n) 
    #Hallamos los valores y vectories propios de A, respectivamente
    D,P = np.linalg.eig(A) 
    #Sacamos el valor absoluto de cada valor propio
    D = abs(D) 
    #Pasamos el vector D a una matriz cuya diagonal tiene los valores propios.
    D = D*(np.identity(n))
    #A la diagonal de la matriz D sumamos la norma (euclidiana(2)) de D
    D = D + (np.linalg.norm(D,2))*(np.identity(n))
    #Obtenemos la matriz buscada qu es el producto de las matrices P, D y la inversa de P.
    A = P.dot((D.dot(np.linalg.inv(P))))
    return A

#print(PdSMat(4))
#--------------------------------------

def Cholesky(A):
    """
    Esta función regresa una matriz triangular inferior B
    tal que la matriz A se puede expresar como el producto
    de B y la transpuesta de B (factorización de Cholesky)

    Argumentos:
    A (matriz) : A es una matriz simétrica 

    Excepciones:
    División entre cero:     si A[j][j] = 0  
    Raiz cuadrada de un numero negativo:     si A[J][J] - suma < 0
    Resultado erroneo:  si A no es simetrica
    """
    #Primero, creamos la matriz B
    n = A.shape[0] 
    B = np.zeros((n,n))
    #Verificamos si la matriz es simetrica
    if not np.array_equal(A, np.transpose(A)):
        print("Error de ejecución: La matriz no es simétrica")
        return 
    #Hallamos los valores de la j-esima columna de B
    for j in range(n):
        suma = 0
        #El siguiente ciclo es para hallar los valores de la diagonal
        for k in range(j):
            suma += B[j][k]*B[j][k]
        #Verificamos que no se calculen raíces cuadradas negativas
        if A[j][j] - suma < 0:
            print("Error de ejecución: Raíz cuadrada negativa")
            return
        else:
            #Asignamos el valor de B en la diagonal
            B[j][j] = math.sqrt(A[j][j] - suma)
        #Hallamos los valores de la iésima fila de B
        for i in range(j+1,n):
            suma = 0
            for k in range(j):
                suma += B[j][k]*B[i][k]
            #Verificamso que no existan divisiones entre cero
            if B[j][j] == 0:
                print("Error de ejecución: División entre cero")
                return
            else:
                #Asigamos el valor de B en la i-esima fila
                B[i][j] = (A[i][j] - suma)/B[j][j]
    return B

A = np.array([[25, 15, -5, -10], [15, 10, 1, -7], [-5, 1, 21, 4], [-10, -7, 4, 18]])
n = 4
P = PdSMat(n)
#B = np.array([[4, -1, 1], [-1, 4.25, 2.75], [1, 2.75, 3.5]])
X = Cholesky(P)
print(X)
#Y = np.transpose(X)

#print('matriz B')
#print(Cholesky(A))
#print('matriz Btranspuesta')
#print(Y)
#print('res')
#print(X.dot(Y))
#print('matriz A')
#print(A)

#------------------------------------
#z = BackSub(Y, b)
#sol = np.array([z])
#print(Y*(sol.T))

#b = np.ones((10,1))
#print(b)