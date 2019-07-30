#台形公式による数値積分プログラム
import numpy as np  #NumPyライブラリ
import matplotlib.pyplot as plt  #データ可視化ライブラリ


#定積分したい関数
def func_f(x):
    return 3.0*x**2.0


#台形公式（関数、定積分の開始点、定積分の終了点、刻み幅）
def trapezoidal(func_f, x_min, x_max, dx=1e-2):
    num_calc = 0  #計算回数
    x_div = (x_max-x_min)/dx  #格子分割数

    x = x_min  #独立変数x
    y = func_f(x)  #従属変数y
    print("x = {:.7f},  y = {:.7f}".format(x, y))

    #グラフ用データを追加
    x_list = [x]
    y_list = [y]

    #x = x_min
    area = 0.0  #積分値（面積）
    while(True):
        num_calc += 1  #計算回数を数える

        x += dx
        delta_area = (func_f(x-dx) +func_f(x))*dx/2.0
        area += delta_area

        #グラフ用データを追加
        x_list.append(x)
        y_list.append(func_f(x))

        #「計算回数が格子分割数以上」ならば終了
        if(x_div<=num_calc):
            break

        #「計算回数が閾値以上」かつ「面積が微小」ならば終了
        #if(x_div/2.0<=num_calc and delta_area<=1e-10):
            #break

    print("n = {:3d}:  area = {:.15f}".format(num_calc, area))

    return area, x_list, y_list


#可視化
def visualization(func_f, area, x_list, y_list):
    plt.xlabel("$x$")  #x軸の名前
    plt.ylabel("$f(x)$")  #y軸の名前
    plt.grid()  #点線の目盛りを表示
    plt.axhline(0, color='#000000')  #f(x)=0の線

    #関数
    exact_x = np.arange(x_list[0],x_list[-1], (x_list[-1]-x_list[0])/500.0)
    exact_y = func_f(exact_x)

    plt.plot(exact_x,exact_y, label="$y(t)$", color='#ff0000')  #折線グラフで表示
    plt.fill_between(x_list,y_list, alpha=0.2)  #塗りつぶし
    plt.text(x_list[0],y_list[0], "$x$ = {:.9f}".format(area), va='bottom', color='#0000ff')
    plt.show()  #グラフを表示


#メイン実行部
if (__name__ == '__main__'):
    #台形公式で定積分を求める
    area, x_list, y_list = trapezoidal(func_f, -1.0, 1.0)

    #結果を可視化
    visualization(func_f, area, x_list, y_list)
