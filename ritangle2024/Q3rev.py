from itertools import *
import itertools
from contextlib import contextmanager

@contextmanager
def nested_break():
    class NestedBreakException(Exception):
        pass
    try:
        yield NestedBreakException
    except NestedBreakException:
        pass


def combination_checker(li):
    y = []
    y = list(map(int, li))
    

    with nested_break() as mylabel:
        for i in range(0, len(y)):
                                
            for s in combinations(y, i):
                
                if sum(s) == 120:
                    
                    return True
                    raise mylabel
   
def get_combinations(lst): # creating a user-defined method
     
    combination = []  # empty list 
    gg = []

                               
    
    with open('combs.txt', 'w+') as combs:
        for r in range(1, len(lst) + 1):         
            for sent in itertools.combinations(lst, r):   
                for g in range(0, len(sent)):

                    combs.write(f"{sent[g]},")
                combs.write("\n")



    with open('pockets.txt', 'w+') as outfile:
        combs = open('combs.txt', 'r')
        for line in combs:
            gg = []
            for u in line.split(","):
                gg.append(u)
            gg.pop(-1)
            
            if combination_checker(gg) != True:
                outfile.write(f"{gg}\n")
                
        combs.close()




 
           
objects = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,12, 12, 12, 12, 12, 12, 12, 12, 12,15, 15, 15, 15, 15, 15, 15,20, 20, 20, 20, 20,30, 30, 30,60]
#objects = [1,2,3,4,5,10,12,15,20,30,60]        


get_combinations(objects)

