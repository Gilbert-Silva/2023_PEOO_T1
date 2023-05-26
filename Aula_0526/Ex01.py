x = 5
y = 10.5
s = "10/10/2000"
print(x)
print(type(x))
print(y)
print(type(y))
print(s)
print(type(s))
print(x + y)
print(s + s)
print(5 * s)
#print(s * s)
print(s.split('/'))
print(s[0])
l = s.split('/')
print(type(l))
print(l[0])
print(type(l[0]))
x = 50
y = 5
b = x > y
print(b)
print(type(b))

if x > y: print(f"{x} > {y}")
else: 
  if x == y: print(f"{x} == {y}")
  else: print(f"{x} < {y}")  
  
if b: print(f"{x} > {y}")
elif x == y: print(f"{x} == {y}")
else: print(f"{x} < {y}")

for k in range(10):
  print(k+1)

for k in range(2,11,2):
  print(k, end=" ")
print()
for k in range(10,1,-2):
  print(k, end="\t")
print()
k = 10
while k > 1:
  print(k)
  k = k - 2
  
def soma(x, y):
  return x + y

print(soma(10, 10))
print(soma("10", "10"))
#print(soma(10, "10"))

z = soma("10", "10")
print(type(z))

def escreve(x):
  print(x)
  if (x < 10): escreve(x + 1)

escreve(1) # print(1) if 1 < 10: escreve(2)
           # print(2) if 2 < 10: escreve(3)
           # print(3) if 3 < 10: escreve(4)
           # ...
           # print(9) if 9 < 10: escreve(10)
           # print(10) if 10 < 10:







