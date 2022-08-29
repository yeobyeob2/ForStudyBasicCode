'''
#2739
n=int(input())
for i in range(1,10):
    print(n, "*", i, "=", n*i)


#10950
T=int(input())
for i in range(T):
    a, b=map(int, input().split())
    print(a+b)

#8393
n=int(input())
m=0
for i in range(n+1):
    m += i
print(m)

#25304
x=int(input())
n=int(input())
list=[]
for i in range(n):
    a, b=map(int, input().split())
    list.append(a*b)
if sum(list) == x:
    print("Yes")
else:
    print("No")

#15552 *
import sys
T=int(sys.stdin.readline())
for _ in range(T):
    A, B=map(int, sys.stdin.readline().split())
    print(A+B)

#11021
n=int(input())
for i in range(1,n+1):
    a, b=map(int, input().split())
    print("Case #%d: %d"%(i,a+b))

#11022
n=int(input())
for i in range(1,n+1):
    a, b=map(int, input().split())
    print("Case #%d: %d + %d = %d"%(i,a,b,a+b))

#2438
n=int(input())
for i in range(1,n+1):
    print("*"*i)

#2439 *
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)

#10871 *
n, x=map(int, input().split())
z = list(map(int, input().split()))

for i in range(n):
    if z[i] < x:
        print(z[i],end=" ")

#10952
while True:
    a, b=map(int, input().split())

    if a == 0 and b == 0:
        break

    else:
        print(a+b)

#10951 *
while 1:
    try:
        a, b=map(int, input().split())
        print(a+b)
    except:
        break
'''
#1110 *
n=int(input())
num=n
cnt=0
while True:
    a=num//10
    b=num%10
    c=(a+b)%10
    num=b*10+c

    cnt=cnt+1
    if num==n:
        break
print(cnt)