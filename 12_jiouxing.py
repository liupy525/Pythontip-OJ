l = [2, 5, 10]
n = 1
for i in l:
    n *= i
while n%10==0:
    n = n/10
t = n%10
print t%2