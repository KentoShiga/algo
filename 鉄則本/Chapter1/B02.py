#全探索
A, B = map(int, input().split())

x = range(A, B+1)
flag = False

for i in x:
  if 100 % i == 0:
    print("Yes")
    flag = True
    exit()

if flag == False:
  print("No")
