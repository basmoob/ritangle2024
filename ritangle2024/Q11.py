


# Python3 program to find number of days
# between two given dates
from datetime import date
 
 
def numOfDays(date1, date2):
  #check which date is greater to avoid days output in -ve number
    if date2 > date1:   
        return (date2-date1).days
    else:
        return (date1-date2).days
 
 


temp_d = 1
temp_mm = 1
temp_yy = 24
li = []
for yy in range(24,100):
    for mm in range(1,13):
        for d in range(1,9):
            
            
            if mm % d == 0 and yy % mm == 0 and d < mm and mm < yy:
                
                

                date1 = date(temp_yy + 2000, temp_mm, temp_d)
                date2 = date(yy + 2000, mm, d)

                value = numOfDays(date1,date2)

                li.append(date1)
                li.append(date2)
                li.append(value)

                if numOfDays(date1,date2) >= 730:
                    print(temp_d,temp_mm,temp_yy,d,mm,yy)
                    print(value)
                    
                

                temp_d = d
                temp_mm = mm
                temp_yy = yy

#n = max(li)
print(li)