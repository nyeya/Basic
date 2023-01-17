"""
     A
    ABC
   ABCDE
  ABCDEFG
 ABCDEFGHI
"""

n=5
start = 1
for i in range(0,n):
    for j in range(n,i,-1):
        print(end=" ")
    for k in range(start):
        print(chr(k+65),end="")
    start+=2
    print()
