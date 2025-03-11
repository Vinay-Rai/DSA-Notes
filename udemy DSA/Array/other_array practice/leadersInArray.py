def leader(arr):
    
    for i in range(len(arr)):
        flag=0
        for j in range(i+1,len(arr)):
            if arr[j]>=arr[i]:
                flag=1
                break
        if flag==0:
            print(arr[i])


arr = [7,10,4,8,4,6,5,2]
# leader(arr)

def leaderstwo(arr):
    current_leader=arr[-1]
    for i in range(len(arr)-1,0,-1):
        if arr[i] > current_leader:
            print(current_leader)
            current_leader = arr[i]
    print(current_leader)
leaderstwo(arr)
        

