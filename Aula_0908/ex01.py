x = {"RN" : "Natal", "PB" : "João Pessoa", "PE" : "Recife"}
print(x)
print(type(x))
x["AM"] = "Manaus"
#print(x["Natal"])
print(*x)

for item in x.items():
  print (item, item[0], item[1])
  

#print(x["AM"])


y = [ 1, 2, 3 ]
print(y)
print(type(y))
#print(y[10])
print(*y)


