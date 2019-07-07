import scipy.optimize

def func_f1(x):
    return x**2.0 -2.0

#二分法
result1 = scipy.optimize.bisect(func_f1, 1.0, 2.0)
print(result1)

#Brent法
result2 = scipy.optimize.brentq(func_f1, 1.0, 2.0)
print(result2)



import sympy

x = sympy.Symbol("x")
result = sympy.solve(x**2.0 -2.0, x)
print(result)
