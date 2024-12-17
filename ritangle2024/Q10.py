from num2words import *
import re



def wordCount(li, strr):
   
    wCount = li[10]
  
    

    u = re.split(r'\s|-', strr)
    u.pop(-1)
    #u = strr.split(" ", "-")
    a = len(u)
    if a == wCount:
        return True

def vowelCount(str, li):
    count = 0
    vowels = "aeiou"
 
    for alphabet in str:
        if alphabet.lower() in vowels:
            count+=1
    if count == li[17]:
        return True

def wordizer(li):
    strings = ""
    for n in li:
        try:
            int_value = int(n)
        except ValueError:
    # it wasn't an int, do something appropriate
            strings = strings + n + " "
        else:
    # it was an int, do something appropriate
            strings = strings + str(num2words(n)) + " "
    return strings

counter = 0






for n in range(0,100):
    for i in range(0,100): 
        
        sen = ["count","carefully", "and", "you", "will", "see","that","this","sentence","contains",n,"words","and","between","them","they","contain",i,"vowels"]

        var1 = wordizer(sen)
        var2 = vowelCount(var1,sen)
        var3 = wordCount(sen, var1)

        if var3 and var2:
            print(var1)
            product = sen[10] * sen[17]
            counter += product

print(counter)
'''
sen = ["count","carefully", "and", "you", "will", "see","that","this","sentence","contains",21,"words","and","between","them","they","contain","vowels"]
print(vowelCount(sen))'''