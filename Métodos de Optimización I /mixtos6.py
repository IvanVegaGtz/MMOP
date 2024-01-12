from ortools.linear_solver import pywraplp

model = pywraplp.Solver.CreateSolver('SCIP')
#model = pywraplp.Solver('model_name', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

#Variables enteras

x11 = model.IntVar(0, 1, 'x11')
x12 = model.IntVar(0, 1, 'x12')
x13 = model.IntVar(0, 1, 'x13')
x14 = model.IntVar(0, 1, 'x14')
x15 = model.IntVar(0, 1, 'x15')
x16 = model.IntVar(0, 1, 'x16')

x21 = model.IntVar(0, 1, 'x21')
x22 = model.IntVar(0, 1, 'x22')
x23 = model.IntVar(0, 1, 'x23')
x24 = model.IntVar(0, 1, 'x24')
x25 = model.IntVar(0, 1, 'x25')
x26 = model.IntVar(0, 1, 'x26')

x31 = model.IntVar(0, 1, 'x31')
x32 = model.IntVar(0, 1, 'x32')
x33 = model.IntVar(0, 1, 'x33')
x34 = model.IntVar(0, 1, 'x34')
x35 = model.IntVar(0, 1, 'x35')
x36 = model.IntVar(0, 1, 'x36')


# Variables continuas
y1 = model.NumVar(0, model.infinity(), 'y1')
y2 = model.NumVar(0, model.infinity(), 'y2')
y3 = model.NumVar(0, model.infinity(), 'y3')
y4 = model.NumVar(0, model.infinity(), 'y4')
y5 = model.NumVar(0, model.infinity(), 'y5')
y6 = model.NumVar(0, model.infinity(), 'y6')

s1 = model.NumVar(0, model.infinity(), 's1')
s2 = model.NumVar(0, model.infinity(), 's2')
s3 = model.NumVar(0, model.infinity(), 's3')
s4 = model.NumVar(0, model.infinity(), 's4')
s5 = model.NumVar(0, model.infinity(), 's5')
s6 = model.NumVar(0, model.infinity(), 's6')





# Restricciones

model.Add(x11 + x21 <= 1)
model.Add(x12 + x22 <= 1)
model.Add(x13 + x23 <= 1)
model.Add(x14 + x24 <= 1)
model.Add(x15 + x25 <= 1)
model.Add(x16 + x26 <= 1)

model.Add(y1 <= 5000 x11 + 7500 x21)
model.Add(y2 <= 5000 x12 + 7500 x22)
model.Add(y3 <= 5000 x13 + 7500 x23)
model.Add(y4 <= 5000 x14 + 7500 x24)
model.Add(y5 <= 5000 x15 + 7500 x25)
model.Add(y6 <= 5000 x16 + 7500 x26)

model.Add( x11 + x22 <= x32)
model.Add( x12 + x23 <= x33)
model.Add( x13 + x24 <= x34)
model.Add( x14 + x25 <= x35)
model.Add( x15 + x26 <= x36)


model.Add( s1 == 3000 + y1 - 6000)
model.Add( s2 == s1 + y1 - 6500)
model.Add( s3 == s2 + y1 - 7500)
model.Add( s4 == s3 + y1 - 7000)
model.Add( s5 == s4 + y1 - 6000)
model.Add( s6 == s5 + y1 - 6000)
model.Add( s6 >= 2000)

model.Add( 2000*(x11 + x21) <= y1)



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



