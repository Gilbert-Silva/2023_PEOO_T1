x = [1, 2, 3, 4]
y = x[:]
print(x)
print(y)
y[0] = 10
print(x)
print(y)
print(type(x))
print(type(y))
x.append(20)
print(x)
x.insert(2, 10)
print(x)
if 5 in x: x.remove(5)
print(x)
print(x.index(20))
print(x.count(10))
x.reverse()
print(x)
x.sort()
print(x)






