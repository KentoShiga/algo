#%は余りを求める演算子！！
N = int(input())
for i in [9,8,7,6,5,4,3,2,1,0]:
  waru = 2 ** i
  warareru = N / waru
  print(int(warareru % 2), end="")
print("\n")
