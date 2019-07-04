import numpy as np  #数値計算用モジュール
import bisection


def func_f1(x):
    return x**2.0 -3.0

solution1 = bisection.bisection(func_f1, 1.0, 2.0, 1e-15)
bisection.visualization(func_f1, solution1-1.0, solution1+1.0, solution1)


def func_f2(x):
    return np.arctan(x)

solution2 = bisection.bisection(func_f2, -1.0, 1.0, 1e-10)
bisection.visualization(func_f2, solution2-1.0, solution2+1.0, solution2)
