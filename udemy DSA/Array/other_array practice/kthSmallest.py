
def kthSmallest( arr,k):
    sorted_arr = set(arr)
    print(sorted_arr)
    for counter, item in enumerate(sorted_arr):
        if counter == k-1:
            return item

print(kthSmallest(arr=[10,2,4,29,5,0,6,3],k=7))