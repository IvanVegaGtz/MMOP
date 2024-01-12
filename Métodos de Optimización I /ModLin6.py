from ortools.linear_solver import pywraplp

model = pywraplp.Solver("Modelo_lineal_6", pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

x1 = model.NumVar(0, model.infinity(), 'x1')
x2 = model.NumVar(0, model.infinity(), 'x2')
x3 = model.NumVar(0, model.infinity(), 'x3')
x4 = model.NumVar(0, model.infinity(), 'x4')

model.Add( 12*x1 + 4*x2 + 4.8*x3 + 4*x4 >= 18000)
