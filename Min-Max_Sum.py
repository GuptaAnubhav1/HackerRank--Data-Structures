#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    Total_sum = sum(arr)
    print(Total_sum-(max(arr)), Total_sum-(min(arr)))
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

miniMaxSum(arr)
