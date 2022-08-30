'''
#10818
n=int(input())
a=list(map(int,input().split()))
print(min(a),max(a))

#2562
list=[]
for i in range(9):
    a=int(input())
    list.append(a)
print(max(list))
print(list.index(max(list))+1)

#3052
list=[]
for i in range(10):
    a=int(input())
    list.append(a%42)
set=set(list) ****
print(len(set))

#1546
n=int(input())
m=list(map(int, input().split()))
max=max(m)

list=[]
for i in m:
    list.append(i/max*100)
average= sum(list)/n
print(average)

#8958 *
n=int(input())

for i in range(n):
    s = 0
    a = 1
    ox=list(input())
    for j in ox:
        if j == "O":
            s += a
            a += 1
        else:
            a=1
    print(s)

#4344 *
c=int(input())
av_list=[]

for i in range(c):
    n=list(map(int, input().split()))
    av=sum(n[1:])/n[0]
    c=0
    for j in n[1:]:
        if j > av:
            c += 1
    per=c/n[0]*100
    print(f"{per:.3f}%")
'''






