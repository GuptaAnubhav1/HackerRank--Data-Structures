#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def leapyear(year):
    while(year>=1700 and year<=2700):    
        if((year <= 1917) & (year%4 == 0)) or ((year > 1918) & (year%400 == 0 or ((year%4 == 0) & (year%100 != 0)))):
            return True
        else:
            return False
        
    
def dayOfProgrammer(year):
    if(year==1918):
        return("26.09."+ str(year))
    elif leapyear(year):
        return("12.09."+str(year))
    else:
        return("13.09."+str(year))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
