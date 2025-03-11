def sumN (n):
    if n==0:
        return 0 
    else:
        return n + sumN(n-1)
    
# if __name__=="__main__":
# print(sumN(4))




#sir ke style me

def sumN(n):
    if n==0:
        return 0 
    
    smallans = sumN(n-1)
    ans = n + smallans
    return ans

print(sumN(4))