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
'''
#8958
n=int(input())
list=[]
s=0
a=0

for i in range(n):
    ox=input()
    list.append(ox)
    for j in list:

print(list)