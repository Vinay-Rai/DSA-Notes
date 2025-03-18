def bubble_sort(lst):
    # Your code goes here
    for i in range(len(lst)):
        for j in range(1,len(lst)-i):
            if lst[j-1]>lst[j]:
                lst[j-1],lst[j]=lst[j],lst[j-1]
            
    return lst


print(bubble_sort([10,2,5,45,50,7,9]))


#UDEMY SIR
def bubble(arr):
    n = len(arr)
    for passes in range(0,n):
        for j in range(0,n-1-passes):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

print(bubble([10,2,5,45,50,7,9]))