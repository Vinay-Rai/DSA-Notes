def oneTON(n):
    if n<=0:
        return
    
    oneTON(n-1)                 #THIS IS HEAD RECURSION
    print(n)

# print(oneTON(5))


# returning list
def count_to_n(n):
  
    if n<=0:
        return []
    
    lst = count_to_n(n-1)
    lst.append(n)
    
    return lst

# print(count_to_n(5))


#N TO ONE
def nTOone(n):           #THIS IS TAIL RECURSION
    if n<=0:
        return
    
    print(n)
    nTOone(n-1)





def count_down(n):

    if n == 0:
        return []
    else:
        lst = count_down(n-1)
        lst.insert(0,n)
        return(lst)

print(count_down(5))