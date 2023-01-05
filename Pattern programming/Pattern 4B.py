"""
    A
   B B
  C C C
 D D D D
E E E E E
"""

n=5
for i in range(1,n+1):
    for j in range(n,i,-1):
        print("",end=" ")
    for k in range(1,i+1):
        print(chr(i+64),end=" ")
    print()
