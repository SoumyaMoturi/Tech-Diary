import math
def addSub(n):
    total=0
    s=""
    for i in range(1,n+1):
        s+=str(i)
        if(i%2==0):
            if(i!=n):
                s+="+"
            total-=i
        else:
            if(i!=n):
                s+="-"
            total+=i
    print(s," = " ,total)

def powSeries(n):
    sum=0
    s=""
    for i in range(1,n+1):
        if(i!=n):
            s+=str(i)+"/"+str(n)+"^"+str(i)+"+"
        else:
            s+=str(i)+"/"+str(n)+"^"+str(i)
        sum+=(i)/(math.pow(n,i))
    print(s," = ",sum)
        
def reverseNum(n):
    rev=0
    k=n
    while(n>0):
        rev=rev*10+n%10
        n=n//10
    print("Reverse of",k,"is: ",rev)

addSub(5)
powSeries(5)
reverseNum(5)