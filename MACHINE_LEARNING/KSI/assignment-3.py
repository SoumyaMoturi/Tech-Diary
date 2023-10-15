def common(n):
    l1=[int(x) for x in input().split(' ')][:n]
    l2=[int(x) for x in input().split(' ')][:n]
    for i in l2:
        if i in l1:
            print(i)
            
def consecutive_Vowels(s):
    vowels='aeiou'
    s=s.lower()
    print(s)
    words=s.split(' ')
    for i in words:
        for j in range(0,len(i)-1):
            if i[j] in vowels and i[j+1] in vowels:
                print(i)
                
n=int(input())
s=input()
common(n)
consecutive_Vowels(s)
