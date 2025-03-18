def fIndex(arr,elem,accumulator=0):
    if len(arr)==0:
        return -1
    if arr[0]==elem:
        return accumulator
    accumulator+=1
    return fIndex(arr[1:],elem,accumulator) 


# print(fIndex([5,1,2,4,3,2,7],7))



def allIndex(arr,elem,accumulator=0):
    if len(arr)==0:
        # return -1
        return
    if arr[0]==elem:
        print(accumulator)
    accumulator+=1
    return allIndex(arr[1:],elem,accumulator)



# print(allIndex([7,3,5,1,8,3,2,1,2,4,4,4],3))
allIndex([7,3,5,1,8,3,2,1,2,4,4,4],4)



#UDEMY WALA
def fIndex(arr,elem):
    if len(arr)==0:
        return -1
    if arr[0]==elem:
        return 0
    ans = fIndex(arr[1:],elem)

    if ans == -1:
        return ans
    else :
        return ans + 1



def lastIndex(arr,elem):
    if len(arr) == 0:
        return -1

    if arr[len(arr)-1] == elem :
        return len(arr)-1
    
    # return lastIndex(arr[:len(arr)-1],elem)


    # if ans == -1:
    #     return ans
    # else :
    #     # return arr.index(3)   CONSIDER IT IT IS SHORTCUT DISCOVERED BE ME
    #     return 1+ ans
    

# print(lastIndex([5,1,2,4,3,2,7],5))





