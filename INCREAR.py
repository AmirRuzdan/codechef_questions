import random

randNO =input( random.randint(1,10))
x= input(random.randint(1,1000))
y =input(random.randint(1,1000))
print(x)
print(y)
def even(n):
    if n%2==0:
        return True
    else:
        return False


for i in range(randNO):

    
    m = sum(x,y)
    if even(m)== True:
        if x>y:
            print((x-y)/2)
        else:
            print(y-x)
    elif even(m)== False:
        if even(x)==True:
            if x>y:
                print(int((x-y)/2)+2)
            else:
                print(y-x)
        else:
            if x>y:
                print(int((x-y)/2)+2)
            else:
                print(y-x)
