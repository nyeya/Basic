"""
5 5 5 5 5
 4 4 4 4
  3 3 3
   2 2
    1
"""

n=5
start = 1
for i in range(0,n):
    for j in range(n,i,-1):
        print(end=" ")
    for k in range(start):
        print("*",end="")
    start+=2
    print()
