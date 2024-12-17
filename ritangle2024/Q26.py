

d = 1000000
start = (5*d)/10
start = int(start)

valid = 0
total = 0

for a in range(start,d):
    for b in range(start,d):
        total+=1
        if round((a/d) * (b/d)) == 1:
            valid+=1
print(f"valid is {valid} and total is {total}")
print(valid/total)