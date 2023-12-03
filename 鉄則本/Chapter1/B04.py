# N = int(input())

#どうやってinputを各桁ごとに処理する？
#inputの時点で文字列型だった

N = input()
Nlen = len(N)
goukei = 0

for i, index in enumerate(N):
  kaijou = Nlen - i - 1
  goukei += int(index) * (2 ** kaijou)

print(goukei)