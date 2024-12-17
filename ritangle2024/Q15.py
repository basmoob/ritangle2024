import math
nine = "RITANGLE"
nines = []
counter = 0
for i in range(0,100001):
    nine = nine +"RITANGLE"
#RITANGLE #MULTIPLES OF 9
for n in range(1,100001):
    if n%90==0:   
        tup = (nine[counter],n)
        nines.append(tup)
        counter +=1



three = "TRIANGLE"
threes = []
count = 0
for i in range(0,100001):
    three = three +"TRIANGLE"
#TRIANGLE #MULTIPLES OF 3
for t in range(1,100001):
    g = math.sqrt((t*8)+1)
    if g.is_integer():   
        tup = (three[count],t)
        threes.append(tup)
        count +=1


for g in nines:
    for u in threes:
        if g[0] == u[0] and g[1] == u[1]:
            print(g)
            print(u)
            exit()
