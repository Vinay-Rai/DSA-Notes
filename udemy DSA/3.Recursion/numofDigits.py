def numDigit(n):
    if n == 0:
        return 0
    else:
        return 1 + numDigit(n//10)

print(numDigit(5122))