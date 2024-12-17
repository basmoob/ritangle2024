from itertools import *
import itertools
from contextlib import contextmanager

@contextmanager
def nested_break():                          #need this to break out of two 'for loops' later  have no idea what it acc does
    class NestedBreakException(Exception):
        pass
    try:
        yield NestedBreakException
    except NestedBreakException:
        pass

def combination_checker(li):
    y = []
    y = list(map(int, li))    # need to list and map to convert list of strings to ints
    

    with nested_break() as mylabel:      # need this to break out of two for loops
        for i in range(0, len(y)):
                                
            for s in combinations(y, i):       # checks each combination is equal to 120
                
                if sum(s) == 120:
                    
                    return True
                    raise mylabel
   
def get_combinations(lst): # creating a user-defined method

    for r in range(1, len(lst) + 1):     
            for sent in itertools.combinations(lst, r): # for each combination

                with open('combs.txt', 'r') as combs:

                    list2 = combs.read()
                    l1= list2.strip(')(').split(',')

                if sum(sent) > 160 :
                    if combination_checker(sent) != True:
                        if sum(map(int,l1)) < sum(sent):

                            with open('combs.txt', 'w') as combs:
                                combs.write(str(sent))              
          
objects = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,12, 12, 12, 12, 12, 12, 12, 12, 12,15, 15, 15, 15, 15, 15, 15,20, 20, 20, 20, 20,30, 30, 30,60]
#objects = [1,2,3,4,5,10,12,15,20,30,60]        


get_combinations(objects)

