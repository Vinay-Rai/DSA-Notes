import time

def fiboiter(num):
    prevnum = 0
    current = 1
    for i in range(1,num):
        preprevnum = prevnum
        prevnum = current
        current = prevnum + preprevnum
    return current


def fiborecur(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    # if num ==0 or num ==1:
    #     return num
    else:
        return fiborecur(num-1)+fiborecur(num-2)
    

# USING UDEMY PMI CONCEPT
def fibonicci(n):
    if n ==0 or n ==1:    #two base cases because two no to min provide karne hi padhenge
        return n
    
    last = fibonicci(n-1)
    secondlast = fibonicci(n-2)

    ans = last + secondlast
    return ans


if __name__=="__main__":
    num = int(input("Enter NUmber"))

    init = time.time()

    print(f"using recursion the fibonaci no at {num} is {fiborecur(num)}")
    # print(f"using iteration the fibonaci no at {num} is {fiboiter(num)}")

    print(f"it took {time.time()-init} seconds")