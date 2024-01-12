from ortools.linear_solver import pywraplp

model = pywraplp.Solver("Modelo_lineal_5", pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

x1 = model.NumVar(0, model.infinity(), 'x1')
x2 = model.NumVar(0, model.infinity(), 'x2')

model.Add( x1/2000 + x2/1500 <= 1)
model.Add( x1 + x2 <= 2200)

model.Maximize( 2100*x1 + 3000*x2)

status = model.Solve()

if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
    print("La solución óptima es z = ", model.Objective().Value())