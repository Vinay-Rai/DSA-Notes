from array import *

#ARRAY CREATION
arr1 = array("i",[1,2,3,4,5])  #i for integers and d for double
#time compleity of array creation is constant time operation 
#when we create an empty array and assign value one by one then it is order of N TIME operation
print(arr1)




#ARRAY INSERTION
arr1.insert(6,7)  #index and element
print(arr1)

arr1.insert(0,0) #all element shift ho jen or 0 zeroth index pe fill ho je
print(arr1) #array shifts elements in right if we insert element in starting or middle

#INSERTION OF ELEMENT AT THE END OF ARRAY IS O(1) TIME C. OPERATION
#OTHER POSITION PAR O(n)




#practice
print("reversed array")
arr1.reverse()
print(arr1)
print(arr1[2])

print("reversed array")




#TRAVERSING OF ARRAY
def traverseArray(array):
    for i in array:
        print(i)

traverseArray(arr1)    # TC o(n)  SC O(1)




#ACCESS ARRAY ELEMENT          O(1) constant time operation  sc o(n)
def accessElement(array,index):
    if index >= len(array):
        print("index out of range")
    else:
        print(array[index])
    

accessElement(arr1,8)




#finding/searching an element 
# three ways
#1. using index
#2. binary search if data is sorted
#3. by traversing every element


def searchInArray(array,value): #tc  O(n)  sc o(1)
    for i in arr1:
        if i == value:
            return True
    return "The element does not exits in this array"



#Removing element   removal from last o(1) otherwise o(n)
arr1.remove(1)
print(arr1)



