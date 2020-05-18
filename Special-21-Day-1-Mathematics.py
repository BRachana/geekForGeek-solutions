# M and N
import math
T = int(input())
while(T>0):
  T = T-1;
  M, N = [int(x) for x in input().split()]
 
  n = int(math.log10(N))+1
  m = int(math.log10(N))+1
  if m > n:
    print(M+N)
  elif m < n:
     print(N)
  else:
    total = M+N
    length = int(math.log10(total))+1
    if length == n:
      print(N)
    else:
      print(total)

# Triangle and Square
def numberOfSquares(base):
  base = (base - 2) 
  base = base / 2
  return base * (base + 1) / 2

T = int(input())
while(T>0):
  T = T-1;
  B = int(input())
  print(numberOfSquares(B)) 


