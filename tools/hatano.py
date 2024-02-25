import random
import sympy

def fermat_primegen(p_iv, k):
    p = p_iv
    if p % 2 == 0: # pが2でない偶数ならpは素数でない (ivが奇数より解析2.1では不要)
        p += 1
    P = [2,3,5,7,11,13,17,19,23,29] # フェルマー法に利用する10個の小さい素数
    while True:
        for i in range(k):
            a = P[i]
            if euclid(a, p) != 1: # aとpが互いに素でないならpは素数でない (1<a<p)
            break
      elif fermat_test(a, p) == False: # フェルマーテストの結果がFalseならpは素数でない
        break
      elif i == k - 1:
        return p # k回フェルマーテストでTrue判定ならpを素数とみなして出力
    p += 2
  E = [128, 256, 512, 1024] # 生成する素数のビット数
  k = 10 # フェルマーテストの実行回数
  for e in E:
    prime = []
    p_iv = (1<<(e-1))+1 # 初期値を 𝟐^(𝒆−𝟏) +1 (eビットの最小の奇数)
    while len(prime) != 10:
      p = fermat_primegen(p_iv, k)
      prime.append(p)
      p_iv = p+1
    P.append(prime)
  print("演習2.2の解答")
  for i in range(4):
    count = 0
    for p in P[i]:
      if sympy.isprime(p) == False:
        count += 1
    print("{}ビットの素数の生成確率={}".format(E[i], 1-(count/10)))
  for i in range(4): # 生成した素数を表示
    print(P[i])