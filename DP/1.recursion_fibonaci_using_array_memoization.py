#FIBONACCI SERIES USING MEMOIZATION
#USING ARRAY DATA STRUCTURE


def fib(n,dp):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif dp[n] != -1:
        return dp[n]
    else:
        dp[n] = fib(n-1,dp)+fib(n-2,dp)
        return dp[n]
    


#jitna no ka nikalna hai usse ek length bada array/list bhejna padega taki element usme save ho saken
dp = [-1]*800
# print(fib(790,dp))




#FIBONACCI SERIES USING TABULATION METHOD

dp = [0]*(101)
dp[0]=0
dp[1]=1
for i in range(2,101):
    dp[i]=dp[i-1]+dp[i-2]

print(dp[5])


#USING FUNCTION
#TABULAR METHOD
# 1D ARRAY OR 2D LIST USE KAR SAKTE HAI 
# GENERALLY HAMARI TABLE KA LAST ELEM HI HAMAARA ANSWER HOTA HAI

def feb(n):
    table= [0]*(n+1)
    table[1]=1
    for i in range(2,n+1):
        table[i]= table[i-1]+table[i-2]
    return table[n]

#TABULAR  o(N)
#MEMOIZATION  o(N)

#RECURSION  o(2^N)
