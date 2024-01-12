from ortools.linear_solver import pywraplp

model = pywraplp.Solver.CreateSolver('SCIP')
#model = pywraplp.Solver('model_name', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

#Variables enteras

x1 = model.IntVar(0, 1, 'x1')
x2 = model.IntVar(0, 1, 'x2')

# Variables continuas
x11 = model.NumVar(0, model.infinity(), 'x11')
x21 = model.NumVar(0, model.infinity(), 'x21')
x31 = model.NumVar(0, model.infinity(), 'x31')

x12 = model.NumVar(0, model.infinity(), 'x12')
x22 = model.NumVar(0, model.infinity(), 'x22')
x32 = model.NumVar(0, model.infinity(), 'x32')

# Restricciones

model.Add(x1 + x2 == 1)
model.Add(x11 + x12 >= 75000)
model.Add(x21 + x22 >= 100000)
model.Add(x31 + x32 >= 200000)
model.Add(x11 <= 9000000*x1)
model.Add(x21 <= 9000000*x1)
model.Add(x31 <= 9000000*x1)
model.Add(x12 <= 9000000*x2)
model.Add(x22 <= 9000000*x2)
model.Add(x32 <= 9000000*x2)

#Solucion

model.Minimize(2000000*x1 + 1750000*x2 + 15*x11 + 13*x21 + 10*x31 + 16*x12 + 12*x22 + 9*x32)

# Solve
status = model.Solve()

if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
    print('objetive value z = ', model.Objective().Value(), '\n')
    print('x1 = ', x1.solution_value(), '\n')
    print('x2 = ', x2.solution_value(), '\n')
    print('x11 = ', x11.solution_value(), '\n')
    print('x12 = ', x21.solution_value(), '\n')
    print('x13 = ', x31.solution_value(), '\n')
    print('x12 = ', x12.solution_value(), '\n')
    print('x22 = ', x22.solution_value(), '\n')
    print('x32 = ', x32.solution_value(), '\n')



