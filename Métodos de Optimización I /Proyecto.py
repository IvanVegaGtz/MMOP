from ortools.linear_solver import pywraplp

###Variables de decision
#j patron
#i ancho

model = pywraplp.Solver.CreateSolver('SCIP')

# Datos

# Definimos el número de demandas (órdenes) de cada talla
d = [8, 10, 15, 10, 7]

# Definimos la matriz que contiene los patrones de corte la última
# columna representa el residuo de realizar el corte con el patrón 

aji=[[4, 0, 0, 0, 1, 5],
     [3, 1, 1, 0, 0, 1],
     [3, 1, 0, 1, 0, 9],
     [3, 1, 0, 0, 1, 12],
     [3, 0, 2, 0, 0, 3],
     [3, 0, 1, 1, 0, 11],
     [3, 0, 1, 0, 2, 1],
     [3, 0, 0, 3, 0, 3],
     [3, 0, 0, 2, 1, 6],
     [3, 0, 0, 1, 2, 9],
     [3, 0, 0, 0, 3, 12],
     [2, 3, 0, 0, 0, 6],
     [2, 2, 1, 0, 0, 8],
     [2, 2, 0, 2, 0, 0],
     [2, 2, 0, 1, 1, 3],
     [2, 2, 0, 0, 2, 6],
     [2, 1, 2, 0, 0, 10],
     [2, 1, 1, 2, 0, 2],
     [2, 1, 1, 1, 1, 5],
     [2, 1, 1, 0, 2, 8],
     [2, 0, 3, 0, 0, 12],
     [2, 0, 2, 2, 0, 4],
     [2, 0, 2, 1, 1, 7],
     [2, 0, 2, 0, 2, 10],
     [2, 0, 1, 3, 0, 12],
     [2, 0, 1, 2, 2, 2],
     [2, 0, 1, 1, 3, 5],
     [2, 0, 1, 0, 4, 8],
     [2, 0, 0, 5, 0, 4],
     [2, 0, 0, 4, 1, 7],
     [2, 0, 0, 3, 2, 10],
     [2, 0, 0, 2, 4, 0],
     [2, 0, 0, 1, 5, 3],
     [2, 0, 0, 0, 6, 6],
     [1, 4, 0, 0, 1, 0],
     [1, 3, 1, 0, 1, 2],
     [1, 2, 2, 1, 0, 1],
     [1, 2, 1, 2, 0, 9],
     [1, 2, 1, 1, 1, 12],
     [1, 2, 1, 0, 3, 2],
     [1, 2, 0, 4, 0, 1],
     [1, 2, 0, 3, 1, 4],
     [1, 2, 0, 2, 2, 7],
     [1, 2, 0, 1, 3, 10],
     [1, 2, 0, 0, 5, 0],
     [1, 1, 3, 1, 0, 3],
     [1, 1, 3, 0, 1, 6],
     [1, 1, 2, 2, 0, 11],
     [1, 1, 2, 1, 2, 1],
     [1, 1, 2, 0, 3, 4],
     [1, 0, 4, 1, 0, 5],
     [1, 0, 4, 0, 1, 8],
     [1, 0, 3, 2, 1, 0],
     [1, 0, 3, 1, 2, 3],
     [1, 0, 3, 0, 3, 6],
     [1, 0, 2, 4, 0, 5],
     [1, 0, 2, 3, 1, 8],
     [1, 0, 2, 2, 2, 11],
     [1, 0, 2, 1, 4, 1],
     [1, 0, 2, 0, 5, 4],
     [1, 0, 1, 5, 1, 0],
     [1, 0, 1, 4, 2, 3],
     [1, 0, 1, 3, 3, 6],
     [1, 0, 1, 2, 4, 9],
     [1, 0, 1, 1, 5, 12],
     [1, 0, 1, 0, 7, 2],
     [1, 0, 0, 7, 0, 5],
     [1, 0, 0, 6, 1, 8],
     [1, 0, 0, 5, 2, 11],
     [1, 0, 0, 4, 4, 1],
     [1, 0, 0, 3, 5, 4],
     [1, 0, 0, 2, 6, 7],
     [1, 0, 0, 1, 7, 10],
     [1, 0, 0, 0, 9, 0],
     [0, 5, 0, 1, 0, 4],
     [0, 4, 1, 1, 0, 6],
     [0, 4, 0, 2, 1, 1],
     [0, 4, 0, 1, 2, 4],
     [0, 3, 3, 0, 0, 0]]

# Definimos el número de patrones
n = len(aji)
# Definimos el número de órdenes
m = len(aji[0])-1

# Variables de decisión

inf = model.infinity()
X = {}
for j in range(n):
    X[j] = model.IntVar(0,inf,'X{}'.format(j+1))


# Restricciones

for i in range(m):
    model.Add(d[i] <= model.Sum(X[j]*aji[j][i] for j in range(n)))

# Elegimos el tipo de problema que deseamos resolver  

# Minimizar el número de rollos
model.Minimize(model.Sum(X[j] for j in range(n)))


# Minimizar los residuos
#model.Minimize(model.Sum(X[j]*aji[j][5] for j in range(n)))

# Minimizar la sobre producción
#model.Minimize(model.Sum(model.Sum(X[j]*aji[j][i] for j in range(n))-d[i] for i in range(m)))



status = model.Solve()

if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        print('Solución:')
        print('Valor de la funcion objetivo =', sum(X[j].solution_value() for j in range(n)))
        for j in range(n):
            if X[j].solution_value() != 0:
                print("Para el patron", aji[j])
                print("Número de patrones utilizados =", X[j].solution_value())
        print("Sobre produccion",sum(X[j].solution_value()*aji[j][i] for j in range(n) for i in range(m))-sum(d[i] for i in range(m)))
        print("Residuos=",sum(X[j].solution_value()*aji[j][5] for j in range(n)))
