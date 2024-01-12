#Importamos las librería
from ortools.linear_solver import pywraplp

# Declaramos el solver
#model = pywraplp.Solver.CreateSolver('SCIP')
#model = pywraplp.Solver.CreateSolver('GLOP')
model = pywraplp.Solver('model_name', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

# Creamos las Varialbles de decisión
x1j = model.NumVar(0, model.infinity(), 'x1j')
x2j = model.NumVar(0, model.infinity(), 'x2j')
x3j = model.NumVar(0, model.infinity(), 'x3j')
x4j = model.NumVar(0, model.infinity(), 'x4j')
x5j = model.NumVar(0, model.infinity(), 'x5j')
x3r = model.NumVar(0, model.infinity(), 'x3r')
x4r = model.NumVar(0, model.infinity(), 'x4r')
x5r = model.NumVar(0, model.infinity(), 'x5r')
x1c = model.NumVar(0, model.infinity(), 'x1c')
x2c = model.NumVar(0, model.infinity(), 'x2c')
x3c = model.NumVar(0, model.infinity(), 'x3c')
x4c = model.NumVar(0, model.infinity(), 'x4c')
x5c = model.NumVar(0, model.infinity(), 'x5c')

# Declaramos las Restricciones

model.Add(x1j + x1c == 16500)
model.Add(x2j + x2c == 22000)
model.Add(x3j + x3r + x3c == 62000)
model.Add(x4j + x4r + x4c == 7500)
model.Add(x5j + x5r + x5c == 62000)

model.Add( x1j*(1/4.63) +  x2j*(1/4.63) + x3j*(1/5.23) + x4j*(1/5.23) + x5j*(1/4.17) <= 576 )
model.Add( x3r*(1/5.23) + x4r*(1/5.23) + x5r*(1/4.17) <= 21600)

# Definimos la Función Objetivo
model.Maximize( 1.33*x1j + 1.31*x2j + 1.61*(x3j + x3r) + 1.73*(x4j + x4r) + 1.2*(x5j + x5r) + 1.13*x1c + 1.16*x2c + 1.5*x3c + 1.54*x4c + x5c)

# Llamamos al  Solver
status = model.Solve()

# Imprimimos los resultados
if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
    print('El valor óptimo de la función objetivo es z =', model.Objective().Value())
    print('x1j = ', x1j.solution_value(), '\n')
    print('x2j = ', x2j.solution_value(), '\n')
    print('x3j = ', x3j.solution_value(), '\n')
    print('x4j = ', x4j.solution_value(), '\n')
    print('x5j = ', x5j.solution_value(), '\n')
    print('x3r = ', x3r.solution_value(), '\n')
    print('x4r = ', x4r.solution_value(), '\n')
    print('x5r = ', x5r.solution_value(), '\n')
    print('x1c = ', x1c.solution_value(), '\n')
    print('x2c = ', x2c.solution_value(), '\n')
    print('x3c = ', x3c.solution_value(), '\n')
    print('x4c = ', x4c.solution_value(), '\n')
    print('x5c = ', x5c.solution_value(), '\n')