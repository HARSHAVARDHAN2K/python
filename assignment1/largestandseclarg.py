from cmath import sqrt


def largest(x):
    a = x[0]
    for i in x:
        if a<i:
            a=i

    return a


def seclar(x):
    a = x[0]
    b = x[0]
    for i in x:
        if a<i:
            b=a
            a=i
    if a==b:
        return 0
    return b

b = [1,2,3,4,5,6]
print("Largest:",largest(b))
seclargest = seclar((5,5,5,5,5))
if(seclargest==0):
    print("Second Largest doesn't exist:")
else:
    print("Second largest : ", seclargest)
print("\n")
