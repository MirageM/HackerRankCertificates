#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxElement' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER maxSum
#  3. INTEGER k
#

def maxElement(n, maxSum, k):
    # Function to calculate the sum of an arithmetic sequence from 1 to x
    def sequence_sum(x):
        return (x * (x + 1)) // 2
    
    left, right = 1, maxSum
    
    while left < right:
        mid = (left + right + 1) // 2
        
        # Calculate the sum of elements with values less than or equal to mid,
        # excluding the element at index k.
        total = sequence_sum(mid - 1)
        
        # If k is less than mid, add the contribution of the element at index k.
        if k <= mid:
            total += k
        
        # If k is greater than mid, add the contribution of all elements from 1 to mid.
        else:
            total += sequence_sum(mid) - sequence_sum(mid - k)
        
        # Calculate the sum of elements from k+1 to n.
        total += (n - k)
        
        if total <= maxSum:
            left = mid
        else:
            right = mid - 1
    
    return left
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    maxSum = int(input().strip())

    k = int(input().strip())

    result = maxElement(n, maxSum, k)

    fptr.write(str(result) + '\n')

    fptr.close()
