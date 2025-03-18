def ALLIndex(arr,elem):
    if len(arr) == 0:
        # return -1
        return

    if arr[len(arr)-1] == elem :
        print(len(arr)-1)
    
    return ALLIndex(arr[:len(arr)-1],elem)


# ALLIndex([5,1,2,4,3,2,7],2)




#UDEMY WALA CODE

def FirstIndexBetterApproach(l1,x,index):  
    if len(l1)==index:
        return -1
    
    if(l1[index]==x):
        return index
    
    return FirstIndexBetterApproach(l1,x,index+1)

# print(FirstIndexBetterApproach([3,2,5,2],10,0))



#ALL INDICES
def printAllIndicesOfElement(l1,x,index):   
    if len(l1)==index:
        return 
    
    if(l1[index]==x):
        print(index)
    
    printAllIndicesOfElement(l1,x,index+1)


printAllIndicesOfElement([3,2,5,2],10,0)




#ALL INDECES  USING HELPER FUNCTION

def printAllIndicesOfElementHelper(l1,x,index):   
    if len(l1)==index:
        return 
    
    if(l1[index]==x):
        print(index)
    
    printAllIndicesOfElementHelper(l1,x,index+1)


def printAllIndicesOfElement(l1,x):
    printAllIndicesOfElementHelper(l1,x,0)

# printAllIndicesOfElement([3,2,5,2],10)




#TO PRINT IN REVERSE ORDER


def printAllIndicesOfElementHelper(l1,x,index):   
    if len(l1)==index:
        return 
    
    printAllIndicesOfElementHelper(l1,x,index+1)
    
    if(l1[index]==x):
        print(index)
    

def printAllIndicesOfElement(l1,x):
    printAllIndicesOfElementHelper(l1,x,0)

printAllIndicesOfElement([3,2,5,2],2)



#  UPDATTE ALL INDICES IN PROVIDED LIST

def updateAllIndicesInProvidedLisr(l1,x,index,anslist):
    if len(l1)==index:
        return 
    
    if(l1[index]==x):
        anslist.append(index)

    updateAllIndicesInProvidedLisr(l1,x,index+1,anslist)

anslist = []
updateAllIndicesInProvidedLisr([3,2,5,2,8,2,1],2,0,anslist)
print(anslist)
    

#IN REVERSE ORDER

def updateAllIndicesInProvidedLisr(l1,x,index,anslist):
    if len(l1)==index:
        return 
    
    updateAllIndicesInProvidedLisr(l1,x,index+1,anslist)
    
    if(l1[index]==x):
        anslist.append(index)


anslist = []
updateAllIndicesInProvidedLisr([3,2,5,2,8,2,1],2,0,anslist)
print(anslist)




#UPDATE GLOBAL LIST WITH ALL ELEMENT OF ELEMENT

anslist = []

def updateAllIndicesInProvidedLisr(l1,x,index):
    if len(l1)==index:
        return 

    if(l1[index]==x):
        anslist.append(index)

    updateAllIndicesInProvidedLisr(l1,x,index+1)


updateAllIndicesInProvidedLisr([3,2,5,2,8,2,1],2,0)
print(anslist)



#RETURN ALL INDEX AS LIST

def returnlist(l1,x,index):

    if len(l1)==index:
        return []
    
    smallList = returnlist(l1,x,index+1)

    if(l1[index]==x):
        smallList.insert(0, index)
    
    return smallList

ansList = returnlist([3,2,5,2],2,0)
print(ansList)
