l = [2, 5, 10]
n = 1
for i in l:
    n *= i
t = 0
while n%10==0:
    t += 1
    n /= 10

print t