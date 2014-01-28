def gongyueshu(a, b):
    n = 1
    for i in range (2, min(a,b)+1):
        if a%i==0 and b%i==0:
            n = i
    return n

print gongyueshu(12, 39)