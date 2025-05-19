import sympy as sp

# Definir la variable simbólica
x = sp.symbols('x')

# Definir la ecuación
equation = x**2 + 2*x - 3 

# Resolver la ecuación
solutions = sp.solve(equation, x)
print(solutions)
#----------------------------------------------