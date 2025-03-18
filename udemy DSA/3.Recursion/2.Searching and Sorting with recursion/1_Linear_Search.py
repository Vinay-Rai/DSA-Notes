def linear_Search_Using_Recurison(l1,x,index):
    #Base Case
    if(len(l1)== index):
        return False
    
    ansFromRecurison = linear_Search_Using_Recurison(l1,x,index+1)

    # if(ansFromRecurison == True):
    #     return  True
    
    # if(l1[index]==x):
    #     return True
    # return False

    return l1[index]==x or ansFromRecurison

ans = linear_Search_Using_Recurison([1,4,3,2,6,5,8],5,0)
print(ans)



#Recursion Better

def linear_Search_Using_Recurison_Better(l1,x,index):

    if(len(l1)== index):
        return False

    if(l1[index]==x):
        return True
    
    return linear_Search_Using_Recurison_Better(l1,x,index+1)


l1 = [ i for i in range(10000)]
ans = linear_Search_Using_Recurison_Better([1,4,3,2,6,5,8],5,0)
print(ans)


    
