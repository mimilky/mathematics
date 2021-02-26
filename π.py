# -*- coding: utf-8 -*-
import time


#M1項
def pi1():
    d = 1
    zero = [0 for _ in range(global_digit)] #要素0を桁数分格納
    work2 = divide([1,6]+[0 for _ in range(global_digit-2)], 5) #work2の初期値16を1桁ずつ先頭から格納し、残りの要素は0で埋めた後5で除算
    work1 = work2 #work1(部分和)にwork2をコピー
    work3 = []

    for i in range(720): 
        if work2 == zero: #work2かwork3が0になったらbreak
            break
        if work3 == zero:
            break
        else:
            work2 = divide(work2, 5*5) #work2を5^2で除算
            d += 2
            work3 = divide(work2, d) #work2をdで除算したものをwork3に格納
            if d%4 == 1: 
                work1 = add(work1, work3) #work1とwork3を加算し、work1に格納
            if d%4 == 3: 
                work1 = sub(work1, work3) #work1からwork3を減算し、work1に格納
    return work1

#M2項
def pi2():
    d = 1
    zero = [0 for _ in range(global_digit)] 
    work2 = divide([0,4] + [0 for _ in range(global_digit-2)], 239) #work2の初期値4を先頭から1桁ずつ格納し、残りの要素は0で埋めた後239で除算
    work1 = work2
    work3 = []
    for i in range(220):
        if work2 == zero:
            break
        if work3 == zero:
            break
        else:
            work2 = divide(work2, 239*239) #work2を239^2で除算
            d += 2
            work3 = divide(work2, d)
            if d%4 == 1:
                work1 = add(work1, work3) 
            if d%4 == 3:
                work1 = sub(work1, work3)
    return work1


#加算(1桁ずつ)
def add(a,b):
    cr = 0 #繰り上げ
    z = [0 for _ in range(global_digit)] #0を桁数分格納
    for j in reversed(range(global_digit)): #逆順で計算
        z[j] = a[j] + b[j] + cr #それぞれの要素を計算
        if z[j] >= 10: #繰り上がるとき(加算結果が10以上のとき)
            z[j] -= 10 #加算結果から10を減算
            cr = 1 
        else :
            cr = 0
    return z


#減算(1桁ずつ)
def sub(a,b):
    br = 0 #繰り下げ
    z = [0 for _ in range(global_digit)] 
    for i in reversed(range(global_digit)): 
        z[i] = a[i] - b[i] - br
        if z[i] >= 0: #繰り下がらないとき(減算結果が正のとき)
            br = 0
        else: #繰り下がるとき
            z[i] += 10 #(減算結果に10を加算)
            br = 1
    return z


#除算(1桁ずつ)
def divide(a,b):
    x = a + [0 for _ in range(global_digit-len(str(a)))] #xにaを代入し残りを0で埋める
    z = [0 for _ in range(global_digit)]

    for i in range(global_digit-1): #桁数-1回
        if b > x[i]: #序数>被除数のとき
            q,l = divmod(x[i]*10 + x[i+1], b) #現在の要素(i)を10倍して次の要素(i+1)と加算した後にbで除算、qを商、lを剰余
            x[i+1] = l #次の要素を代入
            z[i+1] = q #次要素の商として代入
        else :
            q,l = divmod(a,b)
            x[i+1] = l
            z[i] = q #現在要素の商なので、i+1ではなくi
    return z

#検算
def verify():
    #円周率1000桁
    define_pi=31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989
    pi_list = ([0]+[int(d) for d in str(define_pi)]) #円周率を1桁ずつの配列として格納
    if pi_list==sub(pi1(),pi2())[:global_digit-3]: #計算した円周率と実際の円周率を比較して、一致したとき
        print('verify:ok')
    else:
        print('verify:failed')

#main
if __name__ == "__main__":
    global_digit = 1005 #桁数(精度の関係で多め)
    t1 = time.time() #処理時間
    print(sub(pi1(),pi2())[:global_digit-3]) #M1項-M2項(円周率)
    verify() #検算
    print(f'処理時間:{time.time()-t1}')
