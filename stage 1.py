
#2557
print("Hello World")

#10718
for i in range(2):
    print("강한친구 대한육군")

#1000
A, B=map(int, input().split())
print(A+B)

#1001
A, B=map(int, input().split())
print(A-B)

#10998
A, B=map(int, input().split())
print(A*B)

#1008
A, B=map(int, input().split())
print(A/B)

#10869
A, B=map(int, input().split())
print(A+B)
print(A-B)
print(A*B)
print(A%B)

#10926
a=input()
if a.islower() == True:
    if len(a) <= 50 :
        print(a+"??!")

#18108
y=int(input())
if 1000<= y <=3000:
    y=y-544
    print(y)

#3003
k, q, l, v, n, p=map(int, input().split())
k1, q1, l1, v1, n1, p1 = 1, 1, 2, 2, 2, 8
if 0 <= k <= 10:
    k=k1-k
    if 0 <= q <= 10:
        q=q1-q
        if 0 <= l <= 10:
            l=l1-l
            if 0 <= v <= 10:
                v=v1-v
                if 0 <= n <= 10:
                    n=n1-n
                    if 0 <= p <= 10:
                        p=p1-p

print(k, q, l ,v, n, p)


#10430
A,B,C=map(int, input().split())
if 2<=A<=10000:
    if 2<=B<=10000:
        if 2<=C<=10000:
            print((A+B)%C)
            print(((A%C) + (B%C))%C)
            print((A*B)%C)
            print(((A%C)*(B%C))%C)


#2588 *
a=int(input())
b=input()

a1=a*int(b[2])
a2=a*int(b[1])
a3=a*int(b[0])
a4=a*int(b)
print(a1,a2,a3,a4,sep="\n")
