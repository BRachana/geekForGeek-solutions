# number of test cases
T = int(input())

def calcsum(A,S):
  sum = A[0]
  i , j = 1, 0
  flag = 0
  if sum == S:
      return(i,j)
  for x in range(1, len(A)):
    sum = sum + A[x]
    j = x 
    print(x,":", i, j, sum)
    while(sum > S) and x > i:
      sum = sum - A[i]
      i = i + 1
    if sum == S:
      return i,j
    
  return -1, 0


while(T>0):
  T = T-1;
  N, S = [int(x) for x in input().split()] 
  A = list(map(int,input().strip().split()))[:N]
  A.insert(0,0)
  i,j = calcsum(A,S)
  if i == -1:
    print (-1)
  else:
    print(i,j)
    


