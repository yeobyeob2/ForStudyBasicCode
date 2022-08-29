'''
#1330
A, B=map(int, input().split())
if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")


#9498
s=int(input())
if 0 <= s <= 100:
    if 90 <= s <= 100:
        print("A")
    elif 80 <= s <= 89:
        print("B")
    elif 70 <= s <= 79:
        print("C")
    elif 60 <= s <= 69:
        print("D")
    else:
        print("F")


#2753
y=int(input())
if y%4 == 0:
    if y%100 != 0 or y%400 == 0:
        print(1)
    else:
        print(0)
else:
    print(0)


#14681
x=int(input())
y=int(input())

if -1000 <= x <= 1000 or x != 0:
    if -1000 <= y <= 1000 or y != 0:
        if x>0 and y>0:
            print(1)
        elif x<0 and y>0:
            print(2)
        elif x<0 and y<0:
            print(3)
        else:
            print(4)

#2884
H, M=map(int, input().split())
if 0 <= H <= 23:
    if 0 <= M <= 59:
       if M > 44:
           print(H,M-45)
       elif M < 45 and H > 0:
           print(H-1,M+15)
       else:
           print(23,M+15)

#2525 *
a, b=map(int, input().split())
c=int(input())
a = a+c//60
b = b+c%60

if b >= 60:
    a += 1
    b -= 60
if a >= 24:
    a -= 24

print(a, b)
'''

#2480 *
a, b, c=map(int, input().split())
if a == b and b == c and a == c:
    print(10000+(a*1000))
elif a == b or a == c:
    print(1000+(a*100))
elif b==c:
    print(1000+(b*100))
else:
    print(max(a,b,c)*100)
