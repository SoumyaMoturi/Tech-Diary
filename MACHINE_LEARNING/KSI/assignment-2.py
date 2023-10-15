from math import sqrt
def areaOfRectangle():
    breadth=int(input("Enter the breadth of rectangles: "))
    n=int(input("No of rectangles: " ))
    length=0
    length=sum(list(map(int,input("Enter lengths of all rectangles: ").strip().split()))[:n])
    print("Area of the largest rectangle is {}.".format(length*breadth))

def perfectCube():
    n=int(input("Enter an integer number: " ))
    l=[i*i*i for i in range(1,1001)]
    if n in l:
        print("Yes! Its a perfect Cube")
    else:
        print("No! Its not a perfect Cube")

def l6h12():
    n=int(input("Enter a positive integer: "))
    if(n%6==0 and n%12!=0):
        print("Yes! I like that")
    elif(n%12==0 and  n%6!=0):
        print("No! I dislike it")
    elif(n%6==0 and n%12==0):
        print("Number is divisible by both 6 and 12")
    else:
        print("neither the number is divisible by 6 nor 12")

def timeToReach():
	n=int(input("Enter number of floors: "))
  	time=[round(sqrt((2*s)/(9.8)),6) for s in range(0,((n+1)*3),3)]
  	print(time)

areaOfRectangle()
perfectCube()      
l6h12()
timeToReach()

