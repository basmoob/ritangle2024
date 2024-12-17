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


def combination_checker(list):
    
    with nested_break() as mylabel:
        for i in range(0, len(list)):
                                
            for s in product(list, repeat=i):
                
                if sum(s) == 120:
                    
                    return True
                    raise mylabel
   
def get_combinations(lst): # creating a user-defined method
     
  combination = []  # empty list 
  gg = []

  for r in range(1, len(lst) + 1):                             # generate all combinations of list
  # to generate combination
    combination.extend(itertools.combinations(lst, r))

  with open('qq3.txt', 'w') as outfile:          #opens a file with
    for sent in combination:                                           # for each combination, it checks if it can make 120 from it
      if combination_checker(sent) != True:
        outfile.write(f"{''.join(str(sent))}\n")                # writes into txt if no 120


 
           
objects = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,12, 12, 12, 12, 12, 12, 12, 12, 12,15, 15, 15, 15, 15, 15, 15,20, 20, 20, 20, 20,30, 30, 30,60]
        
objects = [1, 2, 3, 4, 5, 10, 12, 15, 60]

get_combinations(objects)

