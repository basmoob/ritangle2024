
total = 0
for a in range(0,3000):
    for b in range(0,3000):
        for c in range(0,3000):

            if (a*b*c) + (a*b) + (b*c) + (c*a) + a + b + c == 2024:
                
                if a < b < c and a != 0 and b != 0 and c != 0:
                    print(a)
                    print(b)
                    print(c)
                    print("done")
                    total = c + total
                    
                    print(total)