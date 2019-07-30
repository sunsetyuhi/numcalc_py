#Euler法による常微分方程式の解法プログラム
import numpy as np  #NumPyライブラリ
import matplotlib.pyplot as plt  #データ可視化ライブラリ


#導関数dy/dt
def func_dydt(t, y):
    return t**2.0 -3.0  #dy/dt = t^2 -3.0


#Euler法（導関数、tの初期値、yの初期値、刻み幅dt）
def euler(func_dydt, t, y, dt=1e-3):
    dy = func_dydt(t, y)*dt  #変化量を計算

    t += dt  #変数を更新
    y += dy  #変化量を加えて更新

    return t, y


#常微分方程式を逐次計算（導関数、yの初期値、tの開始点、tの終了点、刻み幅dt）
def ode_calc(func_dydt, y_start, t_start, t_end, dt=1e-2):
    num_calc = 0  #計算回数
    t_div = np.abs((t_end-t_start)/dt)  #格子分割数
    if(t_end<t_start):  #負の方向に計算する時は刻み幅の符号を反転
        dt = -dt

    #初期値
    t = t_start  #独立変数t
    y = y_start  #従属変数y
    print("t = {:.7f},  y = {:.7f}".format(t, y))

    #グラフ用データを追加
    t_list = [t]
    y_list = [y]

    #ずっと繰り返す
    while(True):
        t, y = euler(func_dydt, t, y, dt)
        print("t = {:.7f},  y = {:.7f}".format(t, y))

        #グラフ用データを追加
        t_list.append(t)
        y_list.append(y)

        num_calc += 1  #計算回数を数える

        #「計算回数が格子分割数以上」ならば終了
        if(t_div<=num_calc):
            print("Finished.")
            print()
            break

    return t_list, y_list


#可視化
def visualization(t_list, y_list):
    plt.xlabel("$t$")  #x軸の名前
    plt.ylabel("$y(t)$")  #y軸の名前
    plt.grid()  #点線の目盛りを表示

    plt.plot(t_list,y_list, label="$y(t)$", color='#ff0000')  #折線グラフで表示
    plt.legend(loc='best') #凡例(グラフラベル)を表示
    plt.show()  #グラフを表示


#メイン実行部
if (__name__ == '__main__'):
    #Euler法でdt離れた点の値を取得
    t, y = euler(func_dydt, 0.0, 0.0)
    print("t = {:.7f},  y = {:.7f}".format(t, y))

    #常微分方程式を逐次計算
    t_list, y_list = ode_calc(func_dydt, 0.0, -5.0, 5.0)

    #結果を可視化
    visualization(t_list, y_list)
