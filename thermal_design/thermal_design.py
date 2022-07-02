import scipy.optimize


#方程式の関数項を定義
def func_Q_in(T_hi):
    return P


def func_Q_out(T_hi):
    Q_cd = A_cd*lamb/leng * (T_hi -T_lo)
    Q_rd = A_rd*sigma*epsilon * (T_hi**4 -T_lo**4)
    Q_cv = A_cv*h_tr * (T_hi -T_lo)
    
    return Q_cd +Q_rd +Q_cv


def func_f(T_hi):
    return func_Q_out(T_hi) -func_Q_in(T_hi)


P = 20
T_lo = 300

A_cd = 0.01
lamb = 0.2  #ABS
#lamb = 200  #アルミニウム
leng = 0.1

A_rd = 0.05
sigma = 5.67*10**(-8)
epsilon = 0.9  #ABS
#epsilon = 0.02  #アルミニウム

A_cv = 0.05
h_tr = 10


#300<T_hi<100000と見積もって方程式を解く
equip_temp = scipy.optimize.brentq(func_f, 300, 100000)
print("Equipment temperature =", equip_temp, "[K]")

heat_discharge = func_Q_out(equip_temp)
print("Heat discharge =", heat_discharge, "[W]")
