#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    maximum=0
    minimum=0
    lowest = highest = scores[0]
    for i in range (len(scores)):
        if(scores[i]>highest):
            highest = scores[i]
            maximum += 1
        elif(scores[i]<lowest):
            lowest = scores[i]
            minimum += 1
    return(maximum,
            minimum)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
