def rotateLeft(d, arr):
    # Write your code here
    newlist=[]
    for i in range(d):
        newlist.append(arr[0])
        arr.remove(arr[0])
        arr.append(newlist[0])
        newlist.remove(newlist[0])
    return arr

print(rotateLeft(10,[1,2,3,4,5]))