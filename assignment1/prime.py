def primenUM(x:int,y:int):
    for i in range(x,y):
        flag=False
        if i==1 or i==0:
            flag=True
        else:
            for j in range(2,i//2+1):
                if i%j == 0:
                    flag=True
                    break
        if flag==False:
            print(i,end="\t")

print("Prime Number :")
primenUM(0,100)