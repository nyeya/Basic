"""
1
2 3
3 4 5
4 5 6 7
5 6 7 8 9
"""

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print((i+j-1),end="\t")
        count+=1
    print()
