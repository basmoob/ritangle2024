from operator import length_hint
import  math

def checker(lis):     #checks to see if all digits in the sequence are different to each other
    
    on = []
    total = 0

    for n in lis:
        x = int(n)
        total = x + total
        if x < 10:           # if the value in the list is under 10, that means that it can be split into 0 and the value
            n1 = 0 
            n2 = x
        else:
            n1 = math.trunc(x/10)             #truncate it so that the first value is stored
            n2 = x%10                         #mod because if it is ex 56 then n2 would be 6 cuz remainder from /10 is 6 and if it was 50 then n2 is 0
        on.append(n1) 
        on.append(n2) 
        
    st = set(on)    #removes any duplicate values from list
    if len(st) == len(on):   #checks there was dupe vals or nah. If sequence valid then it returns true
        return True        
        
    

def createList(start, stop, count):              #makes custom arithmetic sequences
    nl = list(range(start, stop, count))
    return nl[0:5]      



Total = 0

for i in range(1, 25):
    for j in range(0,99):           #makes 99 sequences for each value of d from 0-24 as any bigger and sequence would end at three digit "100" which makes it invalid
        a = createList(j,100, i)

        if len(a) == 5:   #checks sequence
            
            #for u in range(0,5):
                #if a[u] <= 9:           #checks if number is two digit, if not then it adds 0
                    #a[u] = f"0{a[u]}" 

                if checker(a) == True:       #checks if the whole sequence is valid
                    print(a)
                    for n in a:
                        y = int(n)
                        Total = Total + y           #adds total of the valid sequences

                    print(Total) 
                        
                #else:
                    #a[u] = f"{a[u]}"
            
            





