x= []
n = int(input("enter no of elemnts"))
for i in range(0,n):
    ele = int(input())
    x.append(ele)
print(x)

revlist = x[::-1]
print(revlist)
