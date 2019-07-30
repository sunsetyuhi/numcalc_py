import numpy as np  #数値計算用モジュール
import trapezoidal


#標準正規分布
def func_f1(x):
    return 1.0/np.sqrt(2.0*np.pi)*np.exp(-x**2.0/2.0)

area1, x_list1, y_list1 = trapezoidal.trapezoidal(func_f1, -2.0, 2.0, dx=1e-4)
trapezoidal.visualization(func_f1, area1, x_list1, y_list1)


#sinc関数
def func_f2(x):
    return np.sin(x)/x

area2, x_list2, y_list2 = trapezoidal.trapezoidal(func_f2, 0.0, 2.0*np.pi)
trapezoidal.visualization(func_f2, area2, x_list2, y_list2)
