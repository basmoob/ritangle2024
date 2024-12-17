

import itertools
dice = [1,2,3,4,5,6]
coin = [1,2]
counter = 0

for d in itertools.product(dice,repeat=5):
    
    for i in itertools.combinations(d, 3):  # for each combination of combination
        print(i)
        a = i[0] 
        b = i[1]
        c = i[2]
        if (a+b>c) and (a+c>b) and (b+c>a):
            counter+=1
            break


print((7776-counter)/7776)
