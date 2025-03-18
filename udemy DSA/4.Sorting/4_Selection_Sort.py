def Selection_Sort(arr):
    for i in range(len(arr)):
        index = -1
        min = arr[i]
        for j in range(i+1,len(arr)):
            if arr[j]<min:
                min = arr[j]
                index=j
        arr[i],arr[index]=arr[index],arr[i]

    return arr

print(Selection_Sort([10,9,8,7]))
            


#UDEMY WALE
def selection(arr):
    n=len(arr)
    for i in range(n-1):
        min_index = i
        
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index = j
        arr[i],arr[min_index]=arr[min_index],arr[i]

    return arr


print(selection([10,9,8,7]))
                
            

