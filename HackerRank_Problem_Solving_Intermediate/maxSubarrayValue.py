# Maximum Subarray Value
import math
import os
import random
import re
import sys

def maxSubarrayValue(arr):
	even = [0]
	odd = [0]
	for i in range(len(arr)):
		if i % 2 == 0:
			even.append(even[-1] + arr[i])
			odd.append(odd[-1])
		else:
			even.append(even[-1])
			odd.append(odd[-1] + arr[i])
	ans = 0
	for i in range(len(arr)):
		for j in range(i + 1, len(arr) + 1):
			a = even[j] - even[i]
			b = odd[j] - odd[i]
			ans = max(ans, (a-b)**2)
	return ans


def maxSubarrayValue(arr):
	even = [0]
	odd = [0]
	for i in range(len(arr)):
		if i % 2 == 0:
			even.append(even[-1] + arr[i])
			odd.append(odd[-1])
		else:
			even.append(even[-1])
			odd.append(odd[-1] + arr[i])
		ans = 0
		for i in range(len(arr)):
			for j in range(i + 1, len(arr) + 1):
				a = even[j] - even[i]
				b = odd[j] - odd[i]
				ans = max(ans, (a-b)**2)
	return ans


def maxSubarrayValue(arr):
	even = [0]
	odd = [0]
	for i in range(len(arr)):
		if i % 2 == 0:
			even.append(even[-1] + arr[i])
			odd.append(odd[-1])
		else:
			even.append(even[-1])
			odd.append(odd[-1] + arr[i])
	ans = 0
	for i in range(len(arr)):
		for j in range(i + 1, len(arr) + 1):
			a = even[j] - even[i]
			b = odd[j] - odd[i]
			ans = max(ans, (a-b)**2)
	return ans