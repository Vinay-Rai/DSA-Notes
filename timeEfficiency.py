"""to measure the time of running of code but this is not used in industry"""
"""
PROBLEM WITH THIS APPROACH

1.Different time for diffrent algorithm
2.Time varies if implementation changes
3.Diffenent machines different time
4.Does not work for extremely small input
5.Time varies for different inputs,but can't establish a relationship
"""
import time
start=time.time()
for i in range(1,101):
    print(i)

print(time.time()-start)