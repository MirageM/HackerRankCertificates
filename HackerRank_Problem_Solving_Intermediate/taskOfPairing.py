# Task Of Pairing
import math
import os
import random
import re
import sys

def taskOfPairing(freq):
	# Could break for n > sys.maxsize, but that's a lot
	n = len(freq)
	inf = sysm.maxsize
	if n == 1:
		return freq[0] // 2
	ans = 0
	# Normalize
	for i in range(n):
		x = 0 if freq[i] <= 2 else ((freq[i] + 1) // 2) - 1
		ans += x 
		freq[i] -= 2 * x
	dp = [-inf] * 6
	dp[freq[0]] = 0
	if freq[0] == 2:
		dp[0] = 1
	for i in range(1, n):
		dpp = [-inf] * 6
		f = freq[i]
		dpp[f] = max(dp)
		dpp[f + 3] = max(dp[1], dp[2], dp[4], dp[5])

		if f >= 1:
			# Case: Prev has at least one movable or immovable. Combine once.
			dpp[f - 1] = max(dp[1:]) + 1
			dpp[f - 1 + 3] = max(dpp[f - 1 + 3], max(dp[4], dp[5]) + 1)
		dp = dpp
	return ans + max(dp)

def taskOfPairing(freq):
	# Could break for n > sys.maxsize, but that's a lot
	n = len(freq)
	inf = sys.maxsize
	if n == 1:
		return freq[0] // 2
	ans = 0
	# Normalize
	for i in range(n):
		x = 0 if freq[i] <= 2 else ((freq[i] + 1) // 2) -1
		ans += x 
		freq[i] -= 2 * x
	dp = [-inf] * 6
	dp[freq[0]] = 0
	if freq[0] == 2:
		dp[0] = 1
	for i in range(1, n):
		dpp = [-inf] * 6
		f = freq[i]
		dpp[f] = max(dp)
		dpp[f + 3] = max(dp[1], dp[2], dp[4], dp[5])
		if f >= 1:
			dpp[f - 1] = max(dp[1:]) + 1
			dpp[f - 1 + 3] = max(dpp[f - 1 + 3], max(dp[4], dp[5]) + 1)
		if f >= 2:
			dpp[f - 2] = max(dp) + 1
			dpp[f - 2 + 3] = max(dp[1], dp[2], dp[4], dp[5]) + 1
		dp = dpp
	return ans + max(dp)


def taskOfPairing(freq):
	n = len(freq)
	inf = sys.maxsize
	if n == 1:
		return freq[0] // 2
	ans = 0
	# Normalize
	for i in range(n):
		x = 0 if freq[i] <= 2 else ((freq[i] + 1) // 2) - 1
		ans += x 
		freq[i] -= 2 * x 
	dp = [-inf] * 6
	dp[freq[0]] = 0
	if freq[0] == 2:
		dp[0] = 1
	for i in range(1, n):
		dpp = [-inf] * 6
		f = freq[i]
		dpp[f] = max(dp)
		dpp[f + 3] = max(dp[1], dp[2], dp[4], dp[5])
		if f >= 1:
			dpp[f - 1] = max(dp[1:]) + 1
			dpp[f - 1 + 3] = max(dpp[f - 1 + 3], max(dp[4], dp[5]) + 1)
		if f >= 2:
			dpp[f - 2] = max(dp) + 1
			dpp[f - 2 + 3] = max(dp[1], dp[2], dp[4], dp[5]) + 1
		dp = dpp
	return ans + max(dp)

