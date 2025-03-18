def linearSearch(arr,element):
    size = len(arr)
    for i in range(size):
        if arr[i]==element:
            return i
    
    return -1

arr = [2,4,1,675,0,7,3]
print(linearSearch(arr,10))