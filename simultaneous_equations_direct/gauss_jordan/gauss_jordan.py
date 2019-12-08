#Gauss-Jordan法による線型連立方程式の解法プログラム
import numpy as np  #NumPyライブラリ
import matplotlib.pyplot as plt  #データ可視化ライブラリ
import numba  #最適化ライブラリ


#解きたい連立方程式の係数行列
mat_A = np.array([
    [ 1.0, 2.0],
    [ 4.0, 5.0]
])
vec_b = np.array(
    [ 3.0, 6.0]
)


#Gauss-Jordan法（係数行列、係数ベクトル、途中計算表示、微小量）
@numba.jit  #JITで最適化
def gauss_jordan(mat_A, vec_b, process=False, eps=1e-10):
    #拡大係数行列を用意
    vec_b = np.reshape(vec_b, (-1,1))  #列ベクトルに変換
    mat_Ab = np.concatenate((mat_A, vec_b), axis=1)  #横方向に結合
    num_vec_x = mat_Ab.shape[0]  #未知数の数

    #行列の確認
    if (process==True):
        print("pre matrix = ")
        print(mat_Ab)

    #各行でpivot選択して掃き出す
    for pivot in range(num_vec_x):
        #pivot列で成分の絶対値が最大の行を探す
        row_max = pivot
        val_max = mat_Ab[pivot,pivot]
        for row in range(pivot+1, num_vec_x):
            if (val_max < abs(mat_Ab[row,pivot])):
                row_max = row
                val_max = abs(mat_Ab[row,pivot])

        #pivotが小さかったら（係数行列が非正則だったら）例外を発生させる
        if(abs(val_max) < eps):
            print("error: pivot (=", val_max, ") is too small (<=", eps, ").")
            if(abs(mat_Ab[pivot,num_vec_x]) < eps):
                raise Exception("連立方程式は不定です。")
            else:
                raise Excaption("連立方程式は不能（解なし）です。")
            #quit()
        elif(process==True):
            print("pivot = ",val_max)

        #pivotの行と入れ替え
        if (pivot != row_max):
            mat_Ab[pivot,:], mat_Ab[row_max,:] = mat_Ab[row_max,:], mat_Ab[pivot,:].copy()

        #pivot行をpivotで割る(mat_Ab[pivot,pivot]=1にする)
        mat_Ab[pivot, :] = mat_Ab[pivot, :]/val_max

        #掃き出し操作で、mat_Ab[pivot,pivot]より下の係数を0にする
        for row in range(0, num_vec_x):
            #pivot行をmat_Ab[row,pivot]倍してrow行から引く
            if row != pivot:
                pivot_row = mat_Ab[row, pivot]*mat_Ab[pivot, range(pivot, num_vec_x+1)]
                mat_Ab[row, range(pivot, num_vec_x+1)] -= pivot_row

            #val_pivot = mat_Ab[row,pivot]
            #for col in range(pivot, num_vec_x+1):
            #    if (row != pivot):
            #        mat_Ab[row,col] -= val_pivot*mat_Ab[pivot,col]

        if (process==True):
            print(mat_Ab)

    #行列の確認
    if (process==True):
        print("Post matrix = ")
        print(mat_Ab)

    #解の取り出し
    return mat_Ab[:, num_vec_x]


#解の検算
def solution_check(mat_A, vec_b, vec_x):
    print('vec_b = ', vec_b)
    print('Calculated vec_b = ', np.dot(mat_A, vec_x))


#メイン実行部
if (__name__ == '__main__'):
    #Gauss-Jordan法で線型連立方程式の解を計算
    vec_x = gauss_jordan(mat_A, vec_b, process=True)
    print("vec_x = ", vec_x)
    print()

    #解の検算
    solution_check(mat_A, vec_b, vec_x)
