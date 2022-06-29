# cook your dish here
t = int(input())


for i in range(t):

    x,y,a= [int(x) for x in input().split()]
    if x<a and a<y:
        print("YES")
    elif x==a :
        print("YES")
    else:
        print("NO")
