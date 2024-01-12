from ortools.linear_solver import pywraplp

model = pywraplp.Solver('Modelo_lineal_3', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

# Variables de decisión
x1 = model.NumVar(0, model.infinity(), 'x1')
x2 = model.NumVar(0, model.infinity(), 'x2')
x3 = model.NumVar(0, model.infinity(), 'x3')
x4 = model.NumVar(0, model.infinity(), 'x4')

# Restricciones

model.Add( 2*x1 + 3*x2 + 4*x3 + 2*x4 <= 500)
model.Add( 3*x1 + 2*x2 +   x3 + 2*x4 <= 380 )

#Función objetivo

model.Maximize( 65*x1 + 70*x2 + 55*x3 + 45*x4 -10*(2*x1 + 3*x2 + 4*x3 + 2*x4) -5*(3*x1 + 2*x2 + x3 + 2*x4) )

#Solucionador

status = model.Solve()

#Impresión

if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
    print("La solución óptima es z = ", model.Objective().Value(), '\n')
    print(x1,'=', x1.solution_value(),'\n')
    print(x2,'=', x2.solution_value(),'\n')
    print(x3,'=', x3.solution_value(),'\n')
    print(x4,'=', x4.solution_value(),'\n')