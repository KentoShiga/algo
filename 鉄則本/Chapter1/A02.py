N,X = map(int,input().split())
A = list(map(int,input().split()))

Answer = False

for i in A:
  if i == X:
    print("Yes")
    Answer = True
    break

if Answer == False:
  print("No")

#別解
# if X in A:
#   print("Yes")
# else:
#   print("No")