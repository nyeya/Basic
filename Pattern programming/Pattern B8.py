"""
5 4 3 2 1
 4 3 2 1
  3 2 1
   2 1
    1
"""

n=5
for i in range(n,0,-1):
    for j in range(n,i,-1):
        print("",end=" ")
    for k in range(i,0,-1):
        print(k,end=" ")
    print()
