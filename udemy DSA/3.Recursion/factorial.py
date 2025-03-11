def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    

# print(factorial(2))


# print n to 1 using recursion

def show(n):
    if n==0:
        return
    print(n)
    show(n-1)

# show(5)

def sumNno(n):
    if n==1:
        return 1
    else:
        return n+sumNno(n-1)
    

# print(sumNno(5))




def listPrint(lst,i=0):
    if i==len(lst):
        return
    
    print(lst[i])
    # i+=1
    listPrint(lst,i+1)


# listPrint([1,2,3],0)





#power(2,n) or 2**n

def power2(n):
    if n==1:
        return 2
    else:
        return 2 * power2(n-1)
    
# print(power2(10))


# import sys
# sys.setrecursionlimit(5000)
# sum of N numbers usinfg recursion
def sum(n):
    if n==1:
        return 1
    else:
        return n + sum(n-1)

print(sum(100))