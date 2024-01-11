#明確な実数が存在しない場合、for文である程度回して近似値を求める
# N = int(input())
# left = 0
# right = N


#whileを使うとTLEになる
# while right > left:
#実数のときはmidが整数になるとは限らない
#   mid = (left + right) // 2
#   if(mid ** 3 + mid == N):
#     print(mid)
#     break
#   elif(mid ** 3 + mid < N):
#実数の時は+1をしない
#     left = mid + 1
#   else:
#     right = mid - 1

#x ** 3 + xは単調増加なので、-を考えなくてもいい

# left = -N
# right = 0

# while right > left:
#   mid = (left + right) // 2
#   if(mid ** 3 + mid == N):
#     print(mid)
#     break
#   elif(mid ** 3 + mid < N):
#     left = mid + 1
#   else:
#     right = mid - 1

N = int(input())
left = 0.0
right = 100.0

for i in range(20):
  mid = (left + right) / 2
  if(mid ** 3 + mid == N):
    break
  elif(mid ** 3 + mid < N):
    left = mid
  else:
    right = mid
print(left)