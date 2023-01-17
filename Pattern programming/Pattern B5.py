"""
     A
    A B
   A B C
  A B C D
 A B C D E
"""

n=5
for i in range(0,n):
    for j in range(n,i,-1):
        print("",end=" ")
    for k in range(0,i+1):
        print(chr(k+65),end=" ")
    print()
