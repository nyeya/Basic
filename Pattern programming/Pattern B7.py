"""
5 5 5 5 5
 4 4 4 4
  3 3 3
   2 2
    1
"""

n=5
for i in range(n,0,-1):
    for j in range(n,i,-1):
        print("",end=" ")
    for k in range(i):
        print(i,end=" ")
    print()
