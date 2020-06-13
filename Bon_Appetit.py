#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    s = sum(bill) - bill[k]    
    if(s/2==b):
        return("Bon Appetit")
    else:
        return(int(b-(s/2)))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    
    result = bonAppetit(bill, k, b)
    print(result)
