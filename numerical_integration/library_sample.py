import numpy as np  #NumPyライブラリ
from scipy import integrate


def func_f1(x):
    return 3.0*x**2.0
result1 = integrate.quad(func_f1, -1.0, 1.0)
print(result1)


def func_f2(x):
    return np.sin(x)/x
result2 = integrate.quad(func_f2, 0.0, 2.0*np.pi)
print(result2)
