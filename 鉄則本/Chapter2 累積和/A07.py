D = int(input())
N = int(input())
Rational = [0] * D
CumSum = [None] * (D + 1)
CumSum[0] = 0

#引っ掛かりポイント1: Dで回さない。入力された値がどの制約に当てはまるかを考える
for i in range(N):
    start, end = map(int, input().split())
    Rational[start - 1] += 1
    #引っ掛かりポイント2: ここでendがDになると、Rational[end]が存在しないのでエラーになる
    if(end != D):
      Rational[end] -= 1
      
#引っ掛かりポイント3: Rational[0]は、0日目から1日目での増加量を示す
for k in range(D):
    CumSum[k + 1] = CumSum[k] + Rational[k]
    print(CumSum[k + 1])