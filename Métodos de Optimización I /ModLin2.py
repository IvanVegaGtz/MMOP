from ortools.linear_solver import pywraplp

# Declaración del Solver
model = pywraplp.Solver('Modelo_lineal_2', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

# Creación de las variables de decisión
xa1 = model.NumVar(0, model.infinity(), 'xa1')
xa2 = model.NumVar(0, model.infinity(), 'xa2')
xa3 = model.NumVar(0, model.infinity(), 'xa3')
xa4 = model.NumVar(0, model.infinity(), 'xa4')
xa5 = model.NumVar(0, model.infinity(), 'xa5')
xb1 = model.NumVar(0, model.infinity(), 'xb1')
xb2 = model.NumVar(0, model.infinity(), 'xb2')
xb3 = model.NumVar(0, model.infinity(), 'xb3')
xb4 = model.NumVar(0, model.infinity(), 'xb4')
xc1 = model.NumVar(0, model.infinity(), 'xc1')
xc2 = model.NumVar(0, model.infinity(), 'xc2')
xc3 = model.NumVar(0, model.infinity(), 'xc3')
xd1 = model.NumVar(0, model.infinity(), 'xd1')
xd2 = model.NumVar(0, model.infinity(), 'xd2')

# Creación de las restricciones
model.Add(xa2 + xb2 + xc2 + xd2 == 1.5*xa1)
model.Add(xa3 + xb3 + xc3 == 1.5*xa2 + 1.13*xb1 - 20000)
model.Add(xa4 + xb4 == 1.5*xa3 + 1.13*xb2 + 1.28*xc1 - 22000)
model.Add(xa5 == 1.5*xa4 + 1.13*xb3 + 1.28*xc2 + 1.40*xd1 - 24000)
model.Add( 1.5*xa5 + 1.13*xb4 + 1.28*xc3 + 1.40*xd2 == 26000)

model.Add(xc1 + xd1 <= 0.20*(xa1 + xb1 + xc1 + xd1))
model.Add(xc1 + xd1 + xc2 + xd2 <= 0.20*(xc1 + xd1 + xc2 + xd2 + xb1 + xa2 + xb2))
model.Add(xc1 + xd1 + xc2 + xd2 + xc3 <= 0.20*(xc1 + xd1 + xc2 + xd2 + xc3 + xb2 + xa3 + xb3))
model.Add(xd1 + xc2 + xd2 + xc3 <= 0.20*(xd1 + xc2 + xd2 + xc3 + xb3 + xa4 + xb4))
model.Add(xd2 + xc3 <= 0.20*(xd2 + xc3 + xb4 + xa5))

# Función Objetivo
model.Maximize(xa1 + xb1 + xc1 + xd1)

# Llamada a Solver
status = model.Solve()

#Impresión de resultados
if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
    print('El valor de la función objetivo es z = ', model.Objective().Value())
    print('xa1 = ', xa1.solution_value(), '\n')
    print('xa2 = ', xa2.solution_value(), '\n')
    print('xa3 = ', xa3.solution_value(), '\n')
    print('xa4 = ', xa4.solution_value(), '\n')
    print('xa5 = ', xa5.solution_value(), '\n')
    print('xb1 = ', xb1.solution_value(), '\n')
    print('xb2 = ', xb2.solution_value(), '\n')
    print('xb3 = ', xb3.solution_value(), '\n')
    print('xb4 = ', xb4.solution_value(), '\n')
    print('xc1 = ', xc1.solution_value(), '\n')
    print('xc2 = ', xc2.solution_value(), '\n')
    print('xc3 = ', xc3.solution_value(), '\n')
    print('xd1 = ', xd1.solution_value(), '\n')
    print('xd2 = ', xd2.solution_value(), '\n')

