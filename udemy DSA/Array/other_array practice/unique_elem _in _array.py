def unique_elem(arr):
    d={}
    for i in arr:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    print(d)
    return len(d) 

arr=[0,3,1,4,2,0,1,1,2,0,1,2,5,]
# print(unique_elem(arr))

s = set(arr)
# print(len(s),s)

temp_arr =[]
for i in arr:
    if i not in temp_arr:
        temp_arr.insert(0,i)
    
# print(temp_arr)


#WRONG HAI SAMAJH LENA BAD ME 
# def countUnique(arr,n):
#     count =1
#     for i in range(1,n):
#         if arr[i]!=arr[count-1]:
#             arr[count-1]=arr[i]
#             count+=1
#             print("hello")
            
#         return count
    
# arr=[10,20,30,30]
# print(countUnique(arr,len(arr)))


