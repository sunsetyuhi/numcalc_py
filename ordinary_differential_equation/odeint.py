#連立常微分方程式を解く
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#1階常微分方程式（放射性崩壊）
def func_dydt(y, t):
    dydt = -y

    return dydt


#1階連立常微分方程式（Lorenz方程式）
def func_lorenz(var, t, p, r, b):
    dxdt = -p*var[0] +p*var[1]
    dydt = -var[0]*var[2] +r*var[0] -var[1]
    dzdt = var[0]*var[1] -b*var[2]

    return [dxdt, dydt, dzdt]


#2階常微分方程式（運動方程式、自由落下）
def func_motion(var, t):
    dxdt = var[1]
    dvdt = -gravity

    return [dxdt, dvdt]


#2d可視化
def plot2d(t_list, y_list, t_label, y_label):
    plt.xlabel(t_label)  #x軸の名前
    plt.ylabel(y_label)  #y軸の名前
    plt.grid()  #点線の目盛りを表示
    plt.plot(t_list, y_list)

    plt.show()


#3d可視化
def plot3d(t_list, var_list):
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.set_xlabel("$x$")  #x軸の名前
    ax.set_ylabel("$y$")  #y軸の名前
    ax.set_zlabel("$z$")  #z軸の名前
    ax.plot(var_list[:, 0], var_list[:, 1], var_list[:, 2])

    plt.show()


#メイン実行部
if (__name__ == '__main__'):
    #1階常微分方程式（放射性崩壊）
    t_list = np.linspace(0.0, 10.0, 1000)
    y_init = 1.0  #初期値
    y_list = odeint(func_dydt, y_init, t_list)
    print(y_list)

    #可視化
    plot2d(t_list, y_list[:, 0], "$t$", "$y(t)$")


    #1階連立常微分方程式（Lorenz方程式）
    t_list = np.linspace(0.0, 100.0, 10000)
    p = 10
    r = 28
    b = 8/3
    var_init = [0.1, 0.1, 0.1]  #3次元座標上での初期値
    var_list = odeint(func_lorenz, var_init, t_list, args=(p, r, b))
    print(var_list)

    #可視化
    plot3d(t_list, var_list)


    #2階常微分方程式（運動方程式、自由落下）
    t_list = np.linspace(0.0, 5.0, 1000)
    v0 = 0.0  #初速度
    gravity = 9.80665  #重力加速度
    m_init = [100.0, 0.0]  #高さと速度の初期値
    m_list = odeint(func_motion, m_init, t_list)
    print(m_list)

    #可視化
    plot2d(t_list, m_list[:, 0], "$t$", "$x(t)$")
    plot2d(t_list, m_list[:, 1], "$t$", "$v(t)$")
