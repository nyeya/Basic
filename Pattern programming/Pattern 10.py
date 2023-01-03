"""
1
3	5
5	7	9
7	9	11	13
9	11	13	15	17
"""

n=5
temp=0
for i in range(1,n+1):
    temp = (2*i)-1
    for j in range(1,i+1):
        print((temp),end="\t")
        temp+=2
    print()
