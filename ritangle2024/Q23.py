
a = (5/6)*(1/6)
b = 0

for i in range(1,20):
    b = b + (((5/6)**((3*i)+1))*(1/6))

print(a+b)
