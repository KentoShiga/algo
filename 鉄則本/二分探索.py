N = int(input())
K = int(input())

#1以上N以下の整数を3枚のカードに書き、その3枚のカードに書かれた数の合計がKになる整数の選び方を考える

#1枚目のカードに書かれた数をiとすると、2枚目のカードに書かれた数はK-iとなる
#3枚目のカードに書かれた数はK-i-(K-i)となる

l = 0

for i in range(1,N + 1):
  for j in range(1,N + 1):
    for k in range(1,N + 1):
      if i + j + k == K:
        # print("Yes")
        l += 1
print(l)

