import numpy as np

twoDarray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8], [15,18,14,9]])  #tc o(1)
print(twoDarray)


# inserion o(mn)

# newTwoArray = np.insert(twoDarray,1,[1,2,3,4], axis=0)
# print(newTwoArray)

# newTwoArray = np.append(twoDarray,1,[[1,2,3,4]], axis=0)
# print(newTwoArray)



def accessElement(array, rowIndex, colIndex):
    if rowIndex>= len(array) and colIndex>= len(array[0]):    #tc and sc = o(n)
        print("Incorrect index")
    else:
        print(array[rowIndex][colIndex])

# accessElement(twoDarray,0,0)



#traversing twoDarray                                    tc = o(mn)  o(n^2)    sc=o(1)
for i in range (len(twoDarray)):
    for j in range(len(twoDarray[0])):
        print(twoDarray[i][j],end=" ")
    print()


#searching elements                                 tc = o(mn)  o(n^2)    sc=o(1)
value =9
for i in range (len(twoDarray)):
    for i in range (len(twoDarray)):
        for j in range(len(twoDarray[0])):
            if twoDarray[i][j]==value:
                print(f"the value is located at index {str(i)} , {str(j)}")


#deleting
newTdarray = np.delete(twoDarray,0,axis=1)
print(newTdarray)



# insertion and deletion dekh lena

#when to use aray
# 1. to store multiple variables of same Data
#2. random access

#when not
#diffrrent datatypes of data
#no reserve of memory