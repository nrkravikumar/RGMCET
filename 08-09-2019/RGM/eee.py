def nat(k):
    for i in range(1,k+1):
        print(i,end=" ")
    return 

def facto(m):
    fact=1
    for i in range(m,0,-1):
        fact *=i
    print("Given number is: {} and its factorial is: {}".format(m,fact))
    return