L = [1,2,3,3.3,5,6]
n = len(L)
if n%2==0:
    print "%.1f" %((L[n/2-1]+L[n/2]+0.0)/2)
else:
    print L[(n-1)/2]

