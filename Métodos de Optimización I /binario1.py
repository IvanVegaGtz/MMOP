from ortools.linear_solver import pywraplp

model = pywraplp.Solver.CreateSolver('SCIP')
#model = pywraplp.Solver('model_name', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

#Variables
x11 = model.IntVar(0, 1, 'x11')
x12 = model.IntVar(0, 1, 'x12')
x13 = model.IntVar(0, 1, 'x13')
x14 = model.IntVar(0, 1, 'x14')
x15 = model.IntVar(0, 1, 'x15')
x21 = model.IntVar(0, 1, 'x21')
x22 = model.IntVar(0, 1, 'x22')
x23 = model.IntVar(0, 1, 'x23')
x24 = model.IntVar(0, 1, 'x24')
x25 = model.IntVar(0, 1, 'x25')
x31 = model.IntVar(0, 1, 'x31')
x32 = model.IntVar(0, 1, 'x32')
x33 = model.IntVar(0, 1, 'x33')
x34 = model.IntVar(0, 1, 'x34')
x35 = model.IntVar(0, 1, 'x35')
x41 = model.IntVar(0, 1, 'x41')
x42 = model.IntVar(0, 1, 'x42')
x43 = model.IntVar(0, 1, 'x43')
x44 = model.IntVar(0, 1, 'x44')
x45 = model.IntVar(0, 1, 'x45')
x51 = model.IntVar(0, 1, 'x51')
x52 = model.IntVar(0, 1, 'x52')
x53 = model.IntVar(0, 1, 'x53')
x54 = model.IntVar(0, 1, 'x54')
x55 = model.IntVar(0, 1, 'x55')

#Restricciones

model.Add(x11 + x12 + x13 + x14 + x15 == 1)
model.Add(x21 + x22 + x23 + x24 + x25 == 1)
model.Add(x31 + x32 + x33 + x34 + x35 == 1)
model.Add(x41 + x42 + x43 + x44 + x45 == 1)
model.Add(x51 + x52 + x53 + x54 + x55 == 1)

model.Add(x11 + x21 + x31 + x41 + x51 == 1)
model.Add(x12 + x22 + x32 + x42 + x52 == 1)
model.Add(x13 + x23 + x33 + x43 + x53 == 1)
model.Add(x14 + x24 + x34 + x44 + x54 == 1)
model.Add(x15 + x25 + x35 + x45 + x55 == 1)



#Funcion objetivo

model.Minimize( 16*x11 + 4*x12 + 9*x13 + 5*x14 + 6*x15 + 2*x21 + 14*x22 + 7*x23 + 5*x24 + 13*x25 + 8*x31 + 10*x32 + 3*x33 + 12*x34 + 11*x35 + 3*x41 + 7*x42 + 6*x43 + 10*x44 + 5*x45 + 3*x51 + 6*x52 + 8*x53 + 11*x54 + 7*x55)

#Solucion
status = model.Solve()

#Imprimir solucion

if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
    print('objetive value z = ', model.Objective().Value(), '\n')
    print('x11 = ', x11.solution_value(), '\n')
    print('x12 = ', x12.solution_value(), '\n')
    print('x13 = ', x13.solution_value(), '\n')
    print('x14 = ', x14.solution_value(), '\n')
    print('x15 = ', x15.solution_value(), '\n')
    print('x21 = ', x21.solution_value(), '\n')
    print('x22 = ', x22.solution_value(), '\n')
    print('x23 = ', x23.solution_value(), '\n')
    print('x24 = ', x24.solution_value(), '\n')
    print('x25 = ', x25.solution_value(), '\n')
    print('x31 = ', x31.solution_value(), '\n')
    print('x32 = ', x32.solution_value(), '\n')
    print('x33 = ', x33.solution_value(), '\n')
    print('x34 = ', x34.solution_value(), '\n')
    print('x35 = ', x35.solution_value(), '\n')
    print('x41 = ', x41.solution_value(), '\n')
    print('x42 = ', x42.solution_value(), '\n')
    print('x43 = ', x43.solution_value(), '\n')
    print('x44 = ', x44.solution_value(), '\n')
    print('x45 = ', x45.solution_value(), '\n')
    print('x51 = ', x51.solution_value(), '\n')
    print('x52 = ', x52.solution_value(), '\n')
    print('x53 = ', x53.solution_value(), '\n')
    print('x54 = ', x54.solution_value(), '\n')
    print('x55 = ', x55.solution_value(), '\n')
