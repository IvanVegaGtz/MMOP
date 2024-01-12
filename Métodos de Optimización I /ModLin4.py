from ortools.linear_solver import pywraplp

model = pywraplp.Solver("Modelo_lineal_4", pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

x11 = model.NumVar(0, model.infinity(), 'x11')
x12 = model.NumVar(0, model.infinity(), 'x12')
x13 = model.NumVar(0, model.infinity(), 'x13')
x21 = model.NumVar(0, model.infinity(), 'x21')
x22 = model.NumVar(0, model.infinity(), 'x22')
x23 = model.NumVar(0, model.infinity(), 'x23')

model.Add( x11 + x12 + x13 <= 10000)
model.Add( x21 + x22 + x23 <= 15000)

model.Add(x11 + x21 >= 6000)
model.Add(x12 + x22 >= 7000)
model.Add(x13 + x23 >= 9000)

model.Add(0.4*x11 + 0.2*x21 >= 0.3*(x11 + x21))
model.Add(0.4*x12 + 0.2*x22 <= 0.3*(x12 + x22))
model.Add(x13 >= 0.3*x23)

model.Maximize( 125*(x11 + x21) + 135*(x12 + x22) + 155*(x13 + x23))

status = model.Solve()

if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
    print("La solución óptima es z = ", model.Objective().Value())
    print(x11, '=', x11.solution_value())
    print(x12, '=', x12.solution_value())
    print(x13, '=', x13.solution_value())
    print(x21, '=', x21.solution_value())
    print(x22, '=', x22.solution_value())
    print(x23, '=', x23.solution_value())