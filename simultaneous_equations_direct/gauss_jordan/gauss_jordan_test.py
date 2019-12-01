import numpy as np  #数値計算用モジュール
#import scipy.linalg  #SciPyの線形計算ライブラリ
import gauss_jordan


mat_A1 = np.array([
    [ 2.0, 1.0, 1.0],
    [ 1.0, 2.0, 1.0],
    [ 1.0, 1.0, 2.0]
])
vec_b1 = np.array(
    [ 7.0, 8.0, 9.0]
)
vec_x1 = gauss_jordan.gauss_jordan(mat_A1,vec_b1)
#vec_x1 = scipy.linalg.solve(mat_A1,vec_b1)
print("vec_x1 = ", vec_x1)
gauss_jordan.solution_check(mat_A1, vec_b1, vec_x1)  #解の検算
print()


mat_A2 = np.array([
    [ 1.0, 2.0, 3.0],
    [ 5.0, 6.0, 7.0],
    [ 9.0,10.0,11.0]
])
vec_b2 = np.array(
    [ 4.0, 8.0,12.0]
)
vec_x2 = gauss_jordan.gauss_jordan(mat_A2,vec_b2, process=True)
#vec_x2 = scipy.linalg.solve(mat_A2,vec_b2)
print("vec_x2 = ", vec_x2)
gauss_jordan.solution_check(mat_A2, vec_b2, vec_x2)  #解の検算
print()
