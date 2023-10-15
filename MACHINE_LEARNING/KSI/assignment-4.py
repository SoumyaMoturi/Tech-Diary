#trialing Zeroes
"""
n=input()
s=n[::-1]
c=0
for i in s:
    if(i=='0'):
        c=c+1
    else:
        break
print(c)
"""
"""

n=int(input())       
l1=[int(x) for x in input().split(' ')][:n]
l2=[int(x) for x in input().split(' ')][:n]
for i,j in enumerate(l2):
    if(l1[i]==j):
        l1[i]=0
        l2[i]=0
l3=l1.copy()
l1=l2.copy()
l2=l3.copy()
del l3
for i in l1:
    print(i,end=" ")
for i in l2:
    print(i,end=" ")
    
"""
n=int(input())
l1=[int(x) for x in input().split(' ')][:n]
l2=[int(x) for x in input().split(' ')][:n]
for i,j in enumerate(l2):
    if(l1[i]==j):
        l1[i]=0
        l2[i]=0
l1=l1+l2
l2=l1[0:n]
l1=l1[n:(n*2)]

for i in l1:
    print(i,end=" ")
print()
for i in l2:
    print(i,end=" ")
    
