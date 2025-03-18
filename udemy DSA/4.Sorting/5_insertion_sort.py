def insertion_sort(arr):
    n = len(arr)
    for current in range(1,n):
        currentCard = arr[current]
        correctPosition = current -1   #it will go from i-1 to 0
        while correctPosition >= 0:
            if(arr[correctPosition]<currentCard):
                break
    
            else:
                arr[correctPosition + 1] = arr[correctPosition]
                correctPosition -=1
            
            arr[correctPosition+1] = currentCard
    return arr
    
print(insertion_sort([10,2,5,45,50,7,9]))