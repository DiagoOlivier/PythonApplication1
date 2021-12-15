from collections import OrderedDict
l = []
for i in range (2,101):
    for j in range (2,101):
        l.append(i**j)
l.sort()
print(len(list (OrderedDict.fromkeys(l))))

