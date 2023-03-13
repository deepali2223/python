x= []
n = int(input("enter no of elemnts"))
for i in range(0,n):
    ele = int(input())
    x.append(ele)
print(x)
y= []
n = int(input("enter no of elemnts"))
for i in range(0,n):
    ele = int(input())
    y.append(ele)
print(y)
if len(x) > len(y):
    print("greatest list is x")
elif len (x) < len(y):
    print("greatest list is y")
else:
    print("both are equal")
