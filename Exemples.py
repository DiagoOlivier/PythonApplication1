p,q = 1, 1
counter = 0
# 1000 iterations
for i in range(1,1001):
    a1 = p + 2*q
    b1 = p + q
    if len(str(a1)) > len(str(b1)):
        counter += 1
    p = a1
    q = b1

# printing the counter
print (counter)
