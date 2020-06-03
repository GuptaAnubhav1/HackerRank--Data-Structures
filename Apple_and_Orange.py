#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    output1 = []
    output2 = []
    for i in apples:
        if (a+i)>=s and (a+i)<=t:
            output1.append(i)
    for i in oranges:
        if (b+i)<=t and (b+i)>=s:
            output2.append(i)
    print (len(output1))
    print (len(output2))

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
