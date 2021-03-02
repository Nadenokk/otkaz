import sympy as sp

Result = []
x, y, z = sp.symbols('x, y, z')

f1 = ((5 - x) ** 2) + ((8 - y) ** 2) + ((9 - z) ** 2) - (4.680 ** 2)
f2 = ((6 - x) ** 2) + ((7 - y) ** 2) + ((15 - z) ** 2) - (10.522 ** 2)
f3 = ((9 - x) ** 2) + ((14 - y) ** 2) + ((10 - z) ** 2) - (9.889 ** 2)

Result.append(sp.solve((f1, f2, f3), (x, y, z)))
print(Result[0][1])
