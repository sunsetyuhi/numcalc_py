import numpy as np  #数値計算用モジュール
import euler


def func_dydt1(t, y):
    return np.cos(t)  #dy/dt = cos(t)

t_list1, y_list1 = euler.ode_calc(func_dydt1, 0.0, 5.0, -5.0, dt=1e-1)
euler.visualization(t_list1, y_list1)


def func_dydt2(t, y):
    return -y  #dy/dt = -y(t)

t_list2, y_list2 = euler.ode_calc(func_dydt2, 5.0, 0.0, 10.0)
euler.visualization(t_list2, y_list2)
